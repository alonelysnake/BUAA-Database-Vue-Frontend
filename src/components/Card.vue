<template>
  <a href="/">
<!--    todo 将标题、封面、内容、跳转页面修改为属性-->
    <n-card title="带封面的卡片" hoverable>
      <template #cover>
        <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.yunspe.com%2Fwp-content%2Fuploads%2F2020%2F07%2F1585752363927035.jpg&refer=http%3A%2F%2Fwww.yunspe.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671712904&t=688e2cc763ea6ffcfb359e5fb1b9b3da">
      </template>
      卡片内容
    </n-card>
  </a>
</template>

<script>
export default {
  name: "Card",
}
</script>

<style scoped>
.n-card {
  max-width: 200px;
}

a {
  text-decoration: none;
}
</style>