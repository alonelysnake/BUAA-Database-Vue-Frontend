import {createRouter, createWebHistory} from 'vue-router'

import Home from "@/view/Home";
import UserPage from "@/view/User";
import UserInfo from "@/components/UserInfo";
import Buyer from "@/components/Buyer";
import SellerGoods from "@/components/SellerGoods";
import SellerOrder from "@/components/SellerOrder";
import Register from "@/components/Register";
import Login from "@/components/Login";
import store from "@/store";
const routes = [
    {
        path: '/',
        redirect: '/home'
    },
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    {
        path: '/game/:gameId',
        name: 'Game',
        component: import('@/view/DetailPage'),
    },
    {
      path: '/user_v/:username',
        component: UserPage,
        children: [
            {
                path: '/user_v/:username/info',
                name: 'Info_v',
                component: UserInfo,
            },
            {
                path: '/user_v/:username/sellerGoods',
                name: 'SellerGoods_v',
                component: SellerGoods,
            },
        ]
    },
    {
        path: '/user/:username',
        name: 'User',
        component: UserPage,
        meta: {
            requiresLoggedIn:true
        },
        children: [
            {
                path: '/user/:username/info',
                name: 'Info',
                component: UserInfo,
            },
            {
                path: '/user/:username/buyer',
                name: 'Buyer',
                component: Buyer,
            },
            {
                path: '/user/:username/sellerGoods',
                name: 'SellerGoods',
                component: SellerGoods,
            },
            {
                path: '/user/:username/sellerOrder',
                name: 'SellerOrder',
                component: SellerOrder,
            },
            {
                path: '/user/:username/favor',
                name: 'Favor',
                component: import('@/components/FavoriteGame'),
            }
        ]
    },
    {
        path: '/logReg',
        name: 'LogReg',
        redirect: '/logReg/login',
        component: () => import('@/view/RegisterLoginPage'),
        children: [
            {
                path: 'register',
                name: 'register',
                component: Register
            },
            {
                path: 'login',
                name: 'login',
                component: Login
            },
        ]
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

// 全局守卫
router.beforeEach((to, from, next) => {
    if (to.meta.requiresLoggedIn && !store.state.loggedIn) {
        next({
            path: '/logReg/login',
            query: {
                redirect: to.path
            }
        })
    } else {
        next()
    }
})

export default router