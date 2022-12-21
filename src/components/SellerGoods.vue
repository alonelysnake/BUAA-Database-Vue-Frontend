<template>
  <div class="header"
       v-if="isSelf.valueOf()">
    <div class="operate">
      <n-button type="primary" ghost style="height: 35px" @click="delAll">批量删除</n-button>
    </div>
<!--    <div class="operate">-->
<!--      <n-upload-->
<!--          action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"-->
<!--          @before-upload="beforeUpload"-->
<!--          style="display: inline"-->
<!--      >-->
<!--        <n-button type="primary" ghost style="height: 35px">批量导入</n-button>-->
<!--      </n-upload>-->
<!--    </div>-->
    <div class="operate">
      <n-button type="primary" ghost style="height: 35px" @click="handleAdd">添加商品</n-button>
    </div>
  </div>
  <div
      v-if="notSelf.valueOf()"
      style="min-height: 50px"
  >
  </div>
  <n-space vertical :size="12" style="width: 83%;position:relative;">
    <n-input v-model:value="search" placeholder="输入商品号或游戏名查询" style="width: 400px;"/>
    <n-data-table
        ref="table"
        :columns="columns"
        :data="filterTableData"
        :pagination="pagination"
        striped
        @update:sorter="handleSorterChange"
        :row-key="rowKey"
        @update:checked-row-keys="handleCheck"
    >
    </n-data-table>
    <AddGood class="goodCard" v-if="store.state.addGoodsVisible"></AddGood>
    <EditGood
        class="goodCard"
        v-if="store.state.editGoodsVisible"
        title="修改商品信息"
        edit="true"
    />
  </n-space>

</template>


<script>
import {h, ref, computed, onBeforeMount, watch} from "vue";
import {NButton, NImage, useDialog,useMessage,NEllipsis} from "naive-ui";
import store from "../store"
import AddGood from "@/components/AddGood";
import EditGood from "@/components/EditGood";
import {useRouter} from "vue-router";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";
import request from "@/utils/request";
import sleep from "@/utils/sleep";


const search = ref('')

// 用户本人的列表
const createColumns = ({
                         edit,del
                       }) => {
  return [
    {
      type: "selection",
      disabled() {
        return false;
      }
    },
    {
      title: "",
      key: "game_cover",
      width: 140,
      render: (value) => {
        return h(
            NImage,
            {
              width: 140,
              // height: 40,
              src: value.game_cover
            }
        )
      }
    },
    {
      title: "商品号",
      key: "id"
    },
    {
      title: "游戏名称",
      key: "game_name",
      sortOrder: false,
      sorter: 'default',
    },
    {
      title: "CDKey",
      key: "cd_key"
    },
    {
      title: "价格",
      key: "price"
    },
    {
      title: "商品详情",
      key: "decription",
      render(row) {
        return h(
            NEllipsis,
            {
              style:{
                maxWidth:"200px"
              }
            },
            {default:()=>row.decription}
        )
      }
    },
    {
      title: "操作",
      key: "actions",

      render(row) {
        return h("div", [
          h(
              NButton,
              {
                size: "small",
                onClick: () => edit(row),
                style: "margin-right:20px"
              },
              { default: () => "编辑" },
          ),
              h (
                  NButton,
                  {
                    size: "small",
                    type: "error",
                    ghost: true,
                    onClick: () => del(row),
                  },
                  { default: () => "删除" }
              )
        ]
        )
      }
    }
  ];
};

// 展示给访客的列表
const createColumnsForVistor = ({
                         purchase
                       }) => {
  return [
    {
      title: "",
      key: "game_cover",
      width: 140,
      render: (value) => {
        return h(
            NImage,
            {
              width: 140,
              // height: 40,
              src: value.game_cover
            }
        )
      }
    },
    {
      title: "商品号",
      key: "id"
    },
    {
      title: "游戏名称",
      key: "game_name",
      sortOrder: false,
      sorter: 'default',
    },
    {
      title: "CDKey",
      key: "cd_key"
    },
    {
      title: "价格",
      key: "price"
    },
    {
      title: "商品详情",
      key: "decription",
      render(row) {
        return h(
          NEllipsis,
            {
              style:{
                maxWidth:"200px"
              }
            },
            {default:()=>row.decripition}
        )
      }
    },
    {
      title: "购买",
      key: "actions",

      render(row) {
        return h("div", [
              h(
                  NButton,
                  {
                    size: "small",
                    onClick: () => purchase(row),
                    style: "margin-right:20px"
                  },
                  { default: () => "购买" },
              )
            ]
        )
      }
    }
  ];
};

