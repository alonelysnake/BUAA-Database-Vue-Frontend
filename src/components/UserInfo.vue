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

<!--        <n-upload-->
<!--            accept=".jpg,.png"-->
<!--            directory-dnd-->
<!--            action="http://127.0.0.1:1234/upload/ava"-->
<!--            v-if="isSelf.valueOf()"-->
<!--        >-->
          <n-upload
              accept=".jpg,.png"
              directory-dnd
              :file-list="fileList"
              :custom-request="uploadFile"
              :on-change="handleChange"
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
      <n-form-item label="用户名" path="id">
        <n-input v-model:value="model.id" placeholder="用户名" disabled/>
      </n-form-item>
      <n-form-item v-if="isSelf.valueOf()" label="用户邮箱" path="email">
        <n-input v-model:value="model.email" placeholder="用户邮箱" disabled/>
      </n-form-item>
      <n-form-item label="昵称" path="name">
        <n-input v-model:value="model.name" placeholder="昵称"/>
      </n-form-item>
      <n-form-item label="性别" path="gender">
        <n-radio-group v-model:value="model.gender" name="radiogroup1">
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
      <n-form-item label="个人简介" path="profile">
        <n-input
            v-model:value="model.profile"
            placeholder="个人简介"
            type="textarea"
            :autosize="{
          minRows: 3,
          maxRows: 5
        }"
        />
      </n-form-item>
      <div style="display: flex; justify-content: flex-end" v-if="isSelf.valueOf()">
        <n-button round type="primary" ghost @click="modify" style="margin-right: 10px">
          修改密码
        </n-button>
        <n-button round type="primary" @click="handleSave">
          保存
        </n-button>
      </div>
    </n-form>
    <ModifyPassword
        class="modifyCard" v-if="store.state.modifyVisible"
    >

    </ModifyPassword>
  </div>


</template>

<script>
import { ref } from "vue";
import { ArchiveOutline as ArchiveIcon } from "@vicons/ionicons5";
import {useMessage} from "naive-ui"
import store from "@/store";
import request from "@/utils/request";
import { useRouter } from 'vue-router'
import ModifyPassword from "@/components/ModifyPassword";

export default ({
  name: "UserInfo",
  components: {ModifyPassword},

  setup() {
    let fileList = [];
    const formData = ref({
      file:null
    });
    const router = useRouter();
    const formRef = ref(null);
    const message = useMessage();
    const numberAnimationInstRef = ref(null);
    const targetUserId = ref(router.currentRoute.value.params.username);
    const model = ref({
          avatarPath: store.state.user.avatar,
          email: store.state.user.email,
          id: store.state.user.userID,
          name:store.state.user.nickname,
          profile: store.state.user.intro,
          gender: store.state.user.sex,
          likeValue: store.state.user.like,
          dislikeValue: store.state.user.dislike,
        });
    const isSelf = ref(targetUserId.value === model.value.id);
    const load = () => {
      // todo 这里是获得信息
      request.post("/getSlide/",JSON.stringify({})).then(res=>{
        model.value.avatarPath = res.data.avatar
        model.value.email = res.data.email
        model.value.id = res.data.id
        model.value.name = res.data.name
        model.value.profile = res.data.profile
        model.value.gender = res.data.gender
        model.value.likeValue = res.data.likes
        model.value.dislikeValue = res.data.dislikes
      })
    }
    if (!isSelf.value) {
      load()
    }
    return {
      isSelf,
      formRef,
      numberAnimationInstRef,
      ArchiveIcon,
      store,
      model,

      handleChange(file,files) {
        fileList = files
      },

      uploadFile (file) {
        console.log(file.file, "sb2");
        formData.value.file = file.file;
      },

      modify() {
        store.state.modifyVisible = true;
      },

      handleSave() {
        // todo 上传头像
        // let formData = new FormData();
        // formData.append("file",fileList)
        // console.log(formData)
        // request.post("/api/upload",formData,
        //     {"Content-Type": "multipart/form-data;charset=utf-8"})
        // request.post("/user/editInfo",JSON.stringify(this.model)).then(res=>{
        //
        // })
        console.log("保存信息")
        request.post("/updateUser/",JSON.stringify({"content":model})).then(res=>{
          console.log(res.data)
        })
        if (/* 成功退款 */true) {
          message.success("修改成功");
        }
        else {
          message.error("修改失败");
        }
      },
      generalOptions: ["groode", "veli good", "emazing", "lidiculous"].map(
          (v) => ({
            label: v,
            value: v
          })
      ),
      rules: {
        id: {
          required: false,
          trigger: ["blur", "input"],
          message: "请输入 inputValue"
        },
        email: {
          required: false,
          trigger: ["blur", "input"],
          message: "请输入 inputValue"
        },
        name: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入昵称"
        },
        profile: {
          required: false,
          trigger: ["blur", "input"],
        },
        gender: {
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