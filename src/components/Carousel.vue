<template>
<!--  todo 将图片地址设置为属性 增加点击图片的路由 -->

  <n-carousel
      autoplay interval="2500"
      show-arrow
      style="width: 100%;"
  >
    <n-carousel-item v-for="item in items" :key="item.id">
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

export default {
  name: "Carousel",

  setup() {
    let items = [
      {id:1,gameID:1,url:'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fstatics.klyou.cn%2Fimages%2Fuploadfiles%2F20190516%2F59074390.jpg&refer=http%3A%2F%2Fstatics.klyou.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673295600&t=9a7f474209c256501f36619e15eb1b0a'},
      {id:0,gameID:0,url:'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.199it.com%2Fwp-content%2Fuploads%2F2018%2F08%2F1533909558-3139-b5eab75f4eab636.jpg&refer=http%3A%2F%2Fwww.199it.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673295600&t=2b46e102c2f62ca11ddb8520eb3e1094'},

    ]
    // 从后端获取数据
    // let items = []
    // const load = () => {
    //   request.get("/api/carousel").then(res=>{
    //     items = res.data.records
    //   })
    // }
    // load()
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