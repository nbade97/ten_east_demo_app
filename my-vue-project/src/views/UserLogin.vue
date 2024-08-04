<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-200">
    <div class="p-6 md:p-12 lg:w-1/3 bg-white shadow-lg rounded-lg">
      <div class="flex flex-col items-center">
        <img src="@/assets/ten_east_logo.png" alt="logo" class="mb-4 w-24">
        <h1 class="mb-6 text-2xl font-bold">Sign In</h1>
        <form class="w-full max-w-sm">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
              Email
            </label>
            <input id="email" type="email" placeholder="Enter your email" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
          </div>
          <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
              Password
            </label>
            <input id="password" type="password" placeholder="Enter your password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline">
          </div>
          <div class="flex items-center justify-between">
            <button type="submit" class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Sign In
            </button>
          </div>
        </form>
        <p class="text-blue-500 mt-6 text-xs">
          Forgot your password? <a href="#" class="underline">Click here</a>
        </p>
        <p class="text-blue-500 text-xs">
          Don't have an account? <a href="#" class="underline">Request Access</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserLogin'
};
</script>

<style scoped>
/* Optional: Add additional global styles in your tailwind.css file */
</style>
