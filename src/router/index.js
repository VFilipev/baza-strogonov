import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        selector: to.hash,
        behavior: 'smooth',
      }
    }
  },
  routes: [
    {
      path: '/',
      name: 'main-page',
      component: () => import( '../views/MainPage.vue')
    },
    {
      path: '/booking',
      name: 'booking',
      component: () => import( '../views/Booking.vue'),      
    },
    {
      path: '/uslugi',
      name: 'uslugi',
      component: () => import( '../views/UslugiPage.vue')
    },
    {
      path: '/house',
      name: 'house',
      component: () => import( '../views/HousePage.vue')
    },    
    {
      path:'/booking/confirm',        
      name: 'BookingConfirm',
      component: () => import( '../views/BookingConfirm.vue')
    },    
  ]
})

export default router
