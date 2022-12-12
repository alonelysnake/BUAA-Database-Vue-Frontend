<template>
  <!--价格波动-->
  <div class="chart-style" ref="priceChartRef"/>
  <!--人数波动-->
  <div class="chart-style" ref="activeChartRef"/>
</template>

<script>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Charts",
  props: {
    ids: {
      default: [],
    },
  },
  setup(prop) {
    const priceChartRef = ref()
    const activeChartRef = ref()

    onMounted(() => {
      //TODO 后台同步获取数据
      console.log(prop.ids);
      const priceChart = getPriceHistory(prop.ids)
      const activeChart = getActiveHistory(prop.ids)

      const myEcharts1 = echarts.init(priceChartRef.value)
      myEcharts1.setOption(priceChart)

      const myEcharts2 = echarts.init(activeChartRef.value)
      myEcharts2.setOption(activeChart)
    })

    // 价格波动图
    function getPriceHistory(ids) {
      return {
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
          //如果有多个游戏，则此处为多个
          {
            name: '实际售价',
            data: [150, 230, 224, 218, 135, 147, 260],
            type: 'line'
          }
        ]
      }
    }

    // 活跃人数波动图
    function getActiveHistory(ids) {
      return {
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
          },
          {
            name: '在线',
            data: [30, 20, 24, 28, 13, 17, 60],
            type: 'line'
          }
        ]
      }
    }

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