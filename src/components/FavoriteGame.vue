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
          <router-link
              :to="{name:'Game',params:{gameId:item.game_id}}"
          >
          <img :src="item.url">
          </router-link>
        </template>
      </n-card>
    </ul>
  </div>
</template>

<script>
import {reactive} from "vue";
import request from "@/utils/request";

export default {
  name: "FavoriteGame",

  setup() {
    let items = [{
      id:1,
      name:'CyberPunk 2077',
      game_id:1,
      url: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.juxia.com%2Fupload%2F202104%2F02%2F02163737e1ea7ih8JTL7npy2rne.jpg&refer=http%3A%2F%2Fimg.juxia.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673708300&t=19ca6c235fa8906cc5c45af75bc1ca9b'
    },
      {
        id:2,
        game_id:2,
        name:'CyberPunk 2077',
        url: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.juxia.com%2Fupload%2F202104%2F02%2F02163737e1ea7ih8JTL7npy2rne.jpg&refer=http%3A%2F%2Fimg.juxia.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673708300&t=19ca6c235fa8906cc5c45af75bc1ca9b'
      },
      {
        id:3,
        game_id:3,
        name:'CyberPunk 2077',
        url: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.juxia.com%2Fupload%2F202104%2F02%2F02163737e1ea7ih8JTL7npy2rne.jpg&refer=http%3A%2F%2Fimg.juxia.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673708300&t=19ca6c235fa8906cc5c45af75bc1ca9b'
      },
      {
        id:4,
        game_id:4,
        name:'CyberPunk 2077',
        url: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.juxia.com%2Fupload%2F202104%2F02%2F02163737e1ea7ih8JTL7npy2rne.jpg&refer=http%3A%2F%2Fimg.juxia.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673708300&t=19ca6c235fa8906cc5c45af75bc1ca9b'
      },
      {
        id:5,
        game_id:5,
        name:'CyberPunk 2077',
        url: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.juxia.com%2Fupload%2F202104%2F02%2F02163737e1ea7ih8JTL7npy2rne.jpg&refer=http%3A%2F%2Fimg.juxia.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673708300&t=19ca6c235fa8906cc5c45af75bc1ca9b'
      },
      {
        id:6,
        game_id:6,
        name:'CyberPunk 2077',
        url: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.juxia.com%2Fupload%2F202104%2F02%2F02163737e1ea7ih8JTL7npy2rne.jpg&refer=http%3A%2F%2Fimg.juxia.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673708300&t=19ca6c235fa8906cc5c45af75bc1ca9b'
      }
    ]
    // const load = () => {
    //   request.post("/getUserFavorites/",JSON.stringify({})).then(res=>{
    //     items.value = res.data
    //     // console.log(items.value)
    //   })
    // }
    // load()
    return {
      items,
      handleDel(id) {
        request.post("/deleteFavor/",JSON.stringify({"id":id})).then(res=>{
          console.log(res.data)
        })
        console.log('取消收藏')
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