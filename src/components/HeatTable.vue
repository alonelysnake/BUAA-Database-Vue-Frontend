<template>
  <n-data-table :columns="columns" :data="data"/>
</template>

<script>
import {defineComponent, h} from "vue";
import {NButton, NImage} from "naive-ui";


const createColumns = ({clickGameName: clickGameName}) => {
  return [
    {
      title: "排名",
      key: "no",
      width: 120,
      render: (_, index) => {
        return index + 1;
      }
    },
    {
      title: "",//游戏图标
      key: "icon",//图片
      width:140,
      render: (value) => {
        return h(
            NImage,
            {
              width:140,
              height:40,
              src: value.img
            }
        )
      }
    },
    {
      title: "游戏名",
      key: "name",
      render: (value) => {
        return h(
            NButton,
            {
              text: true,
              type: 'primary',
              onClick: () => clickGameName(value)
            },
            {default: () => value.name}
        )
      }
    },
    {
      title: "当前热度",
      key: "cur",
      width: 160
    },
    {
      title: "最高热度",
      key: "max",
      width: 160
    }
    //TODO 增加对比
  ];
};

/*
* cur:当前热度（在线人数）
* max:最大热度
* */
const data = [
  {id: 3, img:"https://cdn.cloudflare.steamstatic.com/steam/apps/1599340/header.jpg?t=1670026493", name: "Houkai 3rd", cur: 99, max: 999},
  {id: 9, img:"https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "Genshin Impact", cur: 2999, max: 19990},
  {id: 8, img:"https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 2, max: 160},
  {id: 2, img:"https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 21, max: 150},
  {id: 4, img:"https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 22, max: 110},
  {id: 6, img:"https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg", name: "aa", cur: 32, max: 130}
];

export default defineComponent({
  name: 'HeatTable',
  setup() {
    return {
      data,
      columns: createColumns({
        clickGameName(value) {
          //TODO 跳转到游戏详情页，路由为 'gameinfo/游戏id'的样子？
          console.log(value.id)
        }
      }),
      pagination: false,
    }
  }
});
</script>