export default {
  name: "SellerGoods",
  components:{AddGood,EditGood},

  setup () {
    let tableData = ref([])
    const load = () => {
      request.post("/getGoods/",JSON.stringify({'seller_id':router.currentRoute.value.params.username,'status':'已上架'})).then(res=>{
        // console.log(res)
        tableData.value = res.data
      })
    }
    onBeforeMount(()=>{
      load()
    })
    const filterTableData = computed(() =>
        tableData.value.filter(
            (data) =>
                !search.value ||
                data.game_name.toLowerCase().includes(search.value.toLowerCase())
                || data.cd_key === search.value ||
                data.id  === search.value - 0

        )
    )
    const addGoods = computed(()=>{
      return store.state.addGoodsVisible;
    })

    const editGoods = computed(()=>{
      return store.state.editGoodsVisible;
    })

    watch(addGoods,(newVal) => {
      if (newVal.valueOf() === false) {
        load()
      }
    })

    watch(editGoods,(newVal) => {
      // console.log('我在load啊')
      if (newVal.valueOf() === false) {
        load()
      }
    })

    const formRef = ref(null);
    const tableRef = ref(null)
    const checkedRowKeysRef = ref([]);
    let columnsRef = ref(createColumns(
        {
          edit(rowData) {
            store.state.editGoodsVisible = true;
            store.state.good.goodId = rowData.id;
            store.state.good.intro = rowData.decription;
            store.state.good.CDKey = rowData.cd_key;
            store.state.good.name = rowData.game_name;
            store.state.good.steamId = rowData.steam_id;
            store.state.good.money = rowData.price;
            // console.log("edit data " + rowData.name)
          },
          del(rowData) {
            dialog.warning({
              title: "确认删除",
              content: () => "是否确定删除商品",
              positiveText: "确定",
              onPositiveClick: () => {
                request.post("/delGoods/",JSON.stringify({'id':rowData.id})).then(res=>{
                  message.success(res.message)
                  load()
                })
              },
              negativeText: "取消"
            });
          }
        }
    ))
    const router = useRouter();
    const isSelf = ref(true);
    const notSelf = ref(false);
    const dialog = useDialog();
    const message = useMessage();
    if (parseInt(router.currentRoute.value.params.username) !== store.state.user.userID) {
      isSelf.value = false;
      notSelf.value = true;
      columnsRef = ref(createColumnsForVistor({
        purchase(rowData) {
          if (store.state.loggedIn === false) {
            dialog.warning({
              title: "请先登录",
              content: () => "请先登陆",
              positiveText: "确定",
              onPositiveClick: () => {
                router.push({name:'login'})
              },
              negativeText: "取消"
            })
            return;
          }
          dialog.warning({
            title: "确认购买",
            content: () => "是否确定购买该商品",
            positiveText: "确定",
            onPositiveClick: () => {
              request.post("/buyGoods/",JSON.stringify({'id':rowData.id,'buyer_id':store.state.user.userID})).then(res=>{
                message.success(res.messsage)
                load()
              })
            },
            negativeText: "取消"
          });
        }
      }))
    }
    return {
      store,
      isSelf,
      notSelf,
      rowKey: (row) => row.id,
      checkedRowKeys: checkedRowKeysRef,
      handleCheck(rowKeys) {
        checkedRowKeysRef.value = rowKeys;
      },
      table: tableRef,
      columns: columnsRef,
      filterTableData,
      search,
      pagination:
          {
            pageSize: 15,
            showQuickJumper:true,
          },
      handleSorterChange (sorter) {
        columnsRef.value.forEach((column) => {
          /** column.sortOrder !== undefined means it is uncontrolled */
          if (column.sortOrder === undefined) return
          if (!sorter) {
            column.sortOrder = false
            return
          }
          if (column.key === sorter.columnKey) column.sortOrder = sorter.order
          else column.sortOrder = false
        })
      },
      async beforeUpload(file) {
        let extension = file.name.substring(file.name.lastIndexOf('.')+1)
        let size = file.size / 1024 / 1024
        if(extension !== 'xlsx') {
          this.$message.warning('只能上传后缀是.xlsx的文件')
        }
        if(size > 10) {
          this.$message.warning('文件大小不得超过10M')
        }
      },
      handleAdd() {
        store.state.addGoodsVisible = true
      },
      delAll() {
        dialog.warning({
          title: "确认删除",
          content: () => "是否确定删除商品",
          positiveText: "确定",
          onPositiveClick: () => {
            request.post("/delGoods/",JSON.stringify({'id':checkedRowKeysRef.value})).then(res=>{
              message.success(res.message)
              load()
            })
          },
          negativeText: "取消"
        });

      },
      formRef,
      CloseCircleOutline,
      size: ref("medium"),
    }
  },
}
</script>

<style scoped>
.operate {
  float: left;
  margin-right: 10px;
}

.goodCard {
  position: absolute;
  top: 10px;
  left: 0;
  right: 0;
  margin-right: auto;
  margin-left: auto;
}

.header {
  margin-top: 31px;
  margin-bottom: 9px;
  min-height: 40px
}
</style>