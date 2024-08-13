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
          <p>Project A</p>
        </div>
        <div class="mb-4">
          <h2 class="font-medium text-gray-900">Amount Requested</h2>
          <p>100,000</p>
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
export default {
  name: 'RequestSummary',
  props: {
    amount: {
      type: String,
      required: true
    },
    projectName: {
      type: String,
      required: true
    }
  },
  methods: {
    submitRequest() {
      // Here you would handle the form submission
      console.log("Submitting request...");
      alert('Request submitted!');
    }
  }
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
  