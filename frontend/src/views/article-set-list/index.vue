<template>
    <div id="article-set-list" :class="[theme.colorTheme]">
        <button class="return-btn" @click="goBack">
            <img
                src="data:image/png;base64,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">
        </button>
        <div class="title-wrapper">
            <h1 class="title">{{ theme.themeName_zh }}</h1>
            <h2 class="sub-title">{{ theme.themeName_en }}</h2>
        </div>
        <List :theme="theme" />
    </div>
</template>
<script>
import List from './components/List.vue'
export default {
    name: "ArticleSetList",
    components: { List },
    computed: {
        theme() {
            let currentThemeName = this.$route.params['theme']
            for (let item of this.$store.state.theme.themes) {
                if (item['themeName_en'] == currentThemeName) return item
            }
        }
    },
    methods: {
        goBack() {
            this.$router.go(-1)
        }
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

.return-btn {
    position: absolute;
    z-index: 1000;
    top: 20px;
    left: 30px;

    img {
        width: 35px;
    }

    &:hover {
        opacity: 0.9;
    }
}

.title-wrapper {
    position: absolute;
    width: 100%;
    text-align: center;
    padding-top: 4em;
    color: whitesmoke;

    .title {
        font-size: 40px;
    }

    .sub-title {
        font-weight: 300;
    }
}

#article-set-list {
    height: 100vh;
    overflow: hidden;

    &.theme0 {
        background-color: $theme0-path-fill-4;
    }

    &.theme1 {
        background-color: $theme1-path-fill-4;
    }

    &.theme2 {
        background-color: $theme2-path-fill-4;
    }
}
</style>
