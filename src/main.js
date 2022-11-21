import { createApp } from 'vue'
import App from './App.vue'

import naive from 'naive-ui'

import '@/assets/css/global.css'

const app = createApp(App)
app.use(naive)
app.mount('#app')
