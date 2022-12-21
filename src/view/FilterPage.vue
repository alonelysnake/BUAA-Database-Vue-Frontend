<template>
  <!--  筛选器-->
  <n-card class="filter" hoverable>
    <Filter class="content" @handleFilter="handleFilter"/>
  </n-card>

  <!--经过筛选后的展示-->
  <div class="table">
    <FilterShowTable ref="tableRef"/>
  </div>

</template>

<script>
import Filter from "@/components/Filter";
import FilterShowTable from "@/components/FilterShowTable";
import {ref} from "vue";

export default {
  name: "FilterPage",
  components: {
    Filter,
    FilterShowTable
  },
  setup() {
    const tableRef = ref(null)

    function handleFilter(cond) {
      tableRef.value.handleFilter(cond);
    }

    return {
      tableRef,
      handleFilter,
    }
  }
}
</script>

<style scoped>
.filter {
  margin-left: 100px;
  margin-top: 30px;
  padding: 100px 100px;
  width: 800px;
  min-height: 300px;
  position: relative;
}

.content {
  position: absolute;
  top: 30px;
  right: 20px;
  left: 20px;
  margin: auto;
}

.table {
  padding: 20px 100px 50px;
}
</style>