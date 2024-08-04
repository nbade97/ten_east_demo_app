import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/views/Login';

Vue.use(Router);

export default new Router({
  mode: 'history',  // Enables cleaner URLs without the hash
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
});
