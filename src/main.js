import { createApp } from 'vue'
import App from './App.vue'
import naive from 'naive-ui'
import router from './router'
import store from './store'

import '@/assets/css/global.css'

const app = createApp(App)
app.use(store).use(naive).mount('#app')
