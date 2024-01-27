<template>
  <div id="app" :class="themeClass">
    <Search />
    <router-view></router-view>

  </div>
</template>

<script>
import Search from '@/views/search';

export default {
  name: 'App',
  components: {
    Search
  },
  computed: {
    themeClass() {
      return "theme" + this.$store.state.theme.currentThemeIndex
    }
  }
}
</script>

<style scoped></style>
