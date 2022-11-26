import { createApp } from 'vue'
import App from './App.vue'

import naive from 'naive-ui'
// import * as echarts from 'echarts'

import '@/assets/css/global.css'

const app = createApp(App)
app.use(naive)
// app.use(echarts)
app.mount('#app')
