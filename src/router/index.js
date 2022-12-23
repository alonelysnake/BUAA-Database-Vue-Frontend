import {createRouter, createWebHistory} from 'vue-router'

import Home from "@/view/Home";
import UserPage from "@/view/User";
import UserInfo from "@/components/UserInfo";
import Buyer from "@/components/Buyer";
import SellerGoods from "@/components/SellerGoods";
import SellerOrder from "@/components/SellerOrder";

import RegisterLoginPage from "@/view/RegisterLoginPage";
import Register from "@/components/Register";
import Login from "@/components/Login";

import HeatPage from "@/view/HeatPage";
import FilterPage from "@/view/FilterPage";

import DetailPage from "@/view/DetailPage";
import CountryPriceTable from "@/components/CountryPriceTable";
import Charts from "@/components/Charts";
import ScreenShot from "@/components/ScreenShot";
import Comment from "@/components/Comment"

import store from "@/store";
import GameGoods from "@/components/GameGoods";
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
        path: '/detail/:gameid',
        name: 'Detail',
        redirect: '/detail/:gameid/price',
        component: DetailPage,
        children: [
            {
                path: '/detail/:gameid/price',
                name: 'CountryPrice',
                component: CountryPriceTable
            },
            {
                path: '/detail/:gameid/graph',
                name: 'Chart',
                component: Charts
            },
            {
                path: '/detail/:gameid/comment',
                name: 'Commment',
                component: Comment,
            },
            {
                path: '/detail/:gameid/goods',
                name: 'Good',
                component: GameGoods,
            },
            {
                path: '/detail/:gameid/screenshot',
                name: 'ScreenShot',
                component: ScreenShot,
            },
        ]
    },
    {
        path: '/heat',
        name: 'Heat',
        component: HeatPage,
    },
    {
        path: '/filter',
        name: 'Filter',
        component: FilterPage,
    },
    {
        path: '/logReg',
        name: 'LogReg',
        redirect: '/logReg/login',
        component: RegisterLoginPage,
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