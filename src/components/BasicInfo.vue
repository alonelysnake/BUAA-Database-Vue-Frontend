<template>
  <n-space justify="center" style="padding: 10px">

    <n-table :bordered="false" :single-line="false" size="small" class="opacity">
      <thead>
      <n-text>{{ info.name.value }}</n-text>
      </thead>
      <tbody>
      <tr>
        <td style="width: 200px" class="opacity">游戏ID</td>
        <td style="width: 300px">{{ info.id.value }}</td>
      </tr>
      <tr>
        <td>标签</td>
        <td>{{ info.tags.value }}</td>
      </tr>
      <tr>
        <td>发行商</td>
        <td>{{ info.publisher.value }}</td>
      </tr>
      <tr>
        <td>出版商</td>
        <td>{{ info.publisher.value }}</td>
      </tr>
      <tr>
        <td>平台</td>
        <td>{{ info.platform.value }}</td>
      </tr>
      <tr>
        <td>发行日期</td>
        <td>{{ info.time.value }}</td>
      </tr>
      </tbody>
    </n-table>

    <!--宽设置统一-->
    <n-space vertical>
      <n-image height="160" :src="info.image.value"/>

      <n-button type="primary" @click="handleFavor">
        {{ favorButtonRef.text }}
      </n-button>
    </n-space>
  </n-space>
</template>

<script>
import {useRouter} from "vue-router/dist/vue-router";
import request from "@/utils/request";
import {onMounted, ref} from "vue";
import store from "@/store";

export default {
  name: "BasicInfo",
  setup() {
    const router = useRouter();
    const favorButtonRef = ref({
      "text": "收藏",
      "flag": false,
    })

    const gameId = parseInt(router.currentRoute.value.params.gameid);//游戏id
    let info = {
      "id": ref(''),
      "name": ref(''),
      "platform": ref(''),
      "publisher": ref(''),
      "time": ref(''),
      "tags": ref(''),
      "image": ref(''),
    };

    onMounted(() => {
      // 发送游戏id，得到游戏的id、游戏名、发行商、发行日期、标签
      request.post('/getGame/', JSON.stringify({'game_id': gameId})).then(res => {
        // console.log(res.data[0]);
        let gameInfo = res.data[0]
        info.id.value = gameInfo.id;
        info.name.value = gameInfo.name;
        info.platform.value = gameInfo.platform;
        for (let i = 0; i < gameInfo.developer.length; i++) {
          info.publisher.value += gameInfo.developer[i].name + " "
        }
        info.time.value = gameInfo.date;
        for (let i = 0; i < gameInfo.tag.length; i++) {
          info.tags.value += gameInfo.tag[i].tag + " "
        }
        info.image.value = gameInfo.cover;
      });

      let post = JSON.stringify({
        "game_id": gameId,
        "user_id": store.state.user.userID,
      });
      request.post("/isFavorites/", post).then(res => {
        // 根据res得到是否被收藏
        favorButtonRef.value.flag = res.data;
        if (favorButtonRef.value.flag) {
          favorButtonRef.value.text = "取消收藏";
        } else {
          favorButtonRef.value.text = "收藏";
        }
      })
    })

    function handleFavor() {
      let post = JSON.stringify({
        "game_id": gameId,
        "user_id": store.state.user.userID,
      });
      if (favorButtonRef.value.flag) {
        request.post('/delFavorites/', post).then(res => {
          favorButtonRef.value.flag = false;
          favorButtonRef.value.text = "收藏";
        })
      } else {
        request.post('/addFavorites/', post).then(res => {
          favorButtonRef.value.flag = true;
          favorButtonRef.value.text = "取消收藏";
        })
      }
    }

    return {
      info,
      favorButtonRef,
      handleFavor,
    };
  }
}
</script>

<style scoped>
.opacity {
  background-color: rgba(255, 0, 0, 0);
  /*opacity: 0;*/
}
</style>