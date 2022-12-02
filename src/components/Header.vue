<template>
  <nav class="navbar header">
    <router-link class="navbar-brand" to="/" style="margin-left: 3.5%">
      <n-avatar class="picture"
          size="small"
          :src="logoUrl"
          color="white"
      />
    </router-link>
    <div class="collapse" id="top-menu">
      <ul class="navbar-nav" style="margin-right: 25%">
        <li class="nav-item1">
          <n-space id="search">
            <n-input round placeholder="搜索" clearable style="min-width: 200px">
              <template #suffix>
                <n-icon :component="FlashOutline" />
              </template>
              <template #clear-icon>
                  <n-icon :component="CloseCircleOutline" />
              </template>
            </n-input>
          </n-space>
        </li>
        <li class="nav-item1">
          <a class="nav-link" href="/">
            <n-button text>
              优惠
            </n-button>
          </a>
        </li>
        <li class="nav-item1">
          <a class="nav-link" href="/">
            <n-button text>
              热门
            </n-button>
          </a>
        </li>
        <li class="nav-item1">
          <a class="nav-link" href="/">
            <n-button text>
              订单
            </n-button>
          </a>
        </li>
        <li class="nav-item1">
          <a class="nav-link" href="/">
            <n-button text>
              关于
            </n-button>
          </a>
        </li>
      </ul>
      <ul class="navbar-nav" style="margin-left: 25%;left: 10%">
        <li class="nav-item2">
          <n-space id="avatar">
            <n-avatar class="picture"
                      :src="headUrl"
                      round
                      size="small"
            />
          </n-space>
        </li>
        <li class="nav-item2">
          <div style="width: 100px">
            <n-dropdown :options="options">
              <n-button round>
                <n-ellipsis style="max-width: 60px">
                  <!--            {{ userName }}-->
                  {{userId}}
                </n-ellipsis>
              </n-button>
            </n-dropdown>
          </div>
        </li>
      </ul>
    </div>

  </nav>

</template>

<script>

import { h,computed } from "vue";
import { NIcon } from "naive-ui";

import {
  SearchSharp,
  CloseCircleOutline,
  PersonCircleOutline as UserIcon,
  LogOutOutline as LogoutIcon,
  TrainOutline as TrainIcon
} from "@vicons/ionicons5";

import headUrl from "../static/img/head.jpg"
import logoUrl from "../assets/logo.png"
import { RouterLink } from "vue-router";
import store from "../store"

const renderIcon = (icon) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon)
    });
  };
};

export default {
  name: "Header",
  // todo 实现跳转登陆注册页面，登出，搜索等功能
  props: {
    headIndex: String,
  },

  setup() {
    let userId = computed(()=>{
      return store.state.user.userID
    })
    return {
      userId,
      options: [
        {
          label: () => h(
              RouterLink,
              {
                to: {
                  name: 'User',
                  params: {
                    username: userId.value
                  }
                }
              },
              {
                default: () => "个人中心"
              }
          ),
          key: "profile",
          icon: renderIcon(UserIcon),
        },
        {
          label: "退出登录",
          key: "logout",
          icon: renderIcon(LogoutIcon)
        }

      ],
      headUrl:headUrl,
      logoUrl:logoUrl,
      FlashOutline: SearchSharp,
      CloseCircleOutline,
      TrainIcon
    };
  }
}
</script>

<style scoped>
.header {
  height: 63px; line-height: 38px; border-bottom: 1px solid #ccc; display: flex;align-items: center;width: 100%;
}

ul {
  list-style: none;
}

a {
  text-decoration: none;
}

#top-menu {
  margin-left: 100px;display: flex;align-items: center;width: 100%
}

.navbar-brand {
  height: 42px; position: relative;left: 30px;
}

.navbar-nav {
  position: relative;display: flex;align-items: center;
}

.picture {
  position: absolute;top: 0;bottom: 0;margin-top: auto;margin-bottom: auto
}

.nav-item1 {
  float: left;margin-right: 20%;width: auto;
}

.nav-item2 {
  float: right;margin-left: 5px;width: auto;
}


#avatar {
  height: 50px; position: relative;right: 50px
}

</style>