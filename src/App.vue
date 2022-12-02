<template>
  <n-config-provider :locale="zhCN" :date-locale="dateZhCN">
    <Header></Header>
    <router-view></router-view>
  </n-config-provider>

<!--  <div style="display: block; height: 100%">-->
<!--    <div v-if="headerVisiable" class="header-container">-->
<!--      <Header-->
<!--          :head_index="this.headerIndex"-->
<!--      ></Header>-->
<!--    </div>-->
<!--    <div v-if="headerVisiable" style="height: 70px; background-color: rgb(243, 243, 244)"></div>-->
<!--    <router-view :key="$route.fullPath"/>-->
<!--  </div>-->
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
