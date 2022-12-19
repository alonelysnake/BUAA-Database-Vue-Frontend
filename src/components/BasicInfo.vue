<template>
  <n-space justify="center" style="padding: 10px">

    <n-table :bordered="false" :single-line="false" size="small" class="opacity">
      <thead>
      <n-text>{{ name }}</n-text>
      </thead>
      <tbody>
      <tr>
        <td style="width: 200px" class="opacity">游戏ID</td>
        <td style="width: 300px">{{ id }}</td>
      </tr>
      <tr>
        <td>标签</td>
        <td>{{ tags }}</td>
      </tr>
      <tr>
        <td>发行商</td>
        <td>{{ publisher }}</td>
      </tr>
      <tr>
        <td>出版商</td>
        <td>{{ publisher }}</td>
      </tr>
      <tr>
        <td>发行日期</td>
        <td>{{ time }}</td>
      </tr>
      </tbody>
    </n-table>

    <!--宽设置统一-->
    <n-image height="160" src="https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg?t=1668885944"/>
  </n-space>
</template>

<script>
import {useRouter} from "vue-router/dist/vue-router";
import request from "@/utils/request";

export default {
  name: "BasicInfo",
  setup() {
    const router = useRouter();

    const gameId = parseInt(router.currentRoute.value.params.gameid);//游戏id

    let data;
    //TODO 发送游戏id，得到游戏的id、游戏名、发行商、发行日期、标签
    // request.post('/getGame/', JSON.stringify({'id': gameId})).then(res => {
    //   data = res.data;
    // })
    console.log(data);
    let publisher = '游戏的发行商';
    let id = '游戏的id号';
    let name = '游戏名';
    let time = '游戏的发行日期';
    let tags = "射击 策略";

    return {
      id,
      name,
      publisher,
      time,
      tags,
    };
  }
}
</script>

<style scoped>
.opacity{
  background-color: rgba(255,0,0,0);
  /*opacity: 0;*/
}
</style>