import {createRouter, createWebHistory} from "vue-router";
import Register from "@/components/Register";
import Login from "@/components/Login";

const routes = [
    //TODO 考虑登录界面与主界面的父子关系
    {
        path: '/Register',
        component: Register
    },
    {
        path: '/Login',
        component: Login
    },
    {
        path: '/',
        component: Login,
        redirect: '/Login'//重定向，设置默认路由
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router