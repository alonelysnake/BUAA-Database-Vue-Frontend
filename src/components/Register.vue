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
          type="password"
          show-password-on="mousedown"
          placeholder="请输入密码6-15位"
          :maxlength="15"
          :minlength="6"
          size="small"
      />

      <n-input
          type="password"
          show-password-on="mousedown"
          placeholder="请再次输入密码"
          :maxlength="15"
          :minlength="6"
          size="small"
      />

      <div style="text-align: right">

        <n-button type="success" :loading="loading" @click="handleLogin">
          完成注册
        </n-button>

      </div>

    </n-space>

  </n-space>

</template>

<script>
import {ref, computed} from "vue";
import {GlassesOutline, Glasses} from '@vicons/ionicons5'

export default {
  name: "Register",
  setup() {
    const mail = ref("");
    const loading = ref(false);

    return {
      mail: mail,
      loading: loading,

      // TODO 处理登录按钮事件
      handleLogin() {
        loading.value = true;
        setTimeout(() => {
          loading.value = false;
        }, 2e3);
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
.global{
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