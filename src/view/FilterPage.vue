<template>
  <!--  筛选器-->
  <div class="filter">
    <Filter @handleFilter="handleFilter"/>
  </div>

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
  padding: 100px 100px 0 100px;
  width: 800px;
}

.table {
  padding: 50px 100px;
}
</style>