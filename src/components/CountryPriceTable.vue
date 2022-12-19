<!--更改自naive-数据表格-受控的排序-->
<template>

  <n-space vertical :size="12">
    <!--TODO 如果需要分页，添加属性:pagination="pagination"-->
    <n-data-table
        :columns="columns"
        :data="data"
        striped
        @update:sorter="handleSorterChange"
    />
  </n-space>

</template>

<script>
import {reactive, ref, onMounted} from 'vue'
import request from "@/utils/request";
import {useRouter} from "vue-router/dist/vue-router";

const nameColumn = {
  title: '国家（地区）',
  key: 'name',
  sortOrder: false,//表示是否排序
  sorter: 'default'//排序方式
}

const originPriceColumn = {
  title: '原价',
  key: 'origin',
  sortOrder: false,
  sorter(rowA, rowB) {
    return rowA.origin - rowB.origin//自定义的排序函数
  }
}

const curPriceColumn = {
  title: '当前价格',
  key: 'curPrice',
  sortOrder: false,
  sorter(rowA, rowB) {
    return rowA.curPrice - rowB.curPrice
  }
}

const lowestPriceColumn = {
  title: '历史最低价格',
  key: 'lowest',
  sortOrder: false,
  sorter(rowA, rowB) {
    return rowA.lowest - rowB.lowest
  }
}

/*属性列
* 国家/地区名
* 原价
* 当前价格
* 最低价格
* */
const columns = [
  nameColumn,
  originPriceColumn,
  curPriceColumn,
  lowestPriceColumn
]

/*从后端读取的数据格式*/
let data = [
  {
    key: 0,
    name: 'China',
    origin: 99,
    curPrice: 38,
    lowest: 1
  },
  {
    key: 1,
    name: 'USA',
    origin: 108,
    curPrice: 42,
    lowest: 9
  },
  {
    key: 2,
    name: 'UK',
    origin: 105,
    curPrice: 36,
    lowest: '3'
  },
  {
    key: 3,
    name: 'Japan',
    origin: 648,
    curPrice: 32,
    lowest: '7'
  },
  {
    key: 4,
    name: 'Korea',
    origin: 328,
    curPrice: 32,
    lowest: '5'
  },
  {
    key: 5,
    name: 'Russia',
    origin: 98,
    curPrice: 32,
    lowest: '2'
  },
]

export default {
  name: "CountryPriceTable",
  setup() {
    const nameColumnReactive = reactive(nameColumn)
    const originColumnReactive = reactive(originPriceColumn)
    const curColumnReactive = reactive(curPriceColumn)
    const lowestColumnReactive = reactive(lowestPriceColumn)
    const columnsRef = ref(columns)
    const router = useRouter();

    const gameId = parseInt(router.currentRoute.value.params.gameid);//游戏id

    //TODO 后端获取每个国家的价格
    onMounted(() => {
      request.post('/getPrice/', JSON.stringify({'id': gameId})).then(res => {
        data = res.data;
      });
    })

    return {
      data,
      columns: columnsRef,
      nameColumn: nameColumnReactive,
      originColumn: originColumnReactive,
      curPriceColumn: curColumnReactive,
      lowestColumn: lowestColumnReactive,

      pagination: {pageSize: 5},/*TODO 每页的元素数量*/



      handleSorterChange(sorter) {
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
      }
    }
  }
}
</script>

<style scoped>

</style>