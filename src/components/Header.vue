<template>
  <div style="height: 50px; line-height: 50px; border-bottom: 1px solid #ccc; display: flex">
    <div style="width: 200px">logo</div>
    <div style="flex: 1"></div>
    <div style="width: 200px">
      <n-dropdown :options="options">
        <n-button>用户资料</n-button>
      </n-dropdown>
    </div>
  </div>
</template>

<script>
import {h} from "vue";
import {NIcon} from "naive-ui";
import {
  PersonCircleOutline as UserIcon,
  Pencil as EditIcon,
  LogOutOutline as LogoutIcon
} from "@vicons/ionicons5";

const renderIcon = (icon) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon)
    });
  };
};

export default {
  name: "Header",

  setup() {
    return {
      options: [
        {
          label: "用户资料",
          key: "profile",
          icon: renderIcon(UserIcon)
        },
        {
          label: "编辑用户资料",
          key: "editProfile",
          icon: renderIcon(EditIcon)
        },
        {
          label: "退出登录",
          key: "logout",
          icon: renderIcon(LogoutIcon)
        }
      ]
    };
  }

}
</script>

<style scoped>

</style>