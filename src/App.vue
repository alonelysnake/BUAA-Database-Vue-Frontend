<template>
  <n-config-provider :locale="zhCN" :date-locale="dateZhCN">
    <Header></Header>
    <router-view></router-view>
  </n-config-provider>
  
</template>

<script>
import { NConfigProvider } from 'naive-ui'
import { zhCN, dateZhCN } from 'naive-ui'
import Header from "@/components/Header";
export default {
  name: 'App',
  components: {
    Header,
    NConfigProvider,
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
