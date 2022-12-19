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
  key: 'country_name',
  sortOrder: false,//表示是否排序
  sorter: 'default'//排序方式
}

const originPriceColumn = {
  title: '原价',
  key: 'original_price',
  sortOrder: false,
  sorter(rowA, rowB) {
    return rowA.original_price - rowB.original_price//自定义的排序函数
  }
}

const curPriceColumn = {
  title: '当前价格',
  key: 'current_price',
  sortOrder: false,
  sorter(rowA, rowB) {
    return rowA.current_price - rowB.current_price
  }
}

const lowestPriceColumn = {
  title: '历史最低价格',
  key: 'lowest_price',
  sortOrder: false,
  sorter(rowA, rowB) {
    return rowA.lowest_price - rowB.lowest_price
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

export default {
  name: "CountryPriceTable",
  setup() {
    const nameColumnReactive = reactive(nameColumn)
    const originColumnReactive = reactive(originPriceColumn)
    const curColumnReactive = reactive(curPriceColumn)
    const lowestColumnReactive = reactive(lowestPriceColumn)
    const columnsRef = ref(columns)
    const router = useRouter();

    //从后端读取的数据格式
    let data = ref([]);

    const gameId = parseInt(router.currentRoute.value.params.gameid);//游戏id

    //TODO 后端获取每个国家的价格
    onMounted(() => {
      request.post('/getPrice/', JSON.stringify({'game_id': gameId})).then(res => {
        console.log("gg");
        console.log(res.data);
        console.log("gg");
        data.value = res.data;
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