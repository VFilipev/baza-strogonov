import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
import axios from "axios"

import { setupCalendar } from 'v-calendar';
import 'swiper/css';

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken' 

const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(setupCalendar, {})
app.use(router)

app.mount('#app')

router.afterEach((to,from,next) => {
    window.scrollTo(0,0);
})