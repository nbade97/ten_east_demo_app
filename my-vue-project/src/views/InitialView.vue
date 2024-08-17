<template>
    <div class="background">
      <!-- Toolbar -->
      <div class="bg-gray-800 text-white p-4">
        
        <div class="max-w-screen-lg mx-auto flex justify-between items-center">
          <div class="flex space-x-4">
            <button class="text-white hover:text-gray-300">Offerings</button>
            <button class="text-white hover:text-gray-300">Investment Process</button>
            <button class="text-white hover:text-gray-300">Community</button>
            <button class="text-white hover:text-gray-300">Insights</button>
            <button class="text-white hover:text-gray-300">Our Story</button>
          </div>
          <button class="text-white hover:text-gray-300">
            <i class="fas fa-user-circle text-xl"></i> <!-- Assuming Font Awesome is used -->
          </button>
        </div>
      </div>
  
      <!-- Main Content -->
      <div class="bg-gray-100 max-w-screen-lg mx-auto py-6">
        <div class="mt-4 bg-white shadow rounded-lg p-4">
          <div class="flex justify-between items-center border-b pb-4">
            <h3 class="text-lg font-semibold">Project Alpha</h3>
            <span class="px-2 py-1 bg-gray-200 text-sm rounded">PRIVATE EQUITY</span>
          </div>
          <div class="pt-4">
            <p>Preferred equity investment in a vertically integrated data-center owner and operator. This opportunity provides derivative AI infrastructure exposure to a business with strong customers including Google, Amazon, and Meta. Entry point reflects a ~75% discount to comparable businesses based on precedent industry transactions.</p>
            <div class="grid grid-cols-2 gap-4 mt-4">
              <div>
                <div><strong>Target Net IRR</strong></div>
                <div>34.8%</div>
              </div>
              <div>
                <div><strong>Target Net MOIC</strong></div>
                <div>2.0x</div>
              </div>
              <div>
                <div><strong>Estimated Term</strong></div>
                <div>3-5 Years</div>
              </div>
              <div>
                <div><strong>Minimum Investment</strong></div>
                <div>$100K</div>
              </div>
            </div>
            <footer class="flex justify-end mt-4">
              <button class="mr-2 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">View Details</button>
              <button class="custom-button" @click="navigateToStepOne('Project Alpha')" >Request Allocation</button>
            </footer>
          </div>
        </div>
      </div>

      <div class="bg-gray-100 max-w-screen-lg mx-auto py-6">
        <div class="mt-4 bg-white shadow rounded-lg p-4">
          <div class="flex justify-between items-center border-b pb-4">
            <h3 class="text-lg font-semibold">Project Beta</h3>
            <span class="px-2 py-1 bg-red-200 text-sm rounded">REAL ESTATE</span>
          </div>
          <div class="pt-4">
            <p>Preferred equity investment in a vertically integrated data-center owner and operator. This opportunity provides derivative AI infrastructure exposure to a business with strong customers including Google, Amazon, and Meta. Entry point reflects a ~75% discount to comparable businesses based on precedent industry transactions.</p>
            <div class="grid grid-cols-2 gap-4 mt-4">
              <div>
                <div><strong>Target Net IRR</strong></div>
                <div>34.8%</div>
              </div>
              <div>
                <div><strong>Target Net MOIC</strong></div>
                <div>2.0x</div>
              </div>
              <div>
                <div><strong>Estimated Term</strong></div>
                <div>5-8 Years</div>
              </div>
              <div>
                <div><strong>Minimum Investment</strong></div>
                <div>$100K</div>
              </div>
            </div>
            <footer class="flex justify-end mt-4">
              <button class="mr-2 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">View Details</button>
              <button class="custom-button" @click="navigateToStepOne('Project Beta')" >Request Allocation</button>
            </footer>
          </div>
        </div>
      </div>

      <!--Another Mock Project-->
      <div class="bg-gray-100 max-w-screen-lg mx-auto py-6">
        <div class="mt-4 bg-white shadow rounded-lg p-4">
          <div class="flex justify-between items-center border-b pb-4">
            <h3 class="text-lg font-semibold">Project Gamma</h3>
            <span class="px-2 py-1 bg-red-200 text-sm rounded">REAL ESTATE</span>
          </div>
          <div class="pt-4">
            <p>This investment involves a preferred equity position in a premium mixed-use development located in a rapidly growing urban corridor. The project is spearheaded by an experienced developer with a track record of successful large-scale projects. The development will include residential units, commercial spaces, and lifestyle amenities, catering to the rising demand for integrated living environments in metropolitan areas.</p>
            <div class="grid grid-cols-2 gap-4 mt-4">
              <div>
                <div><strong>Target Net IRR</strong></div>
                <div>32.3%</div>
              </div>
              <div>
                <div><strong>Target Net MOIC</strong></div>
                <div>2.0x</div>
              </div>
              <div>
                <div><strong>Estimated Term</strong></div>
                <div>2-3 Years</div>
              </div>
              <div>
                <div><strong>Minimum Investment</strong></div>
                <div>$100K</div>
              </div>
            </div>
            <footer class="flex justify-end mt-4">
              <button class="mr-2 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">View Details</button>
              <button class="custom-button" @click="navigateToStepOne('Project Gamma')" >Request Allocation</button>
            </footer>
          </div>
        </div>
      </div>

    </div>
  </template>
  
  <script>
  export default {
    name: 'ProjectSynapse',
    methods: {
    navigateToStepOne(projectName) {
        console.log('Navigating to StepOne with project:', projectName);
        this.$router.push({ name: 'StepOne', query: {id: projectName} });
    }
  }
  }
  </script>
  
  <style scoped>
  /* Add any specific styling here */
  .custom-button {
  background-color: #c78B58;
  color: white; /* Keep the text color white */
  font-weight: bold; /* Corrected property */
  padding: 10px 20px; /* Adjust padding as needed */
  border-radius: 5px; /* Keep rounded corners */
  cursor: pointer; /* Change cursor to pointer */
  /* width: 100%; Full width */
}

.custom-button:hover {
  background-color: #b07a4e; /* Darken color on hover */
}

.custom-button:focus {
  outline: none; /* Remove outline */
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.6); /* Add shadow outline */
}

.background {
    background-color: #fbfbfb;
    min-height: 100vh;
}


  </style>
  