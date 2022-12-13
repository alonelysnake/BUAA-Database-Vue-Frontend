<template>
  <div class="header"
       v-if="isSelf.valueOf()">

    <div class="operate">
      <n-button type="primary" ghost style="height: 35px">批量删除</n-button>
    </div>
    <div class="operate">
      <n-upload
          action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
          @before-upload="beforeUpload"
          style="display: inline"
      >
        <n-button type="primary" ghost style="height: 35px">批量导入</n-button>
      </n-upload>
    </div>
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
    />
  </n-space>

</template>

<!--todo 编辑/删除操作、从后端获得数据、测试数据上传-->

<script>
import { h,ref,computed } from "vue";
import {NButton, NImage, useDialog,useMessage,NEllipsis} from "naive-ui";
import store from "../store"
import AddGood from "@/components/AddGood";
import EditGood from "@/components/EditGood";
import {useRouter} from "vue-router";
import {
  CloseCircleOutline,
} from "@vicons/ionicons5";

const search = ref('')
const filterTableData = computed(() =>
    tableData.filter(
        (data) =>
            !search.value ||
            data.name.toLowerCase().includes(search.value.toLowerCase())
            || data.CDKey === search.value ||
            data.goodId === search.value

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
    intro: '一个CDKEYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    goodId: 1233,
    name: 'Sekiro',
    CDKey: '1234156',
    value: 20.5,
    steamId: 'kazeya',
    intro: '一个CDKEY'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    goodId: 1213,
    name: 'Sekiro',
    CDKey: '12123456',
    value: 20.5,
    steamId: 'kazeya',
    intro: '一个CDKEY'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    goodId: 1423,
    name: 'Sekiro',
    CDKey: '12413456',
    value: 20.5,
    steamId: 'kazeya',
    intro: '一个CDKEY'
  },
]

// 用户本人的列表
const createColumns = ({
                         edit,del
                       }) => {
  return [
    {
      type: "selection",
      disabled(row) {
        return false;
      }
    },
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
      title: "游戏名称",
      key: "name",
      sortOrder: false,
      sorter: 'default',
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
      title: "游戏名称",
      key: "name",
      sortOrder: false,
      sorter: 'default',
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
    const formRef = ref(null);
    const tableRef = ref(null)
    const checkedRowKeysRef = ref([]);
    let columnsRef = ref(createColumns(
        {
          edit(rowData) {
            // todo 根据行的信息传递参数
            store.state.editGoodsVisible = true;
            store.state.good.goodId = rowData.goodId;
            store.state.good.intro = rowData.intro;
            store.state.good.CDKey = rowData.CDKey;
            store.state.good.name = rowData.name;
            store.state.good.steamId = rowData.steamId;
            store.state.good.money = rowData.value
            // console.log("edit data " + rowData.name)
          },
          del(rowData) {
            // todo 向后端回传
            console.log("delete data " + rowData.name)
          }
        }
    ))
    const router = useRouter();
    const isSelf = ref(true);
    const notSelf = ref(false);
    const dialog = useDialog();
    const message = useMessage();
    if (router.currentRoute.value.params.username !== store.state.user.userID) {
      isSelf.value = false;
      notSelf.value = true;
      columnsRef = ref(createColumnsForVistor({
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
      }))
    }
    return {
      store,
      isSelf,
      notSelf,
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