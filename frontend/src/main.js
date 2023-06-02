import './index.css';
import { createApp } from 'vue';
import {createRouter, createWebHashHistory} from 'vue-router';

import App from './App.vue';

import Login from './views/Login.vue';
import Landing from './views/Landing.vue';
import Dashboard from './views/Dashboard.vue';

// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
    { path: '/', component: Dashboard },
    { path: '/landing', component: Landing },
    { path: '/login', component: Login },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes: routes,
})

createApp(App)
.use(router)
.mount('#app')