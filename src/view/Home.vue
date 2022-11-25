<template>
  <Header/>
  <div id="bg">
  <div></div>
  </div>
  <div id="carousel"  style="width: 300px">
    <h2 style="float: left;margin-right: 150px">热门游戏</h2>
    <n-button round>更多</n-button>
    <Carousel />
  </div>

  <Cards id="cards"/>

</template>

<script>
import Header from "@/components/Header";
import Cards from "@/components/Cards";
import Carousel from "@/components/Carousel";

export default {
  name: "Home",
  components: {Header,Carousel,Cards},


  setup() {
  }

}
</script>

<style scoped>
  #bg {
    /*TODO 背景图片地址*/
    background-image: url("../assets/logo.png");
    background-size: cover;
    opacity: 50%;
    width: 100%;
    height: 300px;

    display: flex;
    justify-content: center;
    align-items: center;
  }

  #carousel {
    float: left;
    margin-left: 10%;
  }
  #cards {

  }
</style>