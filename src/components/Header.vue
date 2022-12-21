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
          <SearchCard></SearchCard>
        </li>
        <li class="nav-item1">
          <a class="nav-link" href="/">
            <n-button text>
              首页
            </n-button>
          </a>
        </li>
        <li class="nav-item1">
          <router-link class="nav-link" to="/filter">
            <n-button text>
              优惠
            </n-button>
          </router-link>
        </li>
        <li class="nav-item1">
          <router-link to="/heat" class="nav-link" >
            <n-button text>
              热门
            </n-button>
          </router-link>
        </li>
        <li class="nav-item1">
          <a class="nav-link" href="/">
            <n-button text>
              关于
            </n-button>
          </a>
        </li>
      </ul>
      <ul v-if=store.state.loggedIn class="navbar-nav" style="margin-left: 20%;left: 10%">
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
                <n-ellipsis style="max-width: 70px">
                  {{store.state.user.nickname}}
                </n-ellipsis>
              </n-button>
            </n-dropdown>
          </div>
        </li>
      </ul>
      <ul v-else class="navbar-nav" style="margin-left: 20%;left: 10%">
        <n-button round @click="handleLog">登陆/注册</n-button>
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
  TrainOutline as TrainIcon,
  CartOutline as CartIcon,
} from "@vicons/ionicons5";

// import headUrl from "../static/img/head.jpg"
import headUrl from "../assets/logo.png"
import logoUrl from "../assets/logo.png"
import { RouterLink } from "vue-router";
import store from "../store"
import router from "@/router";
import SearchCard from "@/components/SearchCard";

const renderIcon = (icon) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon)
    });
  };
};

export default {
  name: "Header",

  components: {SearchCard},

  setup() {
    // console.log(store.state.user.avatar)
    let nickname = computed(()=>{
      return store.state.user.userID
    })
    return {
      store,
      nickname,
      options: [
        {
          label: () => h(
              RouterLink,
              {
                to: {
                  name: 'Info',
                  params: {
                    username: nickname.value
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
          label: () => h(
              RouterLink,
              {
                to: {
                  name: 'Buyer',
                  params: {
                    username: nickname.value
                  }
                }
              },
              {
                default: () => "我的订单"
              }
          ),
          key: "order",
          icon: renderIcon(CartIcon),
        },
        {
          label: "退出登录",
          key: "logout",
          icon: renderIcon(LogoutIcon),
          props: {
            onClick:() => {
              store.state.loggedIn = false;
              router.push('/home/')
              // console.log(store.state.loggedIn)
            }
          }
        }

      ],
      headUrl:store.state.user.avatar,
      logoUrl:logoUrl,
      FlashOutline: SearchSharp,
      CloseCircleOutline,
      TrainIcon,
      handleLog() {
        router.push("/logReg")
      }
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