<template>
  <n-card title="修改密码" embedded closable @close="handleClose" hoverable>
    <n-form
        ref="formRef"
        :model="model"
        :rules="rules"
        label-placement="left"
        label-width="auto"
        require-mark-placement="right-hanging"
        :size="size"
        :style="{
      maxWidth: '640px'
    }"
    >
      <n-form-item label="原密码" path="oldPassword">
        <n-input
            type="password"
            show-password-on="click"
            v-model:value="model.oldPassword" placeholder="请输入原密码" />
      </n-form-item>
      <n-form-item label="新密码" path="newPassword">
        <n-input
            type="password"
            show-password-on="click"
            v-model:value="model.newPassword" placeholder="请输入新密码" />
      </n-form-item>
      <div style="display: flex; justify-content: flex-end">
        <n-button style="margin-right: 10px" round @click="handleClose">
          取消
        </n-button>
        <n-button round type="primary" @click="handleConfirm">
          确认
        </n-button>
      </div>
    </n-form>
  </n-card>
</template>

<script>
import {ref, reactive} from "vue";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";
import store from "../store"
import request from "@/utils/request";
import md5 from 'js-md5';

export default ({
  name: "ModifyPassword",

  setup() {
    const model = reactive({
      id: store.state.user.userID,
      oldPassword: null,
      newPassword:null,
    })

    const confirmModify = () => {
      model.oldPassword = md5(model.oldPassword);
      model.newPassword = md5(model.newPassword);
      console.log(model)
      request.post("/changePassword/",JSON.stringify({"password":model})).then(res=>{
        console.log(res.data)
      })
    }

    const formRef = ref(null);
    return {
      formRef,
      model,
      CloseCircleOutline,
      size: ref("medium"),

      rules: {
        oldPassword: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入原密码",
        },
        newPassword: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入新密码"
        }
      },

      handleClose() {
        store.state.modifyVisible = false;
      },

      handleConfirm(e) {
        e.preventDefault();
        store.state.modifyVisible = false;
        confirmModify();
      }
    };
  }
})
</script>

<style scoped>
.n-card {
  max-width: 300px;
}

.modifyCard {
  position: absolute;
  top: 250px;
  left: 0;
  right: 0;
  margin-right: auto;
  margin-left: auto;
}
</style>