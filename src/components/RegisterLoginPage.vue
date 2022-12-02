<template>
  <router-link to="/Login">aaa</router-link>
  <router-link to="/Register">bbb</router-link>

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
  /*TODO 背景图片地址*/
  background-image: url("../assets/logo.png");
  background-size: cover;
  opacity: 50%;
  width: 100%;
  height: 800px;

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