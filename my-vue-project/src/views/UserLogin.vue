<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-200">
    <div class="p-6 md:p-12 lg:w-1/3 bg-white shadow-lg rounded-lg">
      <div class="flex flex-col items-center">
        <img src="@/assets/ten_east_logo.png" alt="logo" class="mb-4 w-24">
        <h1 class="mb-6 text-2xl font-bold font-amiri">Sign In</h1>
        <form @submit.prevent="login" class="w-full max-w-sm">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
              Username
            </label>
            <input v-model="username" id="username" type="text" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
          </div>
          <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
              Password
            </label>
            <input v-model="password" id="password" type="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline">
          </div>
          <div class="flex items-center justify-between">
              <button type="submit" class="w-full custom-button">
              Sign In
            </button>
          </div>
        </form>
        <p class="mt-6 text-base" style="color: #C78B58;">
          <a href="#" style="color: #C78B58;">Forgot your password?</a>
        </p>
        <p class="text-base" style="color: black;">
          Don't have an account? <a href="#" style="color: #C78B58;">Request Access</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserLogin',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/auth/login/', {
          username: this.username,
          password: this.password
        });
        console.log('Login successful:', response.data);
        alert('Login success!');
        // Handle successful login, e.g., redirect to another page
      } catch (error) {
        console.error('Login failed:', error);
        alert('Login failed. Please try again.');
        // Handle login failure, e.g., show an error message
      }
    }
  }
};
</script>

<style scoped>
/* Optional: Add additional global styles in your tailwind.css file */
.custom-button {
  background-color: #c78B58;
  color: white; /* Keep the text color white */
  font-weight: bold; /* Corrected property */
  padding: 10px 20px; /* Adjust padding as needed */
  border-radius: 5px; /* Keep rounded corners */
  cursor: pointer; /* Change cursor to pointer */
  width: 100%; /* Full width */
}

.custom-button:hover {
  background-color: #b07a4e; /* Darken color on hover */
}

.custom-button:focus {
  outline: none; /* Remove outline */
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.6); /* Add shadow outline */
}
</style>