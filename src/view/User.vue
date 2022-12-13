<template>
  <Aside/>
  <n-message-provider>
    <n-dialog-provider>
      <router-view style="margin-top: 31px"></router-view>
    </n-dialog-provider>
  </n-message-provider>


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