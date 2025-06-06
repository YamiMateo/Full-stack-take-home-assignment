<template>
  <div>
    <h2>Miembros del equipo ({{ teamMembers.length }})</h2>
    <router-link to="/add">
      <button>➕ Agregar miembro</button>
    </router-link>
    <ul>
      <li v-for="member in teamMembers" :key="member.id">
        {{ member.first_name }} {{ member.last_name }} — <strong>{{ member.role }}</strong>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      teamMembers: []
    }
  },
  created() {
    axios
      .get('http://localhost:8000/api/team-members/')
      .then(response => {
        this.teamMembers = response.data
      })
      .catch(error => {
        console.error("Error al obtener miembros:", error)
      })
  }
}
</script>
