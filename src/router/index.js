import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const router = createRouter ({
  history: createWebHistory(),
  routes: [
    {path: '/', name: 'home', component: Home},
    {path: '/education', component: ()=> import('../views/Education.vue')},
    {path: '/projects', component: ()=> import('../views/Projects.vue')},
    {path: '/gallery', component: ()=> import('../views/Gallery.vue')},
    {path: '/reflection', component: ()=> import('../views/Reflection.vue')},
    {path: '/contact', component: ()=> import('../views/Contact.vue')},
  ]
})

export default router;