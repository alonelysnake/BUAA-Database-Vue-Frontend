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
          <n-input v-model:value="model.nameValue"
                   placeholder="按游戏名搜索"
                   clearable
                   @focus="focus"
                   @blur="blur"
          >
            <template #clear-icon>
              <n-icon :component="CloseCircleOutline" />
            </template>
          </n-input>
          <n-card
              v-if="isSearch"
              class="box-card"
              @mouseenter="enterSearchBoxHandler"
              style="max-width:170px; position: absolute;z-index:15"
          >
            <dl v-if="isSearchList">
              <n-button
                  v-for="search in searchList" :key="search.id"
                  style="display:block;margin-bottom: 1px;min-width: 120px"
                  quaternary
                  @click="searchHandler(search.id,search.name)"
              >{{search.name}}</n-button>
            </dl>
          </n-card>
        </n-space>
      </n-form-item>
      <n-form-item label="CDKey" path="keyValue">
        <n-input v-model:value="model.keyValue" placeholder="游戏CDKey" />
      </n-form-item>
      <n-form-item label="商品价格" path="moneyValue">
        <n-input-number v-model:value="model.moneyValue" placeholder="商品价格" />
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
import {ref, defineProps, computed, watch, reactive} from "vue";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";
import store from "../store"
import request from "@/utils/request";

export default ({
  name: "AddGood",

  setup() {
    let isFocus = ref(false) //是否聚焦
    let search = ref("") //当前输入框的值
    let searchList = ref(["暂无数据"]) //搜索返回数据,
    const model = reactive({
      game_id: null,
      nameValue: null,
      keyValue: null,
      steamValue:null,
      introValue: null,
      moneyValue:null,
      seller_id: store.state.user.userID
    })
    // 显示候选
    const isSearchList = computed(()=>{
      // console.log(model.nameValue)
      return isFocus.value && model.nameValue !== null && model.nameValue !== "";
    })
    // 显示搜索卡片
    const isSearch = computed(()=>{
      // console.log(historySearchList.value)
      return isFocus.value && model.nameValue !== null && model.nameValue !== "";
    })
    let searchBoxTimeout = ref();

    const loadSearchList = () => {
      request.post("/searchGame/",JSON.stringify({'keyword':model.nameValue})).then(res=>{
        console.log(res.data)
        searchList.value = res.data
      })
    }

    watch(()=>model.nameValue,(newValue,oldVal) => {
      // console.log(model.nameValue)
      loadSearchList();
    })

    const addGoods = () => {
      request.post("/addGoods/",JSON.stringify({"goods":model})).then(res=>{
        console.log(res.data)
      })
    }

    const props = defineProps(['regular']);
    const formRef = ref(null);
    return {
      formRef,
      model,
      isSearch,
      isSearchList,
      search,
      searchList,
      CloseCircleOutline,
      size: ref("medium"),

      rules: {
        nameValue: {
          required: true,
          trigger: ["blur", "input"],
          message: "请选择商品所属游戏",

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
        moneyValue: {
          type: 'number',
          required: true,
          trigger: ["blur", "change"],
          message: "请输入商品价格"
        }
      },

      focus() {
        isFocus.value = true
      },

      blur() {
        searchBoxTimeout.value = setTimeout(function() {
          isFocus.value = false;
        }, 100);
      },

      enterSearchBoxHandler() {
        clearTimeout(searchBoxTimeout.value);
      },

      searchHandler(game_id,gameName) {
        model.game_id = game_id;
        model.nameValue = gameName
      },

      handleClose() {
        store.state.addGoodsVisible = false;
        // this.$emit(visible);
        console.log("取消添加游戏");
      },

      handleConfirm(e) {
        e.preventDefault();
        store.state.addGoodsVisible = false;
        addGoods();
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