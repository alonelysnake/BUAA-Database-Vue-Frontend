<template>
  <div style="margin-left: 200px">
    <n-form
        ref="formRef"
        :model="model"
        :rules="rules"
        label-placement="left"
        label-width="auto"
        require-mark-placement="right-hanging"
        size="medium"
        :disabled="isSelf.value"
        :style="{
      maxWidth: '640px',
    }"
    >
      <!--  todo 还没搞清楚path、v-model、检查上传文件、增加保存  -->
      <n-form-item label="用户头像" path="avatarValue">
          <div>
            <n-avatar
                size="large"
                src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
            />
          </div>

          <n-upload
              directory-dnd
              v-if="isSelf.valueOf()"
          >
            <n-button style="height: 40px;margin-left: 20px">上传头像</n-button>
          </n-upload>
      </n-form-item>
      <div style="min-height: 100px">
        <n-statistic
            label="已售出"
            tabular-nums
            class="statistic"
            style="margin-left: 5px"
        >
          <n-number-animation
              ref="numberAnimationInstRef"
              :from="0"
              :to="model.likeValue"
              duration="1000"
          />
          <template #suffix>
            份商品
          </template>
        </n-statistic>
        <n-statistic
            label="共收获"
            tabular-nums
            class="statistic"
        >
          <n-number-animation
              ref="numberAnimationInstRef"
              :from="0"
              :to="model.likeValue"
              duration="1000"
          />
          <template #suffix>
            条好评
          </template>
        </n-statistic>
        <n-statistic
            label="共得到"
            tabular-nums
            class="statistic"
        >
          <n-number-animation
              ref="numberAnimationInstRef"
              :from="0"
              :to="model.dislikeValue"
              duration="1000"
          />
          <template #suffix>
            条差评
          </template>
        </n-statistic>
      </div>
      <n-form-item label="用户名" path="userIdValue">
        <n-input v-model:value="model.userIdValue" placeholder="用户名" disabled/>
      </n-form-item>
      <n-form-item v-if="isSelf.valueOf()" label="用户邮箱" path="emailValue">
        <n-input v-model:value="model.emailValue" placeholder="用户邮箱" disabled/>
      </n-form-item>
      <n-form-item label="昵称" path="nickNameValue">
        <n-input v-model:value="model.nickNameValue" placeholder="昵称"/>
      </n-form-item>
      <n-form-item label="性别" path="sexValue">
        <n-radio-group v-model:value="model.sexValue" name="radiogroup1">
          <n-space>
            <n-radio value="male">
              男
            </n-radio>
            <n-radio value="female">
              女
            </n-radio>
            <n-radio value="secret">
              保密
            </n-radio>
          </n-space>
        </n-radio-group>
      </n-form-item>
      <n-form-item label="个人简介" path="introValue">
        <n-input
            v-model:value="model.introValue"
            placeholder="个人简介"
            type="textarea"
            :autosize="{
          minRows: 3,
          maxRows: 5
        }"
        />
      </n-form-item>
      <div style="display: flex; justify-content: flex-end" v-if="isSelf.valueOf()">
        <n-button round type="primary" @click="handleSave">
          保存
        </n-button>
      </div>
    </n-form>
  </div>


</template>

<script>
import { ref } from "vue";
import { ArchiveOutline as ArchiveIcon } from "@vicons/ionicons5";
import {useMessage} from "naive-ui"
import store from "@/store";
import request from "@/utils/request";
import { useRouter } from 'vue-router'


export default ({
  name: "UserInfo",

  setup() {
    const router = useRouter();

    const formRef = ref(null);
    const message = useMessage();
    const numberAnimationInstRef = ref(null);
    const targetUserId = ref(router.currentRoute.value.params.username);
    const model = ref({
          avatarPath: store.state.user.avatar,
          emailValue: store.state.user.email,
          userIdValue: store.state.user.userID,
          nickNameValue:store.state.user.nickname,
          introValue: store.state.user.intro,
          sexValue: store.state.user.sex,
          likeValue: store.state.user.like,
          dislikeValue: store.state.user.dislike,
        });
    const isSelf = ref(targetUserId.value === model.value.userIdValue);
    console.log(isSelf.value)
    if (!isSelf.value) {
      // 从后台加载
    }
    return {
      isSelf,
      formRef,
      numberAnimationInstRef,
      ArchiveIcon,
      async beforeUpload(data) {
        if (data.file.file?.type !== "image/jpg") {
          return false;
        }
        return true;
      },
      model,

      handleSave() {
        // request.post("/user/editInfo",JSON.stringify(this.model)).then(res=>{
        //
        // })
        if (/* 成功退款 */true) {
          message.success("修改成功");
        }
        else {
          message.error("退款失败");
        }
      },
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
        emailValue: {
          required: false,
          trigger: ["blur", "input"],
          message: "请输入 inputValue"
        },
        nickNameValue: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入昵称"
        },
        introValue: {
          required: false,
          trigger: ["blur", "input"],
        },
        sexValue: {
          required: false,
          trigger: "change",
        },
      },
    };
  }
});
</script>

<style scoped>
.statistic {
  float: left;
  min-width: 160px;
  margin-right: 40px
}
</style>