<template>
  <div class="container">
    <h2 class="title">Edit team member</h2>
    <p class="subtitle">Update email, phone number or role.</p>

    <form @submit.prevent="submitForm" class="form">
      <label class="input-label">Info:</label>

      <label>Name:</label>
      <input v-model="form.first_name" required class="input" />

      <label>Last Name:</label>
      <input v-model="form.last_name" required class="input" />

      <label>Email:</label>
      <input v-model="form.email" type="email" required class="input" />

      <label>Phone number:</label>
      <input v-model="form.phone" required class="input" />

      <label class="input-label">Role:</label>
      <div class="role-group">
        <div class="radio-option" v-for="option in roleOptions" :key="option.value">
          <label class="radio-label">
            <input
              type="radio"
              v-model="form.role"
              :value="option.value"
              class="radio-input"
            />
            <span class="radio-text">{{ option.label }}</span>
          </label>
        </div>
      </div>

      <div class="form-actions dual-buttons">
        <button type="button" @click="deleteMember" class="delete-btn">🗑 Delete</button>
        <button type="submit" class="submit-btn">Save Changes</button>
        <button type="button" class="back-btn" @click="$router.push('/')">Back to list</button>
      </div>

    </form>
  </div>

  <div v-if="showModal" class="modal-overlay">
    <div class="modal">
        <h3>Are you sure?</h3>
        <p>You are about to delete this member. This action cannot be undone.</p>
        <div class="modal-actions">
            <button class="cancel-btn" @click="showModal = false">Cancel</button>
            <button class="confirm-btn" @click="confirmDelete">Yes, delete</button>
        </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
        form: {
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        role: 'regular'
        },
        roleOptions: [
        { value: 'regular', label: "Regular - Can’t delete members" },
        { value: 'admin', label: "Admin - Can delete members" }
        ],
        showModal: false
    }
    },
    methods: {
        submitForm() {
        const memberId = this.$route.params.id
        axios
            .put(`http://localhost:8000/api/team-members/${memberId}/`, this.form)
            .then(() => {
            this.$router.push('/')
            })
            .catch(error => {
            console.error('Error updating member:', error)
            })
        },
        deleteMember() {
            this.showModal = true;
        },
        confirmDelete() {
            const memberId = this.$route.params.id;
            axios
                .delete(`http://localhost:8000/api/team-members/${memberId}/`)
                .then(() => {
                this.$router.push('/');
                })
                .catch((error) => {
                console.error('Error deleting member:', error);
                });
        }

    },
    created() {
        const memberId = this.$route.params.id;
        axios
            .get(`http://localhost:8000/api/team-members/${memberId}/`)
            .then((response) => {
            this.form = response.data;
            })
            .catch((error) => {
            console.error("Error loading member:", error);
            });
    }
}
</script>

<style scoped>

.back-btn {
  margin-left: 12px;
  background-color: #e0e0e0;
  color: #333;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.07);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  box-sizing: border-box;
}

.title {
  text-align: center;
  color: #343a40;
  font-size: 24px;
  margin-bottom: 4px;
}

.subtitle {
  text-align: center;
  color: #6c757d;
  font-size: 14px;
  margin-bottom: 24px;
}

.form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 12px;
  font-weight: 500;
  color: #495057;
}

.input {
  padding: 10px 14px;
  border: 1px solid #ced4da;
  box-sizing: border-box;
  background: #f8f9fa;
  font-size: 14px;
  margin-top: 4px;
  transition: border-color 0.3s ease;
  outline: none;
  width: 100%;
}

.input:focus {
  border-color: #d63384;
  background: #fff;
}

.form-actions {
  margin-top: 24px;
  text-align: right;
}

.submit-btn {
  background-color: #4a90e2;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #357ab8;
}

.input-label {
  margin-top: 20px;
  font-weight: 600;
  color: #212529;
  margin-bottom: 10px;
  display: block;
}

.role-group {
  margin-bottom: 24px;
  padding-top: 8px;
}

.radio-option {
  margin-bottom: 12px;
  border-bottom: 1px solid #dee2e6;
  padding-bottom: 8px;
}

.radio-label {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.radio-input {
  appearance: none;
  display: grid;
  place-items: center;
  border: 2px solid #4a90e2;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  margin-right: 12px;
  transition: border-color 0.2s ease;
}

.radio-input::before {
  content: "";
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #3b0ca3;
  transform: scale(0);
  transition: transform 0.2s ease-in-out;
}

.radio-input:checked {
  border-color: #339dd6;
  background-color: white;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio-text {
  font-size: 15px;
  color: #495057;
}

.dual-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 24px;
}

.delete-btn {
  background-color: transparent;
  color: #e03131;
  border: 1px solid #e03131;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.delete-btn:hover {
  background-color: #e03131;
  color: white;
}

.submit-btn {
  background-color: #4a90e2;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #357ab8;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.4), rgba(248, 243, 246, 0.6));
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.modal {
  background: #fff;
  padding: 24px 32px;
  border-radius: 16px;
  max-width: 400px;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.modal h3 {
  font-size: 20px;
  color: #070707;
  margin-bottom: 8px;
}

.modal p {
  font-size: 14px;
  color: #555;
  margin-bottom: 24px;
}

.modal-actions {
  display: flex;
  justify-content: space-between;
  gap: 12px;
}

.cancel-btn, .confirm-btn {
  flex: 1;
  padding: 10px;
  font-size: 14px;
  border-radius: 8px;
  cursor: pointer;
  border: none;
  transition: all 0.2s ease;
}

.cancel-btn {
  background-color: #f1f3f5;
  color: #495057;
}

.cancel-btn:hover {
  background-color: #e9ecef;
}

.confirm-btn {
  background-color: #e03131;
  color: white;
}

.confirm-btn:hover {
  background-color: #c2255c;
}


</style>
