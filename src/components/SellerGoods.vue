<template>
  <div style="margin: 10px 0;">
    <div style="position: absolute;left: 200px">
      <n-button type="primary" ghost style="margin-right: 10px;">批量删除</n-button>
    </div>
    <div style="position:absolute;left: 100px">
      <n-upload
          action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
          @before-upload="beforeUpload"
          style="display: inline"
      >
        <n-button type="primary" ghost style="margin-right: 10px;">批量导入</n-button>
      </n-upload>
    </div>
    <div>
      <n-button type="primary" ghost >添加商品</n-button>
    </div>
  </div>
  <n-space vertical :size="12" >
    <n-input v-model:value="search" placeholder="输入商品号或游戏名查询" style="width: 400px;"/>
    <n-data-table
        ref="table"
        :columns="columns"
        :data="filterTableData"
        :pagination="pagination"
        striped
        @update:sorter="handleSorterChange"
    >
    </n-data-table>
  </n-space>
</template>

<!--todo 编辑/删除操作、从后端获得数据、测试数据上传-->

<script>
import { h,ref,computed } from "vue";
import { NButton } from "naive-ui";

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
    goodId: '1233',
    name: 'Sekiro',
    CDKey: '123456',
    value: 20.5,
  },
  {
    goodId: '1233',
    name: 'Sekiro',
    CDKey: '1234156',
    value: 20.5,
  },
  {
    goodId: '1213',
    name: 'Sekiro',
    CDKey: '12123456',
    value: 20.5,
  },
  {
    goodId: '1423',
    name: 'Sekiro',
    CDKey: '12413456',
    value: 20.5,
  },
]

const createColumns = ({
                         edit,del
                       }) => {
  return [
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


export default {
  name: "SellerGoods",

  setup () {
    const tableRef = ref(null)
    const columnsRef = ref(createColumns(
        {
          edit(rowData) {
            console.log("edit data " + rowData.name)
          },
          del(rowData) {
            console.log("delete data " + rowData.name)
          }
        }
    ))
    return {
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
    }
  }

}
</script>

<style scoped>

</style>