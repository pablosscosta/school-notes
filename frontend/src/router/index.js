import { createRouter, createWebHistory } from 'vue-router'

//layouts
import PublicLayout from '../layouts/PublicLayout.vue'
import DashboardLayout from '../layouts/DashboardLayout.vue'

//publics
import HomeView from '../views/public/HomeView.vue'
import LoginView from '../views/public/LoginView.vue'
import RegisterView from '../views/public/RegisterView.vue'
import AboutView from '../views/public/AboutView.vue'

//dashboards
import DashboardView from '../views/dashboard/DashboardView.vue'


const routes = [
  {
    path: '/',
    component: PublicLayout,
    children: [
      { path: '', name: 'home', component: HomeView },
      { path: 'login', name: 'login', component: LoginView },
      { path: 'register', name: 'register', component: RegisterView },
      { path: 'about', name: 'about', component: AboutView},
    ]
  },
  {
    path: '/dashboard',
    component: DashboardLayout,
    children: [
      { path: '', name: 'dashboard-home', component: DashboardView},
      // outras rotas do dashboard aqui
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
