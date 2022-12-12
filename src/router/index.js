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

import DetailPage from "@/components/DetailPage";
import CountryPriceTable from "@/components/CountryPriceTable";
import Charts from "@/components/Charts";

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
        path: '/detail/:gameid',
        name: 'Detail',
        redirect: '/detail/:gameid/price',
        component: DetailPage,
        children: [
            {
                path: 'price',
                name: 'CountryPrice',
                component: CountryPriceTable
            },
            {
                path: 'graph',
                name: 'Chart',
                component: Charts
            },
            {
                path: 'screenshot',
                name: 'ScreenShot',
                //TODO
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

export default router