<template>
  <n-space vertical :size="12" style="width: 83%;">
    <div>
      <n-button type="primary" ghost style="margin-right: 20px">批量删除</n-button>
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
import { h,ref,nextTick,computed } from "vue";
import {NImage,useDialog,useMessage} from "naive-ui";

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
    title: "订单号",
    key: "orderId"
  },
  {
    title: "游戏名称",
    key: "name",
    sortOrder: false,
    sorter: 'default'
  },
  {
    title: "用户购买时间",
    key: "date",
    sortOrder: 'descend',
    sorter: 'default'
  },
  {
    title: "订单金额",
    key: "value"
  },
  {
    title: "买家ID",
    key: "sellerId"
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


const tableData = [
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    orderId: 1,
    name: 'Sekiro',
    date: '2016-05-02',
    value: 20.5,
    sellerId: 1,
    status: '已发货',
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp4.itc.cn%2Fq_70%2Fimages03%2F20210622%2F3254befcfb29402297aefdd8a8944b95.jpeg&refer=http%3A%2F%2Fp4.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109495&t=872a11a71436ae2fa168921b78396785',
    orderId: 2,
    name: 'NieR',
    date: '2016-05-03',
    value: 22.5,
    sellerId: 2,
    status: '已发货'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    orderId: 3,
    name: 'Sekiro',
    date: '2016-04-05',
    value: 23.5,
    sellerId: 3,
    status: '交易成功'
  },
  {
    img: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F1b13137cddeb48b0b378108f1d8452a1c099959c.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1673109288&t=59aa2c866d7bce31c6d17d60aa101b17',
    orderId: 4,
    name: 'Sekiro',
    date: '2016-02-02',
    value: 26.5,
    sellerId: 1,
    status: '已付款'
  },
]

const search = ref('')
const filterTableData = computed(() =>
    tableData.filter(
        (data) =>
            !search.value ||
            data.name.toLowerCase().includes(search.value.toLowerCase())
            || data.orderId === parseInt(search.value)
    )
)

const orderId = ref(-1);

export default ({
  name:"SellerOrder",

  setup () {
    const checkedRowKeysRef = ref([]);
    const showDropdownRef = ref(false);
    const tableRef = ref(null)
    const columnsRef = ref(columns)
    const xRef = ref(0);
    const yRef = ref(0);
    const dialog = useDialog();
    const message = useMessage();
    return {
      rowKey: (row) => row.orderId,
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
                  // todo 向后端申请更改订单状态
                  console.log(orderId.value);
                  if (/* 成功删除 */true) {
                    message.success("发货成功");
                  }
                  else {
                    message.error("发货失败");
                  }
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
                // todo 向后端申请更改订单状态
                console.log(orderId.value);
                if (/* 成功退款 */true) {
                  message.success("退款成功，交易取消");
                }
                else {
                  message.error("退款失败");
                }
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
                // todo 向后端申请更改订单状态
                console.log(orderId.value);
                if (/* 成功删除 */true) {
                  message.success("删除成功");
                }
                else {
                  message.error("删除失败");
                }
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

      rowProps: (row) => {
        return {
          onContextmenu: (e) => {
            e.preventDefault();
            showDropdownRef.value = false;
            nextTick().then(() => {
              showDropdownRef.value = true;
              status.value = row.status
              orderId.value = row.orderId
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