<template>
  <a :href="target">
    <n-card :title="title" hoverable>
      <template #cover>
        <img :src="imgUrl">
      </template>
      <n-ellipsis style="max-width: 200px">
        {{text}}
      </n-ellipsis>

    </n-card>
  </a>
</template>

<script>
export default {
  name: "Card",
  props:{
    // 超链接地址
    target:String,
    // 卡片标题
    title:String,
    // 卡片内容
    text:String,
    // 图片url
    imgUrl:String
  }
}
</script>

<style scoped>
.n-card {
  max-width: 245px;
  max-height: 300px;
}

a {
  text-decoration: none;
}
</style>