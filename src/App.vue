<template>
  <Header></Header>
  <RegisterLoginPage/>
</template>

<script>
import Header from "@/components/Header";
import RegisterLoginPage from "@/components/RegisterLoginPage";

export default {
  name: 'App',
  components: {
    RegisterLoginPage,
    Header
  }
}
</script>

<style>
</style>
