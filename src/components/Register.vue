<template>

  <n-space class="global">

    <n-space vertical class="text-right">

      <div style="padding: 3px">用户名：</div>

      <div style="padding: 3px">密码：</div>

      <div style="padding: 3px">确认密码：</div>

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
          placeholder="请输入密码6-15位"
          :maxlength="15"
          :minlength="6"
          size="small"
      />

      <n-input
          v-model:value="check"
          type="password"
          show-password-on="mousedown"
          placeholder="请再次输入密码"
          :maxlength="15"
          :minlength="6"
          size="small"
      />

      <n-space style="text-align: right">

        <n-button v-text="'已有账户？点此登录'" @click="handleLogin" text-color="green"/>

        <n-button type="success" :loading="loading" @click="handleRegister">
          完成注册
        </n-button>

      </n-space>

    </n-space>

  </n-space>
</template>

<script>
import {ref, computed} from "vue";
import {GlassesOutline, Glasses} from '@vicons/ionicons5'
import {useRouter} from 'vue-router'
import {useMessage} from 'naive-ui'
import request from "@/utils/request"

export default {
  name: "Register",
  setup() {
    const mail = ref("");
    const password = ref("");
    const check = ref("");
    const loading = ref(false);
    const router = useRouter();
    const message = useMessage();

    return {
      mail: mail,
      password,
      check,
      loading: loading,

      // TODO 处理登录按钮事件
      handleRegister() {
        if (password.value !== check.value) {
          message.error("两次密码不一致");
          return;
        }

        loading.value = true;

        let success = false;
        // setTimeout(() => {
        //   loading.value = false;
        // }, 2e3);
        //TODO 前后端交互
        request.post("/register/", JSON.stringify({
          'mail:': mail.value,
          'password': password.value,
        })).then(res => {
          console.log(res.data);
          //TODO 后端的返回结果
          success = res.data;
        });
        if (success) {
          message.success('注册成功');
          router.push({name: "login"});
        } else {
          //TODO 注册失败反馈
          message.error('注册失败');
        }

        loading.value = false;
      },

      handleLogin() {
        // 跳转到登录界面
        router.push({name: 'login'})
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