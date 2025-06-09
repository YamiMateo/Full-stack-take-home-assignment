// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import ListPage from '../views/ListPage.vue'
import AddPage from '../views/AddPage.vue'
import EditPage from '../views/EditPage.vue'
import DeletePage from '../views/DeletePage.vue'

const routes = [
  { path: '/', component: ListPage },
  { path: '/add', component: AddPage },
  { path: '/edit/:id', component: EditPage, props: true },
  { path: '/delete', component: DeletePage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
