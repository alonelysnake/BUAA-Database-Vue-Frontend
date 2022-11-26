<template>
  <div ref="containerRef" class="container">

    <!--    顶部导航栏-->
    <div style="height: 60px; width: 100%">
      <n-affix :top="0" :trigger-top="0" :listen-to="() => containerRef" class="head">
        <Header ref="headerRef"/>
      </n-affix>
    </div>

    <!--    顶层基础信息-->
    <div class="basic-info">
      这里是游戏的基础信息
    </div>

    <div class="content">
      以下为游戏的不同详细信息
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
                key-field="whateverKey"
                label-field="whateverLabel"
                children-field="whateverChildren"
                class="sidebar"
            />
<!--          </n-affix>-->
        </n-layout-sider>

        <!--详细信息-->
        <n-layout class="detail">
          <div class="detail">
            根据侧边栏选择展示的的右侧内容
            <!--            TODO 实际内容切换-->
<!--            <CountryPriceTable/>-->
            <Charts style="background-color: white"/>
          </div>
        </n-layout>

      </n-layout>
    </div>

  </div>
</template>

<script>
import {ref} from 'vue'
import Header from "@/components/Header";
import CountryPriceTable from "@/components/CountryPriceTable";
import Charts from "@/components/Charts";

const menuOptions = [
  {
    whateverLabel: '价格',
    whateverKey: 'price'
  },
  {
    whateverLabel: "活跃度",
    whateverKey: "heat",
    disabled: false
  },
  {
    whateverLabel: "详细信息",
    whateverKey: "information",
    disabled: false
  },
  {
    whateverLabel: "游戏截图",
    whateverKey: "screenshots",
    disabled: false
  }
]

export default {
  name: "DetailPage",
  components: {
    Header,
    // eslint-disable-next-line vue/no-unused-components
    CountryPriceTable,
    Charts
  },
  setup() {
    const containerRef = ref(void 0);
    const headerRef = ref(void 0);

    return {
      collapsed: ref(true),
      containerRef,
      headerRef,
      menuOptions
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
  background-color: white;
  z-index: 100;
}

/*基础信息*/
.basic-info {
  height: 150px;
  width: 100%;
  background-color: blue;
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