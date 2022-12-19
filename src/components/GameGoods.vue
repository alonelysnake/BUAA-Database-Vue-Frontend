<template>
  <n-space vertical :size="12" style="width: 83%;position:relative;">
    <n-input v-model:value="search"
             placeholder="输入商品号或商家名查询"
             style="
             width: 400px;
             height: 35px;
             margin: 15px;
             top: 5px"
    />
<!--    <n-button class="operate" type="primary" ghost style="height: 35px" @click="handleAdd">添加商品</n-button>-->
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
<!--    <AddGood-->
<!--        class="goodCard"-->
<!--        v-if="store.state.addGoodsVisible"-->
<!--        :regular=true-->
<!--    >-->
<!--    </AddGood>-->
<!--    <EditGood-->
<!--        class="goodCard"-->
<!--        v-if="store.state.editGoodsVisible"-->
<!--        title="商品详情"-->
<!--        :edit="canEdit.valueOf()"-->
<!--    />-->
  </n-space>

</template>

<!--todo 编辑/删除操作、从后端获得数据、测试数据上传-->

<script>
import {h, ref, computed, onBeforeMount} from "vue";
import {NButton, NImage, useDialog,useMessage,NEllipsis} from "naive-ui";
import store from "../store"
import {useRouter,RouterLink} from "vue-router";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";
import request from "@/utils/request";


const search = ref('')

// 用户本人的列表
const createColumns = ({
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
      title: "商家昵称",
      key: "seller_name",
      sortOrder: false,
      sorter: 'default',
      render(row) {
        return h(
            RouterLink,
            {
              to: {
                name: 'Info_v',
                params: {
                  username: row.seller_name
                },
              },
              style: {
                color: "black",
                textDecoration: "none",
              }
            },
            {
              default: () => row.seller_name
            }
        )
      }
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
              // h(
              //     NButton,
              //     {
              //       size: "small",
              //       onClick: () => edit(row),
              //       style: "margin-right:20px"
              //     },
              //     { default: () => "查看详情" },
              // ),
              h(
                  NButton,
                  {
                    size: "small",
                    type: "primary",
                    ghost: "true",
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
  name: "GameGoods",

  setup () {
    let tableData = ref([])
    const load = () => {
      request.post("/getGoods/",JSON.stringify({'game_id':router.currentRoute.value.params.gameid,'status':'已上架'})).then(res=>{
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
                !search.value || data.id === search.value - 0 ||
                data.seller_name.toLowerCase().includes(search.value.toLowerCase())
        )
    )
    const router = useRouter();
    const dialog = useDialog();
    const message = useMessage();
    const canEdit = ref(true)
    const formRef = ref(null);
    const tableRef = ref(null)
    const checkedRowKeysRef = ref([]);
    let columnsRef = ref(createColumns(
        {
          purchase(rowData) {
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
        }
    ))

    return {
      canEdit,
      store,
      rowKey: (row) => row.goodId,
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

      handleAdd() {
        store.state.addGoodsVisible = true
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
  float: right;
  margin-right: 10px;
}

.goodCard {
  position: absolute;
  top: 50px;
  left: 0;
  right: 0;
  margin-right: auto;
  margin-left: auto;
}
</style>