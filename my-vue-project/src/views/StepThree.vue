<template>
    <div class="bg-gray-100 min-h-screen flex items-center justify-center p-6">
      <div class="bg-white rounded-lg shadow-lg max-w-md w-full p-8">
        <header>
          <h1 class="text-xl font-semibold">Allocation Request Summary</h1>
          <p class="text-gray-600">Please review the information below.</p>
        </header>
        <div class="mt-6">
          <div class="mb-4">
            <h2 class="font-medium text-gray-900">Selected Investment Profile</h2>
            <p>Demo User</p>
          </div>
          <div class="mb-4">
            <h2 class="font-medium text-gray-900">Selected Offering</h2>
          <p>{{this.$route.query.projectName}}</p>
        </div>
        <div class="mb-4">
          <h2 class="font-medium text-gray-900">Amount Requested</h2>
          <p>{{formattedAmount}}</p>
        </div>
      </div>
      <div class="flex justify-center mt-8">
        <button type="submit" class="custom-button" @click="submitRequest">
          Submit
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RequestSummary',
  computed: {
    formattedAmount() {
      const amount = this.$route.query.amount;
      if (!amount) return '';
      return parseFloat(amount).toLocaleString();
    }
  },
  methods: {
    async submitRequest() {
      try {
        let user = "Demo User";
        let amount = this.$route.query.amount;
        let project_name = this.$route.query.projectName;
        let current_time = new Date().toISOString(); // Get the current time in ISO format

        console.log("Submitting request...");

        const response = await axios.post('http://localhost:8000/auth/add_contribution/', {
          user: user,
          amount: amount,
          project_name: project_name,
          current_time: current_time 
        });

        console.log('Request submitted successfully:', response.data);
        alert('Request submitted successfully!');
      } catch (error) {
        console.error('Error submitting request:', error);
        alert('Error submitting request. Please try again.');
      }
    }
  },
  
}
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
  /* width: 100%; */
}

.custom-button:hover {
  background-color: #b07a4e; /* Darken color on hover */
}

.custom-button:focus {
  outline: none; /* Remove outline */
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.6); /* Add shadow outline */
}
</style>
  