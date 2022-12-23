<template>
  <div style="height: 40px">
    <n-space>
      <n-select
          style="width: 100px"
          v-if="showSelect"
          placeholder="国家/地区"
          v-model:label="districtLabel"
          v-model:value="districtValue"
          :options="districtOptions"
          @update:value="updateChart"/>

      <n-select
          style="width: 100px"
          v-if="showSelect"
          placeholder="国家/地区"
          v-model:label="timeLabel"
          v-model:value="timeValue"
          :options="timeOptions"
          @update:value="updateChart"/>
    </n-space>
  </div>

  <!--  <n-space vertical>-->
  <!--价格波动-->
  <div class="chart-style" ref="priceChartRef"/>
  <!--人数波动-->
  <div class="chart-style" ref="activeChartRef"/>
  <!--  </n-space>-->
</template>

<script>
import {onMounted, ref} from "vue";
import * as echarts from "echarts";
import request from "@/utils/request";
import {useRouter} from "vue-router";

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
    let myEcharts1
    let myEcharts2

    const priceData = {
      title: {
        text: '价格波动图'
      },
      tooltip: {},
      legend: {//游戏名列表
        data: []
      },
      xAxis: {
        type: 'time',
      },
      yAxis: {
        // type: 'value'
      },
      series: [
        //如果有多个游戏，则此处为多个
      ]
    }
    const activeData = {
      title: {
        text: '人数波动图'
      },
      tooltip: {},
      legend: {//游戏名列表
        data: [/*'a'*/]
      },
      xAxis: {
        type: 'time',
      },
      yAxis: {
        // type: 'value'
      },
      series: [
        // {
        //   name: 'genshin',
        //   data: [
        //     {value: ['1997-10-1', 150]},
        //     {value: ['1998-10-1', 150]},
        //   ],
        //   type: 'line'
        // },
      ]
    }

    //选择国家地区
    const showSelect = ref(true);
    const districtValue = ref();//选择的国家id
    const districtLabel = ref();//选择的国家name
    const districtOptions = ref([]);

    const timeValue = ref("all");//选择的国家id
    const timeLabel = ref("所有");//选择的国家name
    const timeOptions = ref([
      {
        label: "所有",
        value: "all",
      },
      {
        label: "近一年",
        value: "year",
      },
      {
        label: "近一月",
        value: "month",
      },
      {
        label: "近一周",
        value: "week",
      },
    ]);

    const router = useRouter();

    let ids;//参与展示的所有游戏

    onMounted(() => {
      myEcharts1 = echarts.init(priceChartRef.value)
      myEcharts2 = echarts.init(activeChartRef.value)
      ids = prop.ids;//所有要展示的游戏的编号
      if (ids.length === 0) {
        ids = [parseInt(router.currentRoute.value.params.gameid)];
      }
      // 读取游戏名
      for (let i = 0; i < ids.length; i++) {
        request.post('/getGame/', JSON.stringify({'game_id': ids[i]})).then(res => {
          priceData.legend.data.push(res.data[0].name);
          activeData.legend.data.push(res.data[0].name);
        })
      }
      //读取可选国家
      request.post("/getCountry/", JSON.stringify({})).then(res => {
        // console.log(res.data);
        districtOptions.value = res.data;

        districtValue.value = districtOptions.value[0].value;
        districtLabel.value = districtOptions.value[0].label;//展示的游戏的国家编号(如果没有怎么办?)

        initPriceChart();
        initActiveChart();
      })
    })

    function initPriceChart() {
      //初始化价格图
      // const myEcharts1 = echarts.init(priceChartRef.value)//TODO 考虑移到onMount?
      while (priceData.series.length !== 0) {
        priceData.series.pop();
      }
      let timeType = timeValue.value;
      if (timeType === 'all') {
        timeType = null;
      }
      for (let i = 0; i < ids.length; i++) {
        request.post('/getPrice/', JSON.stringify({
          'game_id': ids[i],
          'country': districtValue.value,
          'time': timeType
        })).then(res => {
          console.log(res.data);
          priceData.series.push({
            name: priceData.legend.data[i],
            data: res.data,
            type: 'line'
          });
        })
      }
      setTimeout(() => {
        myEcharts1.setOption(priceData);
      }, 500);
    }

    function initActiveChart() {
      //初始化热度图
      // const myEcharts2 = echarts.init(activeChartRef.value)
      while (activeData.series.length !== 0) {
        activeData.series.pop();
      }
      for (let i = 0; i < ids.length; i++) {
        let timeType = timeValue.value;
        if (timeType === 'all') {
          timeType = null;
        }
        request.post('/getHeat/', JSON.stringify({'game_id': ids[i], 'time': timeType})).then(res => {
          console.log(res.data);
          activeData.series.push({
            name: activeData.legend.data[i],
            data: res.data,
            type: 'line'
          });
        })
        setTimeout(() => {
          myEcharts2.setOption(activeData)
        }, 500);
      }
    }

    function updateChart() {
      initPriceChart();
      initActiveChart();
    }

    return {
      priceChartRef,
      activeChartRef,

      showSelect,
      districtLabel,
      districtValue,
      districtOptions,

      timeValue,
      timeLabel,
      timeOptions,

      updateChart,
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