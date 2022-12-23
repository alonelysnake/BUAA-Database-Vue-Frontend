<template>
  <n-scrollbar x-scrollable trigger="hover" style="width: 600px">
    <div style="white-space: nowrap; width: 1350px">
      <ul v-for="item in items.value" :key="item.id" style="position:relative;">
        <Card class="card"
              :target="item.target"
              :title="item.title"
              :img-url="item.url"
              :text="item.test"/>
      </ul>
    </div>
  </n-scrollbar>
</template>

<script>
import Card from './Card'
import {reactive} from "vue";
import request from "@/utils/request";

export default {
  name: "Cards",
  components: {Card},

  setup() {
    let items = reactive([])
    const load = () => {
      request.post("/getNews/",JSON.stringify({})).then(res=>{
        items.value = res.data
        // console.log(items.value)
      })
    }
    load()
    return {
      Card,
      items,
    }
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