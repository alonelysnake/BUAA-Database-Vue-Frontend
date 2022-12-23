<template>
  <div style="min-height: 300px">
    <n-grid :cols="2" x-gap="10px" y-gap="10">

      <!--  国家地区-->
      <n-grid-item class="left">
        <!--      国家/地区-->
        <n-select
            placeholder="国家/地区"
            v-model:label="districtLabel"
            v-model:value="districtValue"
            :options="districtOptions"/>
      </n-grid-item>

      <!--  优惠比例-->
      <n-grid-item class="right">
        <n-text>折扣比例：≤{{ discountThreshold }}%</n-text>
        <n-slider v-model:value="discountThreshold" :step="5"/>
      </n-grid-item>

      <!--    发行商-->
      <n-grid-item class="left">
        <!--      开发商-->
        <n-select
            placeholder="开发商"
            v-model:label="publishLabel"
            v-model:value="publishValue"
            :options="publishOptions"
            clearable/>
      </n-grid-item>

      <!--  发售时间-->
      <n-grid-item class="right">
        <n-space>
          发售时间
          <n-date-picker v-model:value="timeRange" type="daterange" clearable/>
        </n-space>
      </n-grid-item>

      <!--  优惠类型-->
      <n-grid-item class="left">
        <n-select
            placeholder="优惠类型"
            v-model:label="discountLabel"
            v-model:value="discountValue"
            :options="discountOptions"/>
      </n-grid-item>

    </n-grid>

    <n-button type="success" :loading="loading" @click="handleFilter">
      搜索
    </n-button>
  </div>


</template>

<script>
import {onMounted, ref} from "vue";
import request from "@/utils/request";

export default {
  name: "Filter",
  setup(props, {emit}) {
    const loading = ref(false);

    const districtLabel = ref();
    const districtValue = ref();
    const districtOptions = ref([]);

    const publishLabel = ref(null);
    const publishValue = ref(null);
    const publishOptions = ref([]);

    const discountLabel = ref("最新优惠");
    const discountValue = ref("0");
    const discountOptions = ref([
      {
        label: "最新优惠",
        value: "0"
      },
    ]);

    const timeRange = ref(null);
    const discountThreshold = ref(50);

    onMounted(() => {
      //获取所有国家
      request.post("/getCountry/", JSON.stringify({})).then(res => {
        districtOptions.value = res.data;
        districtValue.value = res.data[0].value;
        //获取所有开发商
        request.post("/getDeveloper/", JSON.stringify({})).then(res => {
          publishOptions.value = res.data;
          //获取优惠
          request.post("/getDiscount/", JSON.stringify({})).then(res => {
            // console.log(res.data);
            for (let i = 0; i < res.data.length; i++) {
              discountOptions.value.push(res.data[i]);
            }
            // 全部处理完成后初始化表格
            handleFilter();
          })
        })
      })
    })

    function handleFilter() {
      // 筛选重新搜索
      loading.value = true;
      let start_date = null, end_date = null;
      if (timeRange.value !== null) {
        start_date = timeRange.value[0];
        end_date = timeRange.value[1];
      }
      console.log(districtValue.value);
      const conds = {
        country_id: districtValue.value,//国家限制
        developer_id: publishValue.value,//供应商限制
        discount_id: discountValue.value,//优惠种类限制
        discount_rate: discountThreshold.value,//减免比例限制
        start_date: start_date,//时间限制，单位为毫秒
        end_date: end_date,//时间限制，单位为毫秒
        loading: loading,
      }
      // console.log(timeRange.value);
      // console.log(conds);
      emit("handleFilter", conds);
    }

    return {
      //可选择的国家地区
      districtLabel,
      districtValue,
      districtOptions,

      //开发商
      publishLabel,
      publishValue,
      publishOptions,

      //优惠类型
      discountLabel,
      discountValue,
      discountOptions,

      timeRange,//优惠时间
      discountThreshold,//优惠比例

      loading: loading,

      handleFilter,
    }
  }
}
</script>

<style scoped>
.right {
  margin-left: 50px;
}

.left {
  margin-bottom: 30px;
}
</style>