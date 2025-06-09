<template>
  <div class="container">
    <h2 class="title">Team members</h2>
    <p class="subtitle">You have ({{ teamMembers.length }}) team members.</p>

    <div v-if="teamMembers.length === 0" class="empty-state">
        <p class="no-members-text">No team members yet.</p>
        <router-link to="/add">
            <button class="big-add-btn">➕ Add a Member</button>
        </router-link>
        </div>
        <div v-else class="add-button">
        <router-link to="/add">
            <button class="add-member-btn">+</button>
        </router-link>
    </div>


    <ul class="card-list">
        <ul class="card-list">
        <li
            v-for="member in teamMembers"
            :key="member.id"
            class="card"
            @click="selectMember(member)"
        >
            <!-- Show avatar, name, and role -->
            <img
            class="avatar"
            :src="member.avatar || defaultAvatar"
            alt="Foto del miembro"
            />

            <p class="name">{{ member.first_name }} {{ member.last_name }}</p>
            <p class="role">{{ member.role }}</p>

            <!-- Bubble with email and phone number -->
            <div
            v-if="selectedMember && selectedMember.id === member.id"
            class="bubble"
            @click.stop
            >
            <p><strong>Email:</strong> {{ member.email || 'No disponible' }}</p>
            <p><strong>Phone number:</strong> {{ member.phone || 'No disponible' }}</p>

            <router-link :to="`/edit/${member.id}`" class="edit-link" @click.stop>
                ✏️ Edit
            </router-link>
            </div>
        </li>
        </ul>
        </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      teamMembers: [],
      selectedMember: null,
      defaultAvatar: '/images/avatar.png'
    }
  },
  created() {
    axios
      .get("http://localhost:8000/api/team-members/")
      .then((response) => {
        this.teamMembers = response.data;
      })
      .catch((error) => {
        console.error("Error al obtener miembros:", error);
      });
  },
  methods: {
    selectMember(member) {
      this.selectedMember =
        this.selectedMember && this.selectedMember.id === member.id
          ? null
          : member;
    },
  },
};
</script>

<style scoped>
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: #f8f9fa;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.07);
}

.title {
  text-align: center;
  color: #343a40;
  font-size: 24px;
  margin-bottom: 24px;
}

.card-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.card {
  background: #f1f3f5;
  padding: 16px;
  margin-bottom: 16px;
  border-radius: 12px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.name {
  font-size: 18px;
  color: #212529;
  font-weight: bold;
  margin: 0;
}

.role {
  font-size: 14px;
  color: #495057;
  margin: 4px 0 0;
}

.add-button {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
}

.add-member-btn {
  background-color: #4a90e2;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.add-member-btn:hover {
  background-color: #357ab8;
}

.edit-link {
  display: inline-block;
  margin-top: 10px;
  font-size: 14px;
  color: #334bd6;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

.edit-link:hover {
  color: #6473de;
  text-decoration: underline;
}

.avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 12px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

.subtitle {
  text-align: center;
  color: #6c757d;
  font-size: 14px;
  margin-bottom: 24px;
}
.empty-state {
  text-align: center;
  padding: 60px 20px;
}

.no-members-text {
  font-size: 18px;
  color: #6c757d;
  margin-bottom: 20px;
}

.big-add-btn {
  background-color: #4a90e2;
  color: white;
  border: none;
  padding: 16px 24px;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.big-add-btn:hover {
  background-color: #357ab8;
  transform: scale(1.05);
}


</style>
