<template>
  <n-scrollbar x-scrollable trigger="none" style="width: 500px">
    <div style="white-space: nowrap; padding: 12px; width: 1100px">
      <ul style="position:relative;">
        <Card class="card"/>
        <Card class="card"/>
        <Card class="card"/>
        <Card class="card"/>
        <Card class="card"/>
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
  margin-right: 15px;
}

</style>