import {createRouter, createWebHistory} from 'vue-router'

import Home from "@/view/Home";
import User from "@/view/User";
import UserInfo from "@/components/UserInfo";
import Buyer from "@/components/Buyer";
import SellerGoods from "@/components/SellerGoods";
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
        path: '/user/:username/',
        name: 'User',
        component: User,
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

        ]
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router