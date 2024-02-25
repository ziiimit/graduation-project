<template>
    <div id="theme" :class="[themeColor]">
        <Loading v-if="loadingVisible" />
        <HomeBtn v-show="!loadingVisible" />
        <Transition name="from-left">
            <div class="title" v-show="!loadingVisible">
                <div class="title-zh">{{ themeTitle_zh }}</div>
                <div class="title-en">{{ themeTitle_en }}</div>
            </div>
        </Transition>
        <Transition name="from-bottom">
            <ArticleSetList :themeTitle_en="themeTitle_en" v-show="!loadingVisible"
                @dataLoaded="() => this.loadingVisible = false" />
        </Transition>
    </div>
</template>
<script>
import ArticleSetList from "./components/ArticleSetList.vue"
import Loading from "@/components/Loading.vue"
import HomeBtn from "@/components/HomeBtn.vue"
export default {
    name: "Theme",
    components: { ArticleSetList, Loading, HomeBtn },
    data() {
        return {
            themeTitle_en: this.$route.params['themeTitle_en'],
            loadingVisible: true,
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
}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";
@import "@/style/transition.scss";
$top-bar: 50px;

#theme {
    height: 100vh;
    padding: $top-bar clamp(1.5rem, 6vw, 4rem) 0 clamp(1.5rem, 10vw, 8rem);
}

#top-bar {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
    width: 100%;
    height: $top-bar;
}


.title-zh {
    font-size: 50px;
    font-weight: 600;
    font-family: serif;

    .theme0 & {
        color: $theme0;
    }

    .theme1 & {
        color: $theme1;
    }

    .theme2 & {
        color: $theme2;
    }
}

.title-en {
    font-size: 30px;
    font-family: cursive;
}


// ASList上下的渐变过渡
#theme:after,
.title:after {
    display: block;
    content: "";
    position: absolute;
    z-index: 100;
    left: 0;
    width: 100%;
    height: 60px;
    background: linear-gradient(to bottom, $app-bg, $app-bg 50%, rgba($app-bg, 0));
}

#theme:after {
    height: 100px;
    bottom: 0;
    background: linear-gradient(to top, $app-bg, $app-bg 50%, rgba($app-bg, 0));
}
</style>
