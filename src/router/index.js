import {createRouter, createWebHistory} from 'vue-router'

import Home from "@/view/Home";
import UserPage from "@/view/User";
import UserInfo from "@/components/UserInfo";
import Buyer from "@/components/Buyer";
import SellerGoods from "@/components/SellerGoods";
import SellerOrder from "@/components/SellerOrder";
import Register from "@/components/Register";
import Login from "@/components/Login";
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
        path: '/user/:username',
        name: 'User',
        component: UserPage,
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
            }
        ]
    },
    {
        path: '/logReg',
        name: 'LogReg',
        component: () => import('@/view/RegisterLoginPage')
    },
    {
        path: '/register',
        component: Register
    },
    {
        path: '/login',
        component: Login
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router