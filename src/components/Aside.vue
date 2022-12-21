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
    HeartOutline as FavorIcon,
} from "@vicons/ionicons5";
import router from "@/router";
import store from "@/store";
import {useRouter} from "vue-router";

function renderIcon(icon) {
  return () => h(NIcon, null, { default: () => h(icon) });
}

let menuOptions = [
  {
    label: "个人信息",
    key: "userInfo",
    icon: renderIcon(PersonIcon),
  },
  {
    label: "我的收藏",
    key: "favor",
    icon: renderIcon(FavorIcon),
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
    const route = useRouter();
    if (parseInt(route.currentRoute.value.params.username) !== store.state.user.userID) {
      menuOptions = [
        {
          label: "个人信息",
          key: "userInfo",
          icon: renderIcon(PersonIcon),
        },
        {
          label: "商品",
          key: "goods",
          icon: renderIcon(CardIcon),
        },
      ];
    }
    return {
      activeKey: ref(null),
      menuOptions,

      handleSelect(key) {
        // console.log(key);
        if (parseInt(route.currentRoute.value.params.username) !== store.state.user.userID) {
          //console.log(route.currentRoute.value.params.username,store.state.user.userID)
          //console.log("访客进入")
          switch (key) {
            case "userInfo":
              router.push("/user_v/" + route.currentRoute.value.params.username + "/info");
              break;
            case "goods":
              router.push("/user_v/" + route.currentRoute.value.params.username + "/sellerGoods");
              break;
          }
        }
        else {
          //console.log("用户进入")
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
            case "favor":
              router.push("/user/" + store.state.user.userID + "/favor")
          }
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