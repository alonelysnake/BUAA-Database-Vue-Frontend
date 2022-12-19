<template>
  <div class="screenshot">
    <n-grid :cols="2">
      <n-gi v-for="img in imgs" :key="img.id" class="img-container">
        <n-image width="700" :src="img.addr"/>
      </n-gi>
    </n-grid>
  </div>
</template>

<script>
import {useRouter} from "vue-router";
import request from "@/utils/request";

export default {
  name: "ScreenShot",

  setup() {
    const router = useRouter();
    const gameId = parseInt(router.currentRoute.value.params.gameid);
    //TODO 根据游戏id获取所有图片
    let imgs = [];
    request.post("/getScreenShot/", JSON.stringify({"id": gameId})).then(res => {
      imgs = res.data;
    });
    imgs = [
      {id: 0, addr: "https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493"},
      {id: 0, addr: "https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493"},
      {id: 0, addr: "https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493"},
    ]

    return {
      imgs,
    }
  }
}
</script>

<style scoped>
.screenshot {

}

.img-container {
  text-align: center;
  padding: 20px;
}
</style>