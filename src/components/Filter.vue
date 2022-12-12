<template>

  <n-grid :cols="2" x-gap="10px" y-gap="10">

    <!--  国家地区-->
    <n-grid-item>
      <!--      国家/地区-->
      <n-select placeholder="国家/地区" v-model:value="districtValue" :options="districtOptions"/>
    </n-grid-item>

    <!--  优惠比例-->
    <n-grid-item>
      <n-text>折扣比例：≥{{discountThreshold}}%</n-text>
      <n-slider v-model:value="discountThreshold" :step="5"/>
    </n-grid-item>

    <!--    发行商-->
    <n-grid-item>
      <!--      开发商-->
      <n-select placeholder="开发商" v-model:value="publishValue" :options="publishOptions"/>
    </n-grid-item>

    <!--  发售时间-->
    <n-grid-item>
      <n-space>
        发售时间
        <n-date-picker v-model:value="timeRange" type="daterange" clearable/>
      </n-space>
    </n-grid-item>

    <!--  优惠类型-->
    <n-grid-item>
      <n-select placeholder="优惠类型" v-model:value="discountValue" :options="discountOptions"/>
    </n-grid-item>

  </n-grid>

  <n-button type="success" :loading="loading" @click="handleFilter">
    搜索
  </n-button>

</template>

<script>
import {ref} from "vue";

export default {
  name: "Filter",
  setup() {
    const loading = ref(false);
    return {
      //可选择的国家地区
      districtValue: ref(null),
      districtOptions: [
        {
          label: "中国",
          value: "China"
        },
        {
          label: "日本",
          value: "Japan"
        },
        {
          label: "韩国",
          value: "Korea"
        },
        {
          label: "美国",
          value: "America"
        }
      ],

      publishValue: ref(null),
      publishOptions: [
        {
          label: "米哈游",
          value: "mihoyo"
        },
        {
          label: "卡普空",
          value: "Japan"
        },
        {
          label: "暴雪",
          value: "Blizzard"
        },
        {
          label: "EA",
          value: "EA"
        },
        {
          label: "育碧",
          value: "Ubisoft"
        }
      ],

      discountValue: ref("default"),
      discountOptions: [
        {
          label: "最新优惠",
          value: "default"
        },
        {
          label: "冬促",
          value: "winter"
        },
        {
          label: "春促",
          value: "spring"
        },
        {
          label: "夏促",
          value: "summer"
        },
        {
          label: "秋促",
          value: "autumn"
        }
      ],

      timeRange: ref([118313526e4, Date.now()]),
      discountThreshold: ref(50),

      loading:loading,
      handleFilter(){
        //TODO 筛选后重新搜索
        loading.value = true;
        setTimeout(() => {
          loading.value = false;
        }, 2e3);
      }
    }
  }
}
</script>

<style scoped>

</style>