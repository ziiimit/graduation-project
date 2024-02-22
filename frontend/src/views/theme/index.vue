<template>
    <div id="theme">
        <Transition name="fade">
            <ThemeList ref="themeList" @navigate="(title_en) => navigate(title_en)" v-if="showList" />
        </Transition>
        <router-view></router-view>
    </div>
</template>
<script>
import ThemeList from "./components/ThemeList.vue";
export default {
    name: "Theme",
    components: { ThemeList },
    data() {
        return {
            showList: true
        }
    },
    methods: {
        navigate(title_en) {
            let routeName
            switch (title_en) {
                case "Mental Health and Addiction":
                    routeName = "Theme_MentalHealthAndAddiction"
                    break;
                case "Focus, Productivity and Creativity":
                    routeName = "Theme_FocusProductivityAndCreativity"
                    break;
                case "The Science of Well-being":
                    routeName = "Theme_TheScienceOfWellBeing";
                    break;
                default:
                    routeName = "ThemeList"
            }
            this.showList = false
            this.$router.push({ name: routeName })
        }
    },
    created() {
        if (this.$route.name != "ThemeList") {
            this.showList = false;
        }
    },
    watch: {
        '$route.name': function (newVal) {
            if (newVal == "ThemeList") {
                this.showList = true
            }
        }
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/transition.scss";
</style>
