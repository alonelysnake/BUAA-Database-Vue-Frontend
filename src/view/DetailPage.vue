<template>
  <div class="container">

    <!--    顶部导航栏-->
<!--    <div style="height: 60px; width: 100%">-->
<!--      <n-affix :top="0" :trigger-top="0" :listen-to="() => containerRef" class="head">-->
<!--        <Header ref="headerRef"/>-->
<!--      </n-affix>-->
<!--    </div>-->

    <!--    顶层基础信息-->
    <div class="basic-info">
      <!--      这里是游戏的基础信息-->
      <BasicInfo style="width: 100%"/>
    </div>

    <div class="content">
      <n-layout has-sider style="height: 100%;">

        <!--        选择查看不同详细信息的侧边栏-->
        <n-layout-sider
            bordered
            :width="240"
        >
          <!--        TODO 设置保持顶端-->
          <!--          <n-affix :top="0" :trigger-top="0" :listen-to="() => headerRef" class="sidebar">-->
          <n-menu
              :collapsed-width="10"
              :collapsed-icon-size="22"
              :options="menuOptions"
              children-field="whateverChildren"
              class="sidebar"
              @update:value="handleUpdateValue"
          />
          <!--          </n-affix>-->
        </n-layout-sider>

        <!--详细信息-->
        <n-layout class="detail">
          <div class="detail">
            <!--            TODO 实际内容切换-->
            <router-view></router-view>
          </div>
        </n-layout>

      </n-layout>
    </div>

  </div>
</template>

<script>
import {ref} from 'vue'
// import Header from "@/components/Header";
// import CountryPriceTable from "@/components/CountryPriceTable";
// import Charts from "@/components/Charts";
import BasicInfo from "@/components/BasicInfo";
import {useRouter} from "vue-router";

const menuOptions = [
  {
    label: '价格',
    key: 'price',
  },
  {
    label: "图表展示",
    key: "graph",
    disabled: false
  },
  {
    label: "评论",
    key: "comment",
    disabled: false
  },
  {
    label: "游戏截图",
    key: "screenshot",
    disabled: false
  }
]

export default {
  name: "DetailPage",
  props: {
    id: {
      default: "3",
    },
  },
  components: {
    // Header,
    // eslint-disable-next-line vue/no-unused-components
    // CountryPriceTable,
    // Charts,
    BasicInfo
  },
  setup() {
    // const containerRef = ref(void 0);
    // const headerRef = ref(void 0);
    const router = useRouter();

    const gameId = parseInt(router.currentRoute.value.params.gameid);//游戏id

    return {
      collapsed: ref(true),
      // containerRef,
      // headerRef,
      menuOptions,

      //路由跳转
      handleUpdateValue(key, item) {
        console.log("详情页侧边切换");
        console.log(gameId);
        switch (key) {
          case "price":
            router.push({name: "CountryPrice"});
            break;
          case "graph":
            router.push({name: "Chart"});
            break;
          case "comment":
            console.log("comment跳转未实现");
            break;
          case "screenshot":
            router.push({name: "ScreenShot"});
            break;
        }
      },
    };
  }
};
</script>

<style scoped>

/*整个页面*/
.container {
  width: 100%;
  height: 100%;
  background-color: blueviolet;
  border-radius: 3px;
  overflow: auto;
}

/*顶部导航栏*/
.head {
  height: 60px;
  width: 100%;
  /*background-color: white;*/
  z-index: 100;
}

/*基础信息*/
.basic-info {
  height: 220px;
  width: 100%;
  background-color: white;
}

/*详细信息*/
.content {
  height: 100%;
}

/*侧边导航栏*/
.sidebar {
  background-color: antiquewhite;
  height: 100%;
  /*z-index: 99;*/
  /*width: 240px;*/
}

.detail {
  background-color: aqua;
  height: 1000px;
  /*height: 1000px;*/
}
</style>