<template>
  <n-scrollbar x-scrollable trigger="hover" style="width: 600px">
    <div style="white-space: nowrap; width: 1310px">
      <ul style="position:relative;">
        <Card class="card"/>
        <Card class="card"/>
        <Card class="card"/>
        <Card class="card"/>
        <Card style="list-style: none;float: left;"/>
      </ul>
    </div>
  </n-scrollbar>
</template>

<script>
import Card from './Card'

export default {
  name: "Cards",
  components: {Card},

  setup() {
    return [
      Card,
    ]
  }
}



</script>

<style scoped>

.card {
  list-style: none;
  float: left;
  margin-right: 20px;
}

</style>