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
      path: '/house/:slug',
      name: 'house',
      component: () => import( '../views/HousePage.vue')
    },    
    {
      path:'/booking/confirm',        
      name: 'BookingConfirm',
      component: () => import( '../views/BookingConfirm.vue')
    },    
    {
      path: '/admin-vue',
      name: 'admin',
      component: () => import('../views/AdminView.vue'),
      children:[
        {
          path: '',
          redirect: '/admin-vue/order'
        },
        {
          path: 'order',
          name: 'order',
          component: () => import('../views/OrderView.vue')
        },
        {   
          path: '/sauna',
          name: 'sauna',
          component: () => import('../views/SaunaView.vue')
        },
        {
          path: '/plan',
          name: 'plan',
          component: () => import('../views/PlanView.vue')
        },
        {
          path: '/registry',
          name: 'registry',
          component: () => import('../views/RegistryView.vue')
        },
      ]
    },    
  ]
})

export default router
