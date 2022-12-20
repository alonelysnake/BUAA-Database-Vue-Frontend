<template>
  <div class="screenshot">
    <n-grid :cols="2">
      <n-gi v-for="img in imgs" :key="img.game_id" class="img-container">
        <n-image width="600" :src="img.url"/>
      </n-gi>
    </n-grid>
  </div>
</template>

<script>
import {useRouter} from "vue-router";
import request from "@/utils/request";
import {ref} from "vue";

export default {
  name: "ScreenShot",

  setup() {
    const router = useRouter();
    const gameId = parseInt(router.currentRoute.value.params.gameid);
    //TODO 根据游戏id获取所有图片
    let imgs = ref([]);
    request.post("/getGamePhoto/", JSON.stringify({"game_id": gameId})).then(res => {
      imgs.value = res.data;
    });

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