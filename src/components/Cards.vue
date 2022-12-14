<template>
  <n-scrollbar x-scrollable trigger="hover" style="width: 600px">
    <div style="white-space: nowrap; width: 1310px">
      <ul v-for="item in items.value" :key="item.id" style="position:relative;">
        <Card class="card"
              :target="item.target"
              :title="item.title"
              :img-url="item.url"
              :text="item.test"/>
<!--        <Card class="card"/>-->
<!--        <Card class="card"/>-->
<!--        <Card class="card"/>-->
<!--        <Card class="card"/>-->
<!--        <Card style="list-style: none;float: left;"/>-->
      </ul>
    </div>
  </n-scrollbar>
</template>

<script>
import Card from './Card'
import {reactive} from "vue";
import request from "@/utils/request";

export default {
  name: "Cards",
  components: {Card},

  setup() {
    // let items = [
    //   {id:0,target:'https://store.steampowered.com/app/2012840/Portal_with_RTX/',title:'Portal with RTX',imgUrl:'https://cdn.cloudflare.steamstatic.com/steam/apps/2012840/header.jpg?t=1670622268',text:'在这款面向所有 Portal™ 拥有者的免费 DLC 中，广受好评且屡获殊荣的 Portal™ 经过光线追踪重构，快来体验吧！开启 RTX，体验“传送门（Portal）”全新效果。'},
    //   {id:1,target:'https://store.steampowered.com/app/2012840/Portal_with_RTX/',title:'Portal with RTX',imgUrl:'https://cdn.cloudflare.steamstatic.com/steam/apps/2012840/header.jpg?t=1670622268',text:'在这款面向所有 Portal™ 拥有者的免费 DLC 中，广受好评且屡获殊荣的 Portal™ 经过光线追踪重构，快来体验吧！开启 RTX，体验“传送门（Portal）”全新效果。'},
    //   {id:2,target:'https://store.steampowered.com/app/2012840/Portal_with_RTX/',title:'Portal with RTX',imgUrl:'https://cdn.cloudflare.steamstatic.com/steam/apps/2012840/header.jpg?t=1670622268',text:'在这款面向所有 Portal™ 拥有者的免费 DLC 中，广受好评且屡获殊荣的 Portal™ 经过光线追踪重构，快来体验吧！开启 RTX，体验“传送门（Portal）”全新效果。'}
    // ]
    // 从后端获取数据
    let items = reactive([])
    const load = () => {
      request.post("/getNews/",JSON.stringify({})).then(res=>{
        items.value = res.data
        console.log(items.value)
      })
    }
    load()
    return {
      Card,
      items,
    }
  }
}



</script>

<style scoped>

.card {
  list-style: none;
  float: left;
  margin-right: 20px;
}

</style>