<template>
  <n-card title="评价此次交易" closable @close="handleClose" hoverable>
    <n-form
        ref="formRef"
        :model="model"
        :rules="rules"
        label-placement="left"
        label-width="auto"
        require-mark-placement="right-hanging"
        :size="size"
    >
      <n-form-item label="评价" path="likeValue">
        <n-radio-group v-model:value="model.likeValue" name="radiogroup1">
          <n-space>
            <n-radio value="like">
              好评
            </n-radio>
            <n-radio value="dislike">
              差评
            </n-radio>
          </n-space>
        </n-radio-group>
      </n-form-item>
      <n-form-item label="评价内容" path="contentValue">
        <n-input
            v-model:value="model.contentValue"
            placeholder="写写您的购物体会吧"
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
import {defineProps, ref} from "vue";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";
import store from "../store"
import {useMessage} from "naive-ui";
import request from "@/utils/request";


export default {
  name: "Appraise",

  setup() {
    const props = defineProps(['orderId']);
    const message = useMessage();
    const formRef = ref(null);
    const model = ref({
      likeValue: null,
      contentValue: null,
    })
    return {
      formRef,
      CloseCircleOutline,
      size: ref("medium"),
      model,
      rules: {
        likeValue: {
          required: true,
          trigger: "change",
          message: "请选择评价"
        },
        contentValue: {
          required: false,
          trigger: ["blur", "input"],
          message: "请输入评价"
        },

      },
      handleClose() {
        store.state.appraiseVisible = false;
        // console.log("取消评价");
      },

      handleConfirm(e) {
        e.preventDefault();
        store.state.appraiseVisible = false;
        request.post("/rateGoods/",JSON.stringify(
            {'id':store.state.rateGoodsId,
              'rating':model.value.likeValue,
          'comment':model.value.contentValue})).then(res=>{
          message.success(res.messsage);
        })
      }
    };
  }
}
</script>

<style scoped>
.n-card {
  max-width: 400px;
}
</style>