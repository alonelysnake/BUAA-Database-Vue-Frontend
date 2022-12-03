<template>

  <div class="container">

    <div class="bg2"></div>

    <div class="form2">

      <router-view></router-view>

    </div>

  </div>

</template>

<script>

export default {
  name: "RegisterLoginPage",
  components: {
  }
}
</script>

<style scoped>
.container .bg2 {
  background-image: url("../static/img/login_bgp.jpg");
  background-size: cover;
  opacity: 50%;
  width: 100%;
  /*TODO 应该增加一个父容器然后设置height为100%*/
  height: 690px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.container .form2 {
  display: flex;
  justify-content: center;
  align-items: center;

  position: absolute;
  right: 5%;
  top: 50%;
  margin-top: -100px;
  /* margin-right: -100px; */
  color: #000000;
  padding: 20px 20px;
}

</style>