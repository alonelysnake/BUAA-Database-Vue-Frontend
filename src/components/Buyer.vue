<template>
  <n-space vertical :size="12" >
    <n-input v-model:value="search" placeholder="输入订单号或游戏名查询" style="width: 400px;"/>
    <n-data-table
        ref="table"
        :columns="columns"
        :data="filterTableData"
        :pagination="pagination"
        striped
        :row-props="rowProps"
        @update:sorter="handleSorterChange"
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

const options = [
  {
    label: () => h("span", { style: { color: "red" } }, "删除"),
    key: "delete"
  }
];

const columns = [
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
      title: "购买时间",
      key: "date",
      sortOrder: 'descend',
      sorter: 'default'
    },
    {
      title: "订单金额",
      key: "value"
    },
    {
      title: "卖家ID",
      key: "sellerId"
    },
    {
      title: "交易状态",
      key: "status",
      defaultFilterOptionValues: ['待付款', '已付款','已发货','交易成功','已取消','待退款'],
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
      ],
      filter (value, row) {
        return ~row.status.indexOf(value)
      }
    }
  ]


const tableData = [
      {
        orderId: 1,
        name: 'Sekiro',
        date: '2016-05-02',
        value: 20.5,
        sellerId: 1,
        status: '已发货',
      },
      {
        orderId: 2,
        name: 'NieR',
        date: '2016-05-03',
        value: 22.5,
        sellerId: 2,
        status: '已发货'
      },
      {
        orderId: 3,
        name: 'Sekiro',
        date: '2016-04-05',
        value: 23.5,
        sellerId: 3,
        status: '交易成功'
      },
      {
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

export default ({
  name:"Buyer",

  setup () {
    const showDropdownRef = ref(false);
    const tableRef = ref(null)
    const columnsRef = ref(columns)
    const xRef = ref(0);
    const yRef = ref(0);
    return {
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

      handleSelect() {
        showDropdownRef.value = false;
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