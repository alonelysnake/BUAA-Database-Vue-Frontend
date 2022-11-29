<template>
  <n-space justify="center" style="padding: 10px">

    <n-table :bordered="false" :single-line="false" size="small">
      <thead>
      <n-text>{{ name }}</n-text>
      </thead>
      <tbody>
      <tr>
        <td style="width: 200px">游戏ID</td>
        <td style="width: 300px">{{ id }}</td>
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
export default {
  name: "BasicInfo",
  setup() {
    let publisher = '游戏的发行商';
    let id = '游戏的id号';
    let name = '游戏名';
    let time = '游戏的发行日期';
    return {
      id,
      name,
      publisher,
      time
    };
  }
}
</script>

<style scoped>

</style>