<template>
  <n-dialog-provider>
    <n-message-provider>
      <n-config-provider :locale="zhCN" :date-locale="dateZhCN">
        <Header></Header>
        <router-view></router-view>
      </n-config-provider>
    </n-message-provider>
  </n-dialog-provider>
</template>

<script>
import { NConfigProvider } from 'naive-ui'
import { zhCN, dateZhCN } from 'naive-ui'
import {onBeforeMount} from "vue";
import Header from "@/components/Header";
import store from "./store"

export default {
  name: 'App',
  components: {
    Header,
    NConfigProvider,
  },
  setup() {
    onBeforeMount(()=>{
      //在页面加载时读取sessionStorage里的状态信息
      if (sessionStorage.getItem("store")) {
        //console.log('加载')
        //console.log(store.state)
        store.replaceState(Object.assign({}, store.state, JSON.parse(sessionStorage.getItem("store"))))
        //console.log(store.state)
      }

      //在页面刷新时将vuex里的信息保存到sessionStorage里
      window.addEventListener("beforeunload", () => {
        sessionStorage.setItem("store", JSON.stringify(store.state))
      })
    })
    return {
      zhCN,
      dateZhCN
    }
  }
}
</script>

<style>
</style>
