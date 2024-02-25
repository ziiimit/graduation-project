<template>
    <div id="theme">
        <SearchInput />
        <ThemeList ref="themeList" />
    </div>
</template>
<script>
import ThemeList from "./components/ThemeList.vue";
import SearchInput from "./components/SearchInput.vue"
export default {
    name: "Theme",
    components: { ThemeList, SearchInput },
}
</script>
<style scoped lang='scss'>
#theme {
    position: relative;
    padding-top: 50px;
    height: 100vh;
}

#theme-list {
    margin-top: 180px;
}
</style>
