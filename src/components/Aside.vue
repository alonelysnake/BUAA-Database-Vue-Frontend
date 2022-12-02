<template>
  <n-menu v-model:value="activeKey" mode="vertical" :options="menuOptions" />
</template>

<script>
import { defineComponent, h, ref } from "vue";
import { NIcon } from "naive-ui";
import {
  PersonOutline as PersonIcon,
  WineOutline as WineIcon,
    RibbonOutline as RibbonIcon,
} from "@vicons/ionicons5";

function renderIcon(icon) {
  return () => h(NIcon, null, { default: () => h(icon) });
}

const menuOptions = [
  {
    label: "个人信息",
    key: "userInfo",
    icon: renderIcon(PersonIcon),
  },
  {
    label: "买家中心",
    key: "buyer",
    icon: renderIcon(RibbonIcon),
  },
  {
    label: "卖家中心",
    key: "seller",
    icon: renderIcon(BookIcon),
    children: [
      {
        type: "group",
        label: "人物",
        key: "people",
        children: [
          {
            label: "叙事者",
            key: "narrator",
            icon: renderIcon(PersonIcon)
          },
          {
            label: "羊男",
            key: "sheep-man",
            icon: renderIcon(PersonIcon)
          }
        ]
      },
      {
        label: "饮品",
        key: "beverage",
        icon: renderIcon(WineIcon),
        children: [
          {
            label: "威士忌",
            key: "whisky"
          }
        ]
      },
      {
        label: "食物",
        key: "food",
        children: [
          {
            label: "三明治",
            key: "sandwich"
          }
        ]
      },
      {
        label: "过去增多，未来减少",
        key: "the-past-increases-the-future-recedes"
      }
    ]
  }
];

export default defineComponent({
  setup() {
    return {
      activeKey: ref(null),
      menuOptions
    };
  }
});
</script>

<style scoped>

</style>