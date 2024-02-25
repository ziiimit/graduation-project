<template>
    <div id="article-set" :class="[themeColor]">
        <Loading v-if="loadingVisible" />
        <div v-else>
            <HomeBtn />
            <header>
                <div class="theme" :class="{ active: themeTitleActive }" @mouseover="() => themeTitleActive = true"
                    @mouseleave="() => themeTitleActive = false" @click="navigateToTheme">
                    <div class="title_zh">{{ themeTitle_zh }}</div>
                    <div class="title_en">{{ themeTitle_en }}</div>
                </div>
                <div class="article-set" :class="{ active: !themeTitleActive }">
                    <div class="title_zh">{{ articleSetTitle_zh }}</div>
                    <div class="title_en">{{ articleSetTitle_en }}</div>
                </div>
            </header>
        </div>
        <ArticleList :themeTitle_en="themeTitle_en" :articleSetTitle_en="articleSetTitle_en"
            @dataLoaded="(articleSetTitle_zh) => handleDataLoaded(articleSetTitle_zh)" />
    </div>
</template>
<script>
import Loading from "@/components/Loading.vue";
import HomeBtn from "@/components/HomeBtn.vue";
import ArticleList from "./components/ArticleList.vue";
export default {
    name: "ArticleSet",
    components: { Loading, HomeBtn, ArticleList },
    data() {
        return {
            themeTitle_en: this.$route.params.themeTitle_en,
            articleSetTitle_en: this.$route.params.articleSetTitle_en,
            articleSetTitle_zh: "",
            loadingVisible: true,
            themeTitleActive: false
        }
    },
    computed: {
        themeColor() {
            return this.$store.state.theme.themeColors[this.themeTitle_en]
        },
        themeTitle_zh() {
            for (let theme of this.$store.state.theme.themes) {
                if (theme['title_en'] == this.themeTitle_en) return theme['title_zh']
            }
        },
    },
    methods: {
        handleDataLoaded(articleSetTitle_zh) {
            this.articleSetTitle_zh = articleSetTitle_zh;
            this.loadingVisible = false;
        },
        navigateToTheme() {
            this.$router.push({
                name: 'Theme', params: {
                    themeTitle_en: this.themeTitle_en
                }
            })
        }
    },
}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";


#article-set {
    padding: 20px clamp(1.5rem, 6vw, 4rem) 0 clamp(1.5rem, 10vw, 8rem);
}


header .theme {
    cursor: pointer;
    margin-bottom: 10px;
}

header .article-set {
    padding-left: 1.3em;

    .title_zh {
        position: relative;

        &:before {
            display: block;
            position: absolute;
            content: "";
            width: 0.5em;
            height: 0.5em;
            top: 0.5em;
            left: -0.8em;
            border-radius: 0.25em;
            transition: height 0.2s ease;

            .theme0 & {
                background-color: $theme0;
            }

            .theme1 & {
                background-color: $theme1;
            }

            .theme2 & {
                background-color: $theme2;
            }
        }
    }
}

.title_zh,
.title_en {
    transition: all 0.2s;
}

.title_zh {
    font-family: $fontFamily_zh;

    .active & {
        font-size: 1.5em;
        font-weight: 500;

        .theme0 & {
            color: $theme0
        }

        .theme1 & {
            color: $theme1
        }

        .theme2 & {
            color: $theme2
        }
    }
}

.title_en {
    font-family: $fontFamily_en;

    .active & {
        font-size: 1.5em;
    }
}







header .theme {}
</style>
