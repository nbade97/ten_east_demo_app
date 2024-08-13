import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index'; // Import the router
import './assets/tailwind.css';

const app = createApp(App);

app.use(router); // Use the router

app.mount('#app');
