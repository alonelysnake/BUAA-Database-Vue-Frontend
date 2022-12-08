<template>
  <n-card title="添加商品" closable @close="handleClose" hoverable>
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
      <n-form-item label="选择游戏" path="nameValue">
        <n-space id="search">
          <n-input v-model:value="model.nameValue" placeholder="按ID或游戏名搜索" clearable>
            <template #clear-icon>
              <n-icon :component="CloseCircleOutline" />
            </template>
          </n-input>
        </n-space>
      </n-form-item>
      <n-form-item label="CDKey" path="keyValue">
        <n-input v-model:value="model.keyValue" placeholder="游戏CDKey" />
      </n-form-item>
      <n-form-item label="steamID" path="steamValue">
        <n-input v-model:value="model.steamValue" placeholder="您的steam账号" />
      </n-form-item>
      <n-form-item label="商品详情" path="introValue">
        <n-input
            v-model:value="model.introValue"
            placeholder="商品介绍"
            type="textarea"
            :autosize="{
          minRows: 3,
          maxRows: 5
        }"
        />
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
import { ref } from "vue";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";
import store from "../store"

export default ({
  name: "AddGood",

  setup() {
    const formRef = ref(null);
    return {
      formRef,
      CloseCircleOutline,
      size: ref("medium"),
      model: ref({
        nameValue: null,
        keyValue: null,
        steamValue:null,
        introValue: null,
      }),
      rules: {
        nameValue: {
          required: true,
          trigger: ["blur", "input"],
          message: "请选择商品所属游戏"
        },
        keyValue: {
          required: false,
          trigger: ["blur", "input"],
        },
        steamValue: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入您的steamID"
        },
        introValue: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入商品详情"
        },

      },
      handleClose() {
        store.state.addGoodsVisible = false;
        // this.$emit(visible);
        console.log("取消添加游戏");
      },

      handleConfirm(e) {
        e.preventDefault();
        store.state.addGoodsVisible = false;
        // todo 向后端发送数据
        // this.$emit(visible);
        console.log("确定添加游戏");
      }
    };
  }
})
</script>

<style scoped>
.n-card {
  max-width: 300px;
}
</style>