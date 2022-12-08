import Vue from 'vue';
import Router from 'vue-router';
import Game from './views/Game.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';

Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Game
    },
    {
      path: '/home',
      component: Game
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/register',
      component: Register
    },
    // {
    //   path: '/user',
    //   name: 'user',
    //   // lazy-loaded
    //   component: () => import('./views/BoardUser.vue')
    // }
  ]
});