import { createApp } from 'vue'
import App from './App.vue'

import naive from 'naive-ui'
import element from 'element-plus'
import router from "./router";
import store from "./store/index";

import '@/assets/css/global.css'

import router from "@/router";

const app = createApp(App)
app.use(store)
app.use(naive)
app.use(element)
app.use(router)
app.mount('#app')
