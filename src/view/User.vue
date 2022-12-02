<template>
  <Aside/>
<!--  <div style="position: absolute;left: 250px;top: 100px;width: 70%;">-->
<!--    <router-view style="position: relative;left: 0;right: 0;margin-right: auto;margin-left: auto"></router-view>-->
<!--  </div>-->
<router-view style="margin-top: 31px"></router-view>


</template>

<script>
import Aside from "@/components/Aside";
export default {
  name: "UserPage",
  components: {Aside}
}
</script>

<style scoped>

</style>