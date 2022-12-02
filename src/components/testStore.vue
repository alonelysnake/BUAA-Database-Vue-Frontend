<template>
  <div>
    <h3>count值为:{{store.state.count}}</h3>
    <button @click="add">+1</button>
  </div>
</template>

<script>
import store from "../store"


export default {
  name: "testStore",
  setup() {
    function add() {
      store.commit('test')
    }
    return {
      add,
      store,
    }
  }
}
</script>

<style scoped>

</style>