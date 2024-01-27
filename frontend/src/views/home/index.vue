<template>
    <div id="home">


        <div class="wrapper">
            <div class="theme-title">{{ currentTheme["themeName_zh"] }}</div>
            <div class="sub-title">{{ currentTheme["themeName_en"] }}</div>
        </div>

        <MoreBtn @showArticleSetList="changeArticleSetListVisibility" />

        <ThemeMenu v-show="themeMenuVisible" />

        <ArticleSetList ref="article-set-list" @closed="showThemeMenu" />

    </div>
</template>
<script>
import MoreBtn from './components/MoreBtn.vue'
import ThemeMenu from './components/ThemeMenu.vue'
import ArticleSetList from './components/ArticleSetList/index.vue'

export default {
    name: "Home",
    components: {
        MoreBtn,
        ThemeMenu,
        ArticleSetList
    },
    data() {
        return {
            themes: this.$store.state.theme.themes,
            themeMenuVisible: true
        }
    },
    computed: {
        currentTheme() {
            return this.themes[this.$store.state.theme.currentThemeIndex]
        }
    },
    methods: {
        changeArticleSetListVisibility() {
            this.themeMenuVisible = false
            this.$refs['article-set-list'].changeVisibility()
        },
        showThemeMenu() {
            setTimeout(() => {
                this.themeMenuVisible = true;
            }, 1000)
        }
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

#home {
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 50px;
    transition: all 0.2s;

    .theme0 & {
        background-color: $theme0-bg;
    }

    .theme1 & {
        background-color: $theme1-bg;
    }

    .theme2 & {
        background-color: $theme2-bg;
    }
}

.theme-title {
    font-size: 60px;
    font-family: revert;
    padding: 0.2em 1em;

    .theme0 & {
        color: $theme0-title;
    }

    .theme1 & {
        color: $theme1-title;
    }

    .theme2 & {
        color: $theme2-title;
    }
}

.sub-title {
    font-size: 20px;
    font-family: revert;
    text-align: center;

    .theme0 & {
        color: $theme0-title;
    }

    .theme1 & {
        color: $theme1-title;
    }

    .theme2 & {
        color: $theme2-title;
    }
}
</style>
