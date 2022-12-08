<template>
  <!--  筛选器-->
  <div class="filter">
    <Filter/>
  </div>

  <!--经过筛选后的展示-->
  <div class="table">
    <FilterShowTable/>
  </div>

</template>

<script>
import Filter from "@/components/Filter";
import FilterShowTable from "@/components/FilterShowTable";

export default {
  name: "FilterPage",
  components: {
    Filter,
    FilterShowTable
  },
  setup() {

    return {}
  }
}
</script>

<style scoped>
.filter {
  padding: 100px 100px 0 100px;
  width: 600px;
}

.table {
  padding: 50px 100px;
}
</style>