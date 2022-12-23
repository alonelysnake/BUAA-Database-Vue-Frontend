<template>
  <n-space vertical :size="12" style="width: 83%;">
    <div>
      <n-button type="primary" ghost style="margin-right: 20px" @click="delAll">批量删除</n-button>
      <n-input v-model:value="search" placeholder="输入订单号或游戏名查询" style="width: 400px;"/>
    </div>
        <n-data-table
        ref="table"
        :columns="columns"
        :data="filterTableData"
        :pagination="pagination"
        striped
        :row-props="rowProps"
        @update:sorter="handleSorterChange"
        :row-key="rowKey"
        @update:checked-row-keys="handleCheck"
    />

    <n-dropdown
        placement="bottom-start"
        trigger="manual"
        :x="x"
        :y="y"
        :options="options"
        :show="showDropdown"
        :on-clickoutside="onClickoutside"
        @select="handleSelect"
    />
  </n-space>

</template>

<!--todo 删除操作、从后端获得数据-->

<script>
import {h, ref, nextTick, computed, onBeforeMount} from "vue";
import {NImage,useDialog,useMessage} from "naive-ui";
import request from "@/utils/request";

const status = ref("");

const options = [
  {
    label: () => h("span", {style: { color: "black" } }, "确定发货"),
    key: "deliver",
  },
  {
    label: () => h("span", { style: { color: "black" } }, "确定退款"),
    key: "refund",
  },
  {
    label: () => h("span", { style: { color: "red" } }, "删除订单"),
    key: "delete",
  }
];

const columns = [
  {
    type: "selection",
    disabled(row) {
      return row.status !== "交易成功" && row.status !== "已取消";
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
    title: "订单号",
    key: "id"
  },
  {
    title: "游戏名称",
    key: "game_name",
    sortOrder: false,
    sorter: 'default'
  },
  // {
  //   title: "用户购买时间",
  //   key: "date",
  //   sortOrder: 'descend',
  //   sorter: 'default'
  // },
  {
    title: "订单金额",
    key: "price"
  },
  {
    title: "买家ID",
    key: "buyer_id"
  },
  {
    title: "交易状态",
    key: "status",
    defaultFilterOptionValues: ['已付款','待退款'],
    filterOptions: [
      {
        label: '待付款',
        value: '待付款'
      },
      {
        label: '已付款',
        value: '已付款'
      },
      {
        label: '已发货',
        value: '已发货'
      },
      {
        label: '交易成功',
        value: '交易成功'
      },
      {
        label: '已取消',
        value: '已取消'
      },
      {
        label: '待退款',
        value: '待退款'
      },
      {
        label: '已收货',
        value: '已收货',
      }
    ],
    filter (value, row) {
      return ~row.status.indexOf(value)
    }
  }
]

import store from "@/store";
const search = ref('')


const orderId = ref(-1);

let tableData = ref([])
const load = () => {
  request.post("/getGoods/",JSON.stringify({'seller_id':store.state.user.userID})).then(res=>{
    tableData.value = res.data
    // console.log(tableData.value)
  })
}


export default ({
  name:"SellerOrder",

  setup () {
    onBeforeMount(()=>{
      load()
    })

    const filterTableData = computed(() =>
        tableData.value.filter(
            (data) =>
                search.value === '' ||
                data.game_name.toLowerCase().includes(search.value.toLowerCase())
                || data.id === parseInt(search.value)
        )
    )

    const checkedRowKeysRef = ref([]);
    const showDropdownRef = ref(false);
    const tableRef = ref(null)
    const columnsRef = ref(columns)
    const xRef = ref(0);
    const yRef = ref(0);
    const dialog = useDialog();
    const message = useMessage();
    return {
      rowKey: (row) => row.id,
      checkedRowKeys: checkedRowKeysRef,
      handleCheck(rowKeys) {
        checkedRowKeysRef.value = rowKeys;
      },

      table: tableRef,
      filterTableData,
      columns: columnsRef,
      options,
      x: xRef,
      y: yRef,
      search,
      showDropdown: showDropdownRef,
      pagination:
          {
            pageSize: 5,
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

      handleSelect(key) {
        showDropdownRef.value = false;
        if (key === "deliver") {
          switch (status.value) {
            case "已付款":
              dialog.warning({
                title: "确认发货",
                content: () => "请确保您已经发货",
                positiveText: "确定",

                onPositiveClick: () => {
                  request.post("/updateGoods/",JSON.stringify({'id':orderId.value,'type':'status','content':'已发货'})).then(res=>{
                    if (res.messsage === '修改商品信息成功') {
                      message.success("发货成功");
                      load()
                    }
                    else {
                      message.error("发货失败");
                    }
                  })
                },
                negativeText: "取消"
              });
              break;
            case "待付款":
              message.error("客户尚未付款");
              break;
            case "待退款":
              message.error("客户已申请退款");
              break;
            case "已取消":
              message.error("交易已取消");
              break;
            default:
              message.error("您已发货");
              break;
          }
        }
        else if (key === "refund") {
          if (status.value === "待退款") {
            dialog.warning({
              title: "确认退款",
              content: () => "是否确定取消交易并退款",
              positiveText: "确定",
              onPositiveClick: () => {
                request.post("/updateGoods/",JSON.stringify({'id':orderId.value,'type':'status','content':'已取消'})).then(res=>{
                  if (res.messsage === '修改商品信息成功') {
                    message.success("退款成功，交易取消");
                    load()
                  }
                  else {
                    message.error("退款失败");
                  }
                })
              },
              negativeText: "取消"
            });
          }
          else {
            message.error("用户未发起退款");
          }
        }
        else {
          if (status.value === "已取消" || status.value === "交易成功") {
            dialog.warning({
              title: "确认删除订单",
              content: () => "是否确定删除已完成的交易订单",
              positiveText: "确定",
              onPositiveClick: () => {
                request.post("/delGoods/",JSON.stringify({'id':orderId.value})).then(res=>{
                  if (res.message === '删除商品成功') {
                    message.success("删除成功");
                    load()
                  }
                  else {
                    message.error("删除失败");
                  }
                })
              },
              negativeText: "取消"
            });
          }
          else {
            message.error("请完成交易后再删除订单");
          }
        }
      },
      onClickoutside() {
        showDropdownRef.value = false;
      },

      delAll() {
        dialog.warning({
          title: "确认删除订单",
          content: () => "是否确定删除已完成的交易订单",
          positiveText: "确定",
          onPositiveClick: () => {
            request.post("/delGoods/",JSON.stringify({'id':checkedRowKeysRef.value})).then(res=>{
              if (res.message === '删除商品成功') {
                message.success("删除成功");
                load()
              }
              else {
                message.error("删除失败");
              }
            })
          },
          negativeText: "取消"
        });
      },

      rowProps: (row) => {
        return {
          onContextmenu: (e) => {
            e.preventDefault();
            showDropdownRef.value = false;
            nextTick().then(() => {
              showDropdownRef.value = true;
              status.value = row.status
              orderId.value = row.id
              xRef.value = e.clientX;
              yRef.value = e.clientY;
            });
          }
        };
      }
    }
  }
});
</script>