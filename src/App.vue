<template>
  <Header></Header>
  <TestStore></TestStore>
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

import Header from "@/components/Header";
import TestStore from "@/components/testStore";

export default {
  name: 'App',
  components: {
    TestStore,
    Header,
  }
}
</script>

<style>
</style>
