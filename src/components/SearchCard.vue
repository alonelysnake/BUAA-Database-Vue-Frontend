<template>
  <div>
    <div>
      <n-input
          v-model:value="search"
          round
          placeholder="搜索"
          clearable
          @focus="focus"
          @blur="blur"
          style="min-width: 300px">
        <template #suffix>
          <n-icon :component="SearchSharp" />
        </template>
        <template #clear-icon>
          <n-icon :component="CloseCircleOutline" />
        </template>
      </n-input>
    </div>

    <n-card
        v-if="isSearch"
        class="box-card"
        @mouseenter="enterSearchBoxHandler"
        style="max-width:300px; position: absolute;z-index:15"
    >
      <dl v-if="isHistorySearch">
        <dt class="search-title" v-show="history">历史搜索</dt>
        <dt class="remove-history" v-show="history" @click="removeAllHistory">
          清空历史记录
        </dt>
        <n-tag
            v-for="search in historySearchList"
            :key="search.id"
            closable
            type="success"
            :bordered="false"
            @close="closeHandler(search)"
            @click="searchHandler(search.id,search.name)"
            style="margin-right:5px; margin-bottom:5px;"
        >
          {{search.name}}
        </n-tag>
      </dl>
      <dl v-if="isSearchList">
        <n-button
            v-for="search in searchList" :key="search.id"
            style="display:block;margin-bottom: 1px;min-width: 250px"
            quaternary
            @click="searchHandler(search.id,search.name)"
        >{{search.name}}</n-button>
      </dl>
    </n-card>
  </div>

</template>

<script>
import {CloseCircleOutline, SearchSharp,} from "@vicons/ionicons5";
import store from "../store";
import Local from "../utils/local"
import {computed, ref,watch} from "vue"
import request from "@/utils/request";
import router from "@/router";

export default {
  name: "SearchCard",

  setup() {

    let isFocus = ref(false) //是否聚焦
    let search = ref("") //当前输入框的值
    let historySearchList = ref([]) //历史搜索数据
    let searchList = ref(["暂无数据"]) //搜索返回数据,
    let history = ref(false)

    // 显示历史
    const isHistorySearch = computed(()=>{
      // console.log(isFocus.value && search.value === "")
      return isFocus.value && search.value === "" && historySearchList.value.length !== 0;
    })
    // 显示候选
    const isSearchList = computed(()=>{
      // console.log(search.value)
      return isFocus.value && search.value !== "";
    })
    // 显示搜索卡片
    const isSearch = computed(()=>{
      // console.log(historySearchList.value)
      return isFocus.value && (historySearchList.value.length !== 0 || search.value !== "");
    })
    let searchBoxTimeout = ref();

    const loadSearchList = () => {
      request.post("/searchGame/",JSON.stringify({'keyword':search.value})).then(res=>{

        searchList.value = res.data
        // console.log(searchList.value)
      })
    }

    watch(search,() => {
      loadSearchList();
    })
    return {
      store,
      isHistorySearch,
      isSearch,
      isSearchList,
      SearchSharp,
      search,
      CloseCircleOutline,
      // hotSearchList: ["暂无热门搜索"], //热门搜索数据
      historySearchList,
      searchList,
      history,
      focus() {
        isFocus.value = true
        let tmp = Local.loadHistory()
        let type = Object.prototype.toString.call(tmp);
        historySearchList.value = type === "[object Array]" ? Local.loadHistory():[]
        // historySearchList.value = [{id:1,name:"sekiro"}]
        // historySearchList.value = []
        history.value = historySearchList.value.length !== 0
      },
      blur() {
        searchBoxTimeout.value = setTimeout(function() {
          isFocus.value = false;
        }, 100);
      },

      enterSearchBoxHandler() {
        clearTimeout(searchBoxTimeout.value);
      },

      searchHandler(gameId,gameName) {
        // console.log("search")
        let exist =
            historySearchList.value.filter(value => {
              return value.id === gameId;
            }).length !== 0;
        if (!exist) {
          historySearchList.value.push({id:gameId,name: gameName});
          Local.saveHistory(historySearchList.value);
        }
        history.value = historySearchList.value.length !== 0;
        router.push("/detail/" + gameId + '/price')
        isFocus.value = false
        search.value = ''
      },

      closeHandler(search) {
        // console.log(search)
        historySearchList.value.splice(historySearchList.value.indexOf(search), 1);
        Local.saveHistory(historySearchList);
        clearTimeout(searchBoxTimeout.value);
        if (historySearchList.value.length === 0) {
          history.value = false;
        }
      },
      removeAllHistory() {
        // console.log("删除所有历史")
        Local.removeAllHistory();
      },
    }
  }
}
</script>

<style scoped>

#search {
  background-color: #ffc300;
  border-radius: 0%;
}
.search-title {
  color: #bdbaba;
  font-size: 15px;
  margin-bottom: 5px;
}
.remove-history {
  color: #bdbaba;
  font-size: 15px;
  float: right;
  margin-top: -29px;
}
#search-box {
  width: 555px;
  height: 300px;
  margin-top: 0px;
  padding-bottom: 20px;
}
</style>