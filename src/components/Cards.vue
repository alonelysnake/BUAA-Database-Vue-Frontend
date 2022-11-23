<template>
<!--  todo 从Card.vue引入-->
  <n-scrollbar x-scrollable trigger="none" style="width: 300px">
    <div style="white-space: nowrap; padding: 12px; width: 1000px">
      <ul style="position:relative;">
        <li>
          <n-card title="卡片">
            卡片内容
          </n-card>
        </li>
        <li>
          <n-card title="卡片">
            卡片内容
          </n-card>
        </li>
        <li>
          <n-card title="卡片">
            卡片内容
          </n-card>
        </li>
      </ul>
    </div>
  </n-scrollbar>
</template>

<script>
export default {
  name: "Cards"
}
</script>

<style scoped>

li {
  list-style: none;
  float: left;
  margin-right: 15px;
}

</style>