<template>
  <n-form
      ref="formRef"
      :model="model"
      :rules="rules"
      label-placement="left"
      label-width="auto"
      require-mark-placement="right-hanging"
      size="medium"
      :style="{
      maxWidth: '640px'
    }"
  >
<!--  todo 还没搞清楚path、v-model、检查上传文件、增加保存  -->
    <n-form-item label="用户头像" path="avatarValue">
      <n-avatar
          round
          src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
      />
      <n-upload
          directory-dnd
      >
        <n-button>上传头像</n-button>
      </n-upload>
    </n-form-item>
    <n-form-item label="用户名" path="userIdValue">
      <n-input v-model:value="model.userIdValue" placeholder="用户名" disabled/>
    </n-form-item>
    <n-form-item label="昵称" path="nickNameValue">
      <n-input v-model:value="model.nickNameValue" placeholder="昵称"/>
    </n-form-item>
    <n-form-item label="性别" path="radioGroupValue">
      <n-radio-group v-model:value="model.radioGroupValue" name="radiogroup1">
        <n-space>
          <n-radio value="Radio 1">
            男
          </n-radio>
          <n-radio value="Radio 2">
            女
          </n-radio>
          <n-radio value="Radio 3">
            保密
          </n-radio>
        </n-space>
      </n-radio-group>
    </n-form-item>
    <n-form-item label="个人简介" path="textareaValue">
      <n-input
          v-model:value="model.textareaValue"
          placeholder="个人简介"
          type="textarea"
          :autosize="{
          minRows: 3,
          maxRows: 5
        }"
      />
    </n-form-item>
    <div style="display: flex; justify-content: flex-end">
      <n-button round type="primary" @click="handleValidateButtonClick">
        验证
      </n-button>
    </div>
  </n-form>

</template>

<script>
import { ref } from "vue";
import { ArchiveOutline as ArchiveIcon } from "@vicons/ionicons5";

export default ({
  name: "User",

  setup() {
    const formRef = ref(null);
    return {
      formRef,
      ArchiveIcon,
      async beforeUpload(data) {
        if (data.file.file?.type !== "image/jpg") {
          return false;
        }
        return true;
      },
      model: ref({
        avatarPath: null,
        userIdValue: null,
        nickNameValue:null,
        textareaValue: null,
        radioGroupValue: null,
      }),
      generalOptions: ["groode", "veli good", "emazing", "lidiculous"].map(
          (v) => ({
            label: v,
            value: v
          })
      ),
      rules: {
        userIdValue: {
          required: false,
          trigger: ["blur", "input"],
          message: "请输入 inputValue"
        },
        nickNameValue: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入昵称"
        },
        textareaValue: {
          required: false,
          trigger: ["blur", "input"],
        },
        radioGroupValue: {
          required: false,
          trigger: "change",
        },
      }
    };
  }
});
</script>