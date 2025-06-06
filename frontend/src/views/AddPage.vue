<template>
  <div>
    <h2>Agregar miembro</h2>
    <form @submit.prevent="submitForm">
      <label>Nombre:</label>
      <input v-model="form.first_name" required />

      <label>Apellido:</label>
      <input v-model="form.last_name" required />

      <label>Email:</label>
      <input v-model="form.email" type="email" required />

      <label>Teléfono:</label>
      <input v-model="form.phone" required />

      <label>Rol:</label>
      <select v-model="form.role">
        <option value="regular">Regular - Can’t delete members</option>
        <option value="admin">Admin - Can delete members</option>
      </select>

      <br /><br />
      <button type="submit">Guardar</button>
    </form>
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
      }
    }
  },
  methods: {
    submitForm() {
      axios
        .post('http://localhost:8000/api/team-members/', this.form)
        .then(() => {
          this.$router.push('/')
        })
        .catch(error => {
          console.error('Error al agregar miembro:', error)
        })
    }
  }
}
</script>
