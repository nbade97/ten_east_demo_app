<template>
    <div class="min-h-screen bg-gray-100 flex items-center justify-center">
      <div class="bg-white p-16 rounded-lg shadow-lg max-w-3xl w-full">
        <div class="mb-4">
          <h1 class="text-3xl font-semibold">How much would you like to invest in {{ projectName }}?</h1>
          <p class="text-gray-600">Please enter an amount in increments of $10,000.</p>
        </div>
        <form @submit.prevent="submitForm">
          <div class="mb-6">
            <label for="amount" class="block text-sm font-medium text-gray-700">
              AMOUNT
            </label>
            <div class="mt-1 relative rounded-md shadow-sm">
              <input type="text" id="amount" v-model="formattedAmount" @input="updateAmount" class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-12 sm:text-lg border-gray-300 rounded-md" placeholder="$100K Minimum Investment">
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                <!-- Optional icon or text -->
              </div>
            </div>
            <p v-if="errorMessage" class="text-red-500 mt-2">{{ errorMessage }}</p>
          </div>
          <div class="flex justify-end">
            <button type="submit" class="custom-button" @click="navigateToStepTwo" :disabled="errorMessage">
              Next
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      projectName: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        amount: '',
      }
    },
    computed: {
      formattedAmount: {
        get() {
          return this.amount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        },
        set(newValue) {
          this.amount = newValue.replace(/,/g, '');
        }
      },
      errorMessage() {
        const amount = parseInt(this.amount, 10);
        if (isNaN(amount) || amount < 100000 || amount % 10000 !== 0) {
          return 'Amount must be at least $100,000 and in increments of $10,000.';
        }
        return false;
      }
    },
    methods: {
      updateAmount(event) {
        this.formattedAmount = event.target.value;
      },
      navigateToStepTwo() {
        console.log(this.amount, this.projectName);
        if (!this.errorMessage) {
          this.$router.push({ 
            name: 'StepTwo',
            params: { 
              amount: this.amount,
              projectName: this.projectName
            }
          });
        }
      }
    }
  }
</script>
  
  <style scoped>
  .custom-button {
    background-color: #c78B58;
    color: white;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .custom-button:hover {
    background-color: #b07a4e;
  }
  
  .custom-button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.6);
  }
  
  .custom-button:disabled {
    background-color: #e0e0e0;
    cursor: not-allowed;
  }
  </style>