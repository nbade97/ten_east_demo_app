<template>
  <div class="bg-gray-100 min-h-screen flex items-center justify-center p-6">
    <div class="max-w-4xl w-full bg-white rounded-lg shadow-md p-8">
      <header class="mb-6">
        <h1 class="text-2xl font-semibold">Acknowledgements</h1>
        <p>Please acknowledge and agree to the following statements to continue.</p>
      </header>
      <form @submit.prevent="submitForm">
        <div class="space-y-4">
          <div v-for="(item, index) in statements" :key="index">
            <label class="flex items-start">
              <input type="checkbox" v-model="item.checked" class="mt-1 accent-blue-500">
              <span class="ml-2 text-sm text-gray-700">{{ item.text }}</span>
            </label>
          </div>
        </div>
        <div class="flex justify-end mt-8">
          <button type="submit" class="custom-button" @click="navigateToStepThree" :disabled="!allAcknowledged">
            Next
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  // props: {
  //   amount: {
  //     type: String,
  //     required: true
  //   },
  //   projectName: {
  //     type: String,
  //     required: true
  //   }
  // },
  data() {
    return {
      amount: this.$route.query.amount,
      projectName: this.$route.query.projectName,
      statements: [
        { text: 'I acknowledge and agree that allocation requests are accepted or rejected, in whole or in part, at 10 East’s discretion, and that members are not accepted into any 10 East investment unless and until completed and signed subscription documentation is received and countersigned by 10 East.', checked: false },
        { text: 'I acknowledge and agree that 10 East is permitted to, and expects to, call capital in amounts exceeding my approved allocation amount (which will be the commitment amount included on my completed subscription agreement), as set forth in the 10 East investment documentation, including for fees and expenses at the 10 East investing entity level.', checked: false },
        { text: 'I acknowledge and agree that I remain subject to 10 East’s Terms of Use, Non-Disclosure Agreement and Privacy Policy.', checked: false },
        { text: 'Notwithstanding the above, I acknowledge and agree to be bound by any affirmation or assent that I transmit to 10 East by computer or other electronic device, including, but not limited to, when I click on an “I Agree,” “I Consent,” or other similarly worded button, or when I provide an electronic signature, and it will be the equivalent of my handwritten signature on an agreement. I acknowledge and agree that 10 East may send me electronic copies of any and all communication associated with my investment(s).', checked: false },
        { text: 'I acknowledge and agree that I have read and understand the investment memorandum and other legal documentation applicable to this investment and have had the opportunity to ask 10 East personnel any questions regarding the same.', checked: false }
      ]
    };
  },
  computed: {
    allAcknowledged() {
      return this.statements.every(item => item.checked);
    }
  },
  methods: {
    submitForm() {
      if (this.allAcknowledged) {
        console.log("All statements have been acknowledged.");
        // Proceed with the form submission logic
      } else {
        alert("Please acknowledge all the statements to continue.");
      }
    },
    navigateToStepThree() {
      if (this.allAcknowledged) {
        console.log(this.amount, this.projectName);
        this.$router.push({ 
          name: 'StepThree',
          query: { 
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