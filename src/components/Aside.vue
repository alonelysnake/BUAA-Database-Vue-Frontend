<template>
  <div class="aside-container">
    <n-menu
            class="aside"
            v-model:value="activeKey"
            mode="vertical"
            :options="menuOptions"
            @update:value="handleSelect"
    />
  </div>

</template>

<script>
import { defineComponent, h, ref } from "vue";
import { NIcon } from "naive-ui";
import {
  PersonOutline as PersonIcon,
  RocketOutline as RibbonIcon,
  DocumentOutline as DocIcon,
  CardOutline as CardIcon,
  CartOutline as CartIcon,
} from "@vicons/ionicons5";
import router from "@/router";
import store from "@/store";

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
    icon: renderIcon(CartIcon),
  },
  {
    label: "卖家中心",
    key: "seller",
    icon: renderIcon(RibbonIcon),
    children: [
      {
        label: "商品",
        key: "goods",
        icon: renderIcon(CardIcon),
      },
      {
        label: "订单",
        key: "order",
        icon: renderIcon(DocIcon),
      },
    ]
  }
];

export default defineComponent({
  name: "Aside",
  setup() {
    return {
      activeKey: ref(null),
      menuOptions,

      handleSelect(key, item) {
        // console.log(key);
        switch (key) {
          case "userInfo":
            router.push("/user/" + store.state.user.userID + "/info");
            break;
          case "buyer":
            router.push("/user/" + store.state.user.userID + "/buyer");
            break;
          case "goods":
            router.push("/user/" + store.state.user.userID + "/sellerGoods");
            break;
          case "order":
            router.push("/user/" + store.state.user.userID + "/sellerOrder");
            break;
        }
      }
    };
  }
});
</script>

<style scoped>
  .aside-container {
    height: 700px;
    border-right: 1px solid rgb(204, 204, 204);
    float: left;
    margin-right: 30px;
  }

 .aside {
   width: 200px;
   height: 100%;
 }
</style>