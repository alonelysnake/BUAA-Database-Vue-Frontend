<template>
  <div style="white-space: nowrap; width: 1500px;margin-left: 20px">
    <ul v-for="item in items" :key="item.id" style="position:relative;">
      <n-card class="card"
              :title="item.name"
              closable
              hoverable
              @close="handleDel(item.id)"
              style="max-width: 233px"
      >
        <template #cover>
<!--          <router-link-->
<!--              :to="{name:'Detail',params:{gameid:item.game_id}}"-->
<!--          >-->
          <img :src="item.cover" @click="link(item.id)">
<!--          </router-link>-->
        </template>
      </n-card>
    </ul>
  </div>
</template>

<script>
import {onBeforeMount, ref} from "vue";
import request from "@/utils/request";
import store from "@/store";
import router from "@/router";
import {useMessage} from "naive-ui";

let items = ref([])
const load = () => {
  request.post("/getUserFavorites/",JSON.stringify({'user_id':store.state.user.userID})).then(res=>{
    items.value = res.data
    // console.log(items.value)
  })
}
export default {
  name: "FavoriteGame",

  setup() {
    onBeforeMount(()=>{
      load()
    })
    const message = useMessage()
    return {
      items,
      handleDel(id) {
        request.post("/delFavorites/",JSON.stringify({"user_id":store.state.user.userID,"game_id":id})).then(res=>{
          if (res.message === '已从收藏夹中删除') {
            message.success('取消收藏')
            load()
          }
          else {
            message.error('取消收藏失败')
          }
        })
      },
      link(id) {
        router.push('/detail/' + id + '/price')
      }
    }
  }
}
</script>

<style scoped>
.card {
  list-style: none;
  float: left;
  margin-right: 20px;
  margin-bottom: 20px;
}
</style>