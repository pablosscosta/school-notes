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
import StudentsView from '@/views/dashboard/StudentsView.vue'
import ClassroomsView from '@/views/dashboard/ClassroomsView.vue'
import SubjectsView from '@/views/dashboard/SubjectsView.vue'


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
    meta: { requiresAuth: true },
    children: [
      { path: '', name: 'dashboard-home', component: DashboardView},
      { path: 'students', component: StudentsView },
      { path: 'classrooms', component: ClassroomsView },
      { path: 'subjects', component: SubjectsView }
      // outras rotas do dashboard aqui
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('accessToken');

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'login' });
  } else if ((to.path === '/login' || to.path === '/register') && isAuthenticated){
    next('/dashboard');
  } else {
    next();
  }
})

export default router
