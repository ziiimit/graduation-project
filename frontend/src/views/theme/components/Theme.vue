<template>
    <div id="theme" :class="[theme['themeColor']]">
        <div id="top-bar">
            <HomeBtn />
        </div>
        <Transition name="from-left">
            <div class="title" v-show="titleVisible">
                <div class="title-zh">{{ theme['title_zh'] }}</div>
                <div class="title-en">{{ theme['title_en'] }}</div>
            </div>
        </Transition>
        <Transition name="from-bottom">
            <ArticleSetList :theme="theme" v-show="asListVisible" @dataLoaded="show" />
        </Transition>
        <Loading :theme="theme" v-if="loadingVisible" />
    </div>
</template>
<script>
import ArticleSetList from "./ArticleSetList.vue"
import Loading from "@/components/Loading.vue"
import HomeBtn from "@/components/HomeBtn.vue"
export default {
    name: "Theme",
    components: { ArticleSetList, Loading, HomeBtn },
    data() {
        return {
            theme: null,
            titleVisible: false,
            asListVisible: false,
            loadingVisible: true,
        }
    },
    methods: {
        show() {
            this.titleVisible = true;
            this.asListVisible = true;
            this.loadingVisible = false;
        },

    },
    created() {
        switch (this.$route.name) {
            case "Theme_MentalHealthAndAddiction":
                this.theme = this.$store.state.theme.themes[0];
                break;
            case "Theme_FocusProductivityAndCreativity":
                this.theme = this.$store.state.theme.themes[1];
                break;
            case "Theme_TheScienceOfWellBeing":
                this.theme = this.$store.state.theme.themes[2];
        }


    }
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


#loading {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
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
