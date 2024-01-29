<template>
  <div id="app">
    <Search />
    <router-view></router-view>
  </div>
</template>

<script>
import Search from '@/global/Search.vue';

export default {
  name: 'App',
  components: {
    Search
  },

}
</script>

<style scoped></style>
