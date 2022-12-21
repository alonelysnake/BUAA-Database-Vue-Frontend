<template>
  <div class="table" v-if="showChart">
    <Charts :ids="selectRef"/>
  </div>
  <div class="table">
    <HeatTable @changeChart="changeChart"/>
  </div>
</template>

<script>
import HeatTable from "@/components/HeatTable";
import Charts from "@/components/Charts";
import {nextTick, ref} from "vue";

export default {
  name: "HeatPage",
  components: {
    HeatTable,
    Charts,
  },
  setup() {
    const showChart = ref(false);
    const selectRef = ref([]);

    //TODO 更新对比图
    function changeChart(selects) {
      //selects为热度表中选择对比的游戏id  list
      showChart.value = false;
      selectRef.value = selects;
      //重新加载对比图
      nextTick(()=>{
        //设置查找的
        showChart.value = true;
      })
      console.log(selectRef.value);
    }

    return {
      showChart,
      changeChart,
      selectRef
    }
  }
}
</script>

<style scoped>
.table {
  padding: 50px 100px;
}
</style>