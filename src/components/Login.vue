<template>

  <n-space class="global">

    <n-space vertical class="text-right">

      <div style="padding: 3px">用户名：</div>

      <div style="padding: 3px">密码：</div>

    </n-space>

    <n-space vertical class="text-left">

      <n-auto-complete
          v-model:value="mail"
          :input-props="{
          autocomplete: 'disabled'
        }"
          :options="options"
          placeholder="请输入邮箱"
          size="small"
      />

      <n-input
          v-model:value="password"
          type="password"
          show-password-on="mousedown"
          placeholder="请输入密码"
          :maxlength="15"
          :minlength="6"
          size="small"
      />

      <n-space class="place-center" justify="space-between">

        <n-button v-text="'没有账户？点此注册'" @click="handleRegister" text-color="green"/>

        <n-button type="success" :loading="loading" @click="handleLogin">
          登录
        </n-button>

      </n-space>

    </n-space>

  </n-space>

</template>

<script>
import {ref, computed} from "vue";
import {useRouter} from 'vue-router'
import {GlassesOutline, Glasses} from '@vicons/ionicons5'
import {useMessage} from 'naive-ui'
import request from "@/utils/request";
import store from "@/store";
import md5 from 'js-md5';

export default {
  name: "Login",
  setup() {
    const mail = ref("");
    const password = ref("");
    const loading = ref(false);
    const router = useRouter();
    const message = useMessage();

    return {
      mail: mail,
      password,

      loading: loading,

      // TODO 处理登录按钮事件
      handleLogin() {
        loading.value = true;
        // setTimeout(() => {
        //   loading.value = false;
        // }, 2e3);
        //TODO 从后端接收反馈
        let post = {
          'email': mail.value,
          'password': md5(password.value),
        };
        request.post("/login/", JSON.stringify(post)).then(res => {
          //TODO 后端的返回结果
          let recvMessage = res.message;
          let userInfo = res.info;
          let success = !(userInfo.id === undefined);
          if (success) {
            message.success("登录成功");
            // 用户全局量赋值
            store.state.user.nickname = userInfo.username;
            store.state.user.userID = userInfo.id;
            store.state.user.sales = userInfo.sales;
            store.state.user.avatar = userInfo.photo;
            store.state.user.email = userInfo.email;
            store.state.user.intro = userInfo.profile;
            store.state.user.sex = userInfo.gender;
            store.state.user.like = userInfo.likes;
            store.state.user.dislike = userInfo.dislikes;
            store.state.loggedIn = true;

            router.push({name: "Home"});
          } else {
            //TODO 登录失败提示
            message.error(recvMessage);
          }
          loading.value = false;
        });
      },

      handleRegister() {
        // 跳转到注册页面
        router.push({name: 'register'})
      },

      options: computed(() => {
        return ["@gmail.com", "@163.com", "@qq.com"].map((suffix) => {
          const prefix = mail.value.split("@")[0];
          return {
            label: prefix + suffix,
            value: prefix + suffix
          };
        });
      }),
      GlassesOutline,
      Glasses
    };
  }
}
</script>

<style scoped>
.global {
  background: white;
  padding: 30px;
  border-radius: 10px;
  opacity: 95%;
}

.text-right {
  text-align: right;
}

.text-left {
  text-align: left;
}
</style>