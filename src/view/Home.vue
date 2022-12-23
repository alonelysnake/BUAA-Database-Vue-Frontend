<template>
  <div id="bg"></div>
  <div id="carousel">
    <h2 style="float: left;margin-right: 428px">热门游戏</h2>
    <n-button round style="margin-bottom: 10px" @click="toHeat">
      <template #icon>
        <n-icon :component="DotIcon"></n-icon>
      </template>
      更多
    </n-button>
    <Carousel />
  </div>
  <div id="cards">
    <h2 style="float: left;margin-right: 428px">最新资讯</h2>

      <n-button
          round
          style="margin-bottom: 10px"
          tag="a"
          href="https://store.steampowered.com/news"
      >
        <template #icon>
          <n-icon :component="DotIcon"></n-icon>
        </template>
        更多
      </n-button>

    <Cards/>
  </div>


</template>

<script>
import Cards from "@/components/Cards";
import Carousel from "@/components/Carousel";

import {
  EllipsisHorizontalOutline as DotIcon
} from "@vicons/ionicons5";
import router from "@/router";

export default {
  name: "Home",
  components: {Carousel,Cards},


  setup() {
    return {
      DotIcon,
      toHeat() {
        router.push('/heat')
      }
    }
  }

}
</script>

<style scoped>
  #bg {
    /*TODO 背景图片地址*/
    background-image: url("../static/img/home_bgp.jpeg");
    background-size: cover;
    opacity: 90%;
    width: 100%;
    height: 300px;
    margin-bottom: 30px;

    display: flex;
    justify-content: center;
    align-items: center;
  }

  #carousel {
    float: left;
    margin-left: 6%;
    width: 600px;
    height: 250px;
  }
  #cards {
    float: left;
    margin-left: 10%;
    width: 600px;
    height: 260px;
  }
</style>