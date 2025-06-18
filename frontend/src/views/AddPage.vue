<template>
  <div class="container">
    <h2 class="title">Add a team member</h2>
    <p class="subtitle">Set email, location and role.</p>

    <form @submit.prevent="submitForm" class="form">

      <label class="input-label">Info:</label>

      <label>Name:</label>
      <input v-model="form.first_name" required class="input" />

      <label>Last Name:</label>
      <input v-model="form.last_name" required class="input" />

      <label>Email:</label>
      <input v-model="form.email" type="email" required :class="['input', emailError ? 'input-error' : '']" />

      <label>Phone number:</label>
      <input v-model="form.phone" required class="input" />

      <label class="input-label">Role:</label>
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

      <div class="form-actions">
        <button type="submit" class="submit-btn">Save</button>
        <button type="button" class="back-btn" @click="$router.push('/')">Back to list</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import confetti from 'canvas-confetti'
import { useToast } from 'vue-toastification'
import 'vue-toastification/dist/index.css'

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
        {
          value: 'regular',
          label: "Regular - Can’t delete members"
        },
        {
          value: 'admin',
          label: "Admin - Can delete members"
        }
      ],
      phoneError: false,
      emailError: false,
    }
  },
  methods: {
    submitForm() {
        const toast = useToast()

        if (!/^\d{10}$/.test(this.form.phone)) {
            this.phoneError = "invalid";

            toast.warning('Please enter a valid 10-digit phone number.', {
                timeout: 3000,
                position: 'top-center',
                hideProgressBar: true
            });

            setTimeout(() => {
            this.phoneError = false;
            }, 3000);
            return;
        }

        axios
            .post('http://localhost:8000/api/team-members/', this.form)
            .then(() => {
            this.launchConfetti();
            toast.success('Member added successfully! 🎉', {
                timeout: 3000,
                position: 'top-center',
                hideProgressBar: true
            })
            setTimeout(() => {
                this.$router.push('/');
            }, 1000);
            })
            .catch(error => {
            if (error.response && error.response.data) {
                const data = error.response.data;
                this.phoneError = data.phone ? "duplicate" : false;
                this.emailError = !!data.email;

                let message = "";

                switch (true) {
                case this.phoneError === "duplicate" && this.emailError:
                    message = 'This phone number and email have already been registered.';
                    break;
                case this.phoneError === "duplicate":
                    message = 'This phone number has already been registered.';
                    break;
                case this.emailError:
                    message = 'This email has already been registered.';
                    break;
                }

                if (message) {
                toast.warning(message, {
                    timeout: 3000,
                    position: 'top-center',
                    hideProgressBar: true
                });
                }

                setTimeout(() => {
                this.phoneError = false;
                this.emailError = false;
                }, 3000);
            }

            console.error('An error occurred while adding the member:', error);
            });

    },
    launchConfetti() {
      confetti({
        particleCount: 150,
        spread: 70,
        origin: { y: 0.6 }
      })
    }
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

.subtitle {
  text-align: center;
  color: #6c757d;
  font-size: 14px;
  margin-bottom: 24px;
}

.input-label {
  margin-top: 20px;
  font-weight: 600;
  color: #212529;
  margin-bottom: 10px;
  display: block;
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

.error-message {
  color: #e03131;
  background: #fff5f5;
  padding: 8px 12px;
  border-radius: 6px;
  margin-top: 16px;
  font-size: 14px;
  text-align: center;
  border: 1px solid #ffa8a8;
}

</style>