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
import { h,ref,computed } from "vue";
import {NButton, NImage, useDialog,useMessage,NEllipsis} from "naive-ui";
import store from "../store"
import AddGood from "@/components/AddGood";
import EditGood from "@/components/EditGood";
import {useRouter,RouterLink} from "vue-router";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";

const search = ref('')
const filterTableData = computed(() =>
    tableData.filter(
        (data) =>
            !search.value || data.goodId === search.value - 0 ||
            data.name.toLowerCase().includes(search.value.toLowerCase())
    )
)


const tableData = [
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    goodId: 1253,
    name: 'Sekiro',
    CDKey: '123456',
    value: 20.5,
    steamId: 'kazeya',
    intro: '一个CDKEYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY',
    sellerId: 'Kazeya'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    goodId: 1233,
    name: 'Sekiro',
    CDKey: '1234156',
    value: 20.5,
    steamId: 'kazeya',
    intro: '一个CDKEY',
    sellerId: 'Kazeya'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    goodId: 1213,
    name: 'Sekiro',
    CDKey: '12123456',
    value: 20.5,
    steamId: 'kazeya',
    intro: '一个CDKEY',
    sellerId: 'Kazeya'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    goodId: 1423,
    name: 'Sekiro',
    CDKey: '12413456',
    value: 20.5,
    steamId: 'kazeya',
    intro: '一个CDKEY',
    sellerId: 'Kazeya'
  },
]

// 用户本人的列表
const createColumns = ({
                         edit,purchase
                       }) => {
  return [
    {
      title: "",
      key: "icon",
      width: 140,
      render: (value) => {
        return h(
            NImage,
            {
              width: 140,
              // height: 40,
              src: value.img
            }
        )
      }
    },
    {
      title: "商品号",
      key: "goodId"
    },
    {
      title: "商家昵称",
      key: "name",
      sortOrder: false,
      sorter: 'default',
      render(row) {
        return h(
            RouterLink,
            {
              to: {
                name: 'Info_v',
                params: {
                  username: row.sellerId
                },
              },
              style: {
                color: "black",
                textDecoration: "none",
              }
            },
            {
              default: () => row.name
            }
        )
      }
    },
    {
      title: "CDKey",
      key: "CDKey"
    },
    {
      title: "价格",
      key: "value"
    },
    {
      title: "商品详情",
      key: "intro",
      render(row) {
        return h(
            NEllipsis,
            {
              style:{
                maxWidth:"200px"
              }
            },
            {default:()=>row.intro}
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
  components:{AddGood,EditGood},

  setup () {
    const dialog = useDialog();
    const message = useMessage();
    const canEdit = ref(true)
    const formRef = ref(null);
    const tableRef = ref(null)
    const checkedRowKeysRef = ref([]);
    let columnsRef = ref(createColumns(
        {
          edit(rowData) {
            store.state.editGoodsVisible = true;
            store.state.good.goodId = rowData.goodId;
            store.state.good.intro = rowData.intro;
            store.state.good.CDKey = rowData.CDKey;
            store.state.good.name = rowData.name;
            store.state.good.steamId = rowData.steamId;
            store.state.good.money = rowData.value;
            // console.log("edit data " + rowData.name)
          },
          purchase(rowData) {
            dialog.warning({
              title: "确认购买",
              content: () => "是否确定购买该商品",
              positiveText: "确定",
              onPositiveClick: () => {
                // todo 向后端申请更改订单状态
                console.log(rowData.goodId);
                if (/* 成功删除 */true) {
                  message.success("购买成功");
                }
                else {
                  message.error("购买失败");
                }
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