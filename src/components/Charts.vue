<template>
  <!--价格波动-->
  <div class="chart-style" ref="priceChartRef"/>
  <!--人数波动-->
  <div class="chart-style" ref="activeChartRef"/>
</template>

<script>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

//TODO 变为后台获取数据
// 价格波动图
const priceChart = {
  title: {
    text: '价格波动图'
  },
  tooltip: {},
  legend: {//根据name决定展示顺序
    data: ['实际售价']
  },
  xAxis: {
    type: 'category',
    //TODO 日期
    data: ['Jan 2022', 'Feb 2022', 'Mar 2022', 'Apr 2022', 'May 2022', 'Jun 2022', 'Jul 2022']
  },
  yAxis: {
    // type: 'value'
  },
  series: [
    {
      name: '实际售价',
      data: [150, 230, 224, 218, 135, 147, 260],
      type: 'line'
    }
  ]
}
// 活跃人数波动图
const activeChart = {
  title: {
    text: '人数波动图'
  },
  tooltip: {},
  legend: {//根据name决定展示顺序
    data: ['在线人数']
  },
  xAxis: {
    type: 'category',
    //TODO 日期
    data: ['Jan 2022', 'Feb 2022', 'Mar 2022', 'Apr 2022', 'May 2022', 'Jun 2022', 'Jul 2022']
  },
  yAxis: {
    // type: 'value'
  },
  series: [
    {
      name: '在线人数',
      data: [150, 230, 224, 218, 135, 147, 260],
      type: 'line'
    }
  ]
}

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Charts",
  setup() {
    const priceChartRef = ref()
    const activeChartRef = ref()

    onMounted(() => {
      const myEcharts1 = echarts.init(priceChartRef.value)
      myEcharts1.setOption(priceChart)

      const myEcharts2 = echarts.init(activeChartRef.value)
      myEcharts2.setOption(activeChart)
    })

    return {
      priceChartRef,
      activeChartRef
    }
  }
}
</script>

<style scoped>
.chart-style {
  width: 100%;
  height: 500px;
  background-color: snow
}
</style>