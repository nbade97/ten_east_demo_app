import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from '@/views/UserLogin.vue';
import InitialView from '@/views/InitialView.vue';
import StepOne from '@/views/StepOne.vue';
import StepTwo from '@/views/StepTwo.vue';
import StepThree from '@/views/StepThree.vue';
import store from '../store';

console.log('Starting application setup...');

const routes = [
  {
    path: '/',
    name: 'UserLogin',
    component: UserLogin
  },
  {
    path: '/initial',
    name: 'InitialView',
    component: InitialView
  },
  {
    path: '/step-one',
    name: 'StepOne',
    component: StepOne
  },
  {
    path: '/step-two',
    name: 'StepTwo',
    component: StepTwo
  },
  {
    path: '/step-three',
    name: 'StepThree',
    component: StepThree
  },
];

console.log('Routes defined:', routes);

const router = createRouter({
  history: createWebHistory(),
  routes
});

console.log('Router created:', router);

const app = createApp({});
console.log('Vue app instance created:', app);

app.use(router);
app.use(store);
console.log('Router and store added to the app.');

app.mount('#app');
console.log('App mounted to #app element.');

export default router;