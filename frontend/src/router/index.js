// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import ListPage from '../views/ListPage.vue'
import AddPage from '../views/AddPage.vue'

const routes = [
  { path: '/', component: ListPage },
  { path: '/add', component: AddPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
