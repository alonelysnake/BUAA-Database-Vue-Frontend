<template>
  <n-config-provider :locale="zhCN" :date-locale="dateZhCN">
    <Header></Header>
    <router-view></router-view>
  </n-config-provider>
<!--  <n-dialog-provider>-->
<!--    <n-message-provider>-->
<!--      <GameGoods></GameGoods>-->
<!--    </n-message-provider>-->
<!--  </n-dialog-provider>-->
<!--<FavoriteGame></FavoriteGame>-->

<!--  <Header></Header>-->
<!--  <filter-page></filter-page>-->
</template>

<script>
import { NConfigProvider } from 'naive-ui'
import { zhCN, dateZhCN } from 'naive-ui'
import Header from "@/components/Header";
import store from "./store"
import GameGoods from "@/components/GameGoods";
import FavoriteGame from "@/components/FavoriteGame";

export default {
  name: 'App',
  components: {
    FavoriteGame,
    GameGoods,
    Header,
    NConfigProvider,
  },
  created() {
    //在页面加载时读取sessionStorage里的状态信息
    if (sessionStorage.getItem("store")) {
      store.replaceState(Object.assign({}, store.state, JSON.parse(sessionStorage.getItem("store"))))
    }

    //在页面刷新时将vuex里的信息保存到sessionStorage里
    window.addEventListener("beforeunload", () => {
      sessionStorage.setItem("store", JSON.stringify(store.state))
    })
  },
  setup() {
    return {
      zhCN,
      dateZhCN
    }
  }
}
</script>

<style>
</style>
