<template>
<!--  todo 将图片地址设置为属性 增加点击图片的路由 -->

  <n-carousel
      autoplay interval="2500"
      show-arrow
      style="width: 100%;"
  >
    <n-carousel-item v-for="item in items.value" :key="item.id">
      <!--      todo 路由修改为游戏 8080/game/gameID   -->
<!--      <router-link-->
<!--        :to="{name:'Game',params:{gameID:item.gameID}}"-->
<!--      >-->
      <router-link
          :to="{name:'Info',params:{username:'Veronica'}}"
      >
        <img
            class="carousel-img"
            :src="item.url"
        >
      </router-link>
    </n-carousel-item>
    <template #dots="{ total, currentIndex, to }">
      <ul class="custom-dots">
        <li
            v-for="index of total"
            :key="index"
            :class="{ ['is-active']: currentIndex === index - 1 }"
            @mouseover= "to(index - 1)"
        />
      </ul>
    </template>
  </n-carousel>
</template>

<script>

import request from "@/utils/request";
import {reactive} from "vue";

export default {
  name: "Carousel",

  setup() {
    //从后端获取数据
    let items = reactive([])
    const load = () => {
      request.post("/getSlide/",JSON.stringify({})).then(res=>{
        items.value = res.data
        // console.log(items.value)
      })
    }
    load()
    return {
      items,
    }
  }
}
</script>

<style scoped>
.carousel-img {
  width: 100%;
  height: 248px;
  object-fit: cover;
}

.custom-dots {
  display: flex;
  margin: 0;
  padding: 0;
  position: absolute;
  bottom: 20px;
  left: 20px;
}

.custom-dots li {
  display: inline-block;
  width: 12px;
  height: 4px;
  margin: 0 3px;
  border-radius: 4px;
  background-color: rgba(255, 255, 255, 0.4);
  transition: width 0.3s, background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
}

.custom-dots li.is-active {
  width: 40px;
  background: #fff;
}

img {
  border-radius: 0.6em;
}
</style>