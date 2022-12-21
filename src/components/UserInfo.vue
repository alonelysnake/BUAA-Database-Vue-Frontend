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
        :disabled="!isSelf.valueOf()"
        :style="{
      maxWidth: '640px',
    }"
    >
      <n-form-item label="用户头像" path="avatarValue">
          <div>
            <n-avatar
                size="large"
                :src="model.avatarPath"
                style="margin-right: 10px"
            />
          </div>
          <n-input v-if="isSelf.valueOf()" v-model:value="model.avatarPath" placeholder="头像图片地址"/>
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
              :to="model.sales"
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
      <n-form-item label="用户ID" path="id">
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
import {ref, onBeforeMount} from "vue";
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
    const router = useRouter();
    const formRef = ref(null);
    const message = useMessage();
    const numberAnimationInstRef = ref(null);
    const targetUserId = ref(router.currentRoute.value.params.username);
    const model = ref({
          avatarPath:   null,
          email:        null,
          sales:        null,
          id:           null,
          name:         null,
          profile:      null,
          gender:       null,
          likeValue:    null,
          dislikeValue: null,
        });
    const load = () => {
      request.post("/getUserInfo/",JSON.stringify({'id':targetUserId.value})).then(res=>{
        model.value.avatarPath = res.data.photo
        model.value.email = res.data.email
        model.value.id = res.data.id
        model.value.name = res.data.username
        model.value.profile = res.data.profile
        model.value.gender = res.data.gender
        model.value.sales = res.data.sales
        model.value.likeValue = res.data.likes
        model.value.dislikeValue = res.data.dislikes
      })
    }
    onBeforeMount(()=>{
      load()
    })
    const isSelf = ref(parseInt(targetUserId.value) === store.state.user.userID);
    //let isSelf = computed(()=> targetUserId.value === store.state.user.userID)
    // console.log(isSelf.value,targetUserId.value,store.state.user.userID)
    return {
      isSelf,
      formRef,
      numberAnimationInstRef,
      ArchiveIcon,
      store,
      model,
      targetUserId,
      modify() {
        store.state.modifyVisible = true;
      },

      handleSave() {
        request.post("/updateUser/",JSON.stringify({"content":model.value})).then(res=>{
          message.success(res.messsagee);
          // console.log(res.data)
        })
      },
      rules: {
        avatar: {
          required: true,
          trigger: ["blur", "input"],
          message: "请输入图片地址"
        },
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