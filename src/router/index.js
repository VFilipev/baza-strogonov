import { createRouter, createWebHistory } from 'vue-router'
import Booking from '../views/Booking.vue'
import MainPage from '../views/MainPage.vue'
import UslugiPage from '../views/UslugiPage.vue'
import HousePage from '../views/HousePage.vue'
import sandBox from '../components/sandBox.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main-page',
      component: MainPage
    },
    {
      path: '/booking',
      name: 'booking',
      component: Booking
    },
    {
      path: '/uslugi',
      name: 'uslugi',
      component: UslugiPage
    },
    {
      path: '/house',
      name: 'house',
      component: HousePage
    },
    {
      path: '/sandbox',
      name: 'sandbos',
      component: sandBox
    },
    // {
    //   path: '/about',
    //   name: 'about',      
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

export default router
