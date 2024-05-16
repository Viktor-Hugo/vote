import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import MainView from '@/views/MainView.vue'
import ResultView from '@/views/ResultView.vue'
import { useAccountStore } from '@/stores/accounts'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/result',
      name: 'result',
      component: ResultView
    },

  ]
})

router.beforeEach((to, from) => {
  const accountStore = useAccountStore()
  console.log(to.name)
  if (!accountStore.isAuthenticated && to.name !== 'login') {
    return { name: 'login' }
  }
})

export default router
