<template>
    <div id="article-set-list" :class="[theme['themeColor']]">
        <ul>
            <li v-for="(articleSet, index) in articleSetList" :class="{ 'active': introVisible[index] }"
                @mouseenter="showIntro(index)" @mouseleave="hideIntro(index)" @click="choose(index)">
                <div class="title">
                    <div class="title_zh">{{ articleSet['title_zh'] }}</div>
                    <div class="title_en">{{ articleSet['title_en'] }}</div>
                </div>
                <Transition name="from-left-to-left">
                    <div class="intro" v-show="introVisible[index]">
                        <div class="intro_zh">{{ articleSet['intro_zh'] }}</div>
                        <!-- <div class="intro_en">{{ articleSet['intro_en'] }}</div> -->
                    </div>
                </Transition>
            </li>
        </ul>
    </div>
</template>
<script>
// @ts-ignore
import { getArticleSetList } from "@/api/articleset";
export default {
    name: "ArticleSetList",
    props: ['theme'],
    data() {
        return {
            articleSetList: null,
            introVisible: [],
            introChosen: null,
        }
    },
    methods: {
        showIntro(index) {
            document.querySelector(`li:nth-child(${index + 1})`).style.transition = "padding-bottom 0.2s"
            this.introVisible = [];
            this.introVisible[index] = true;
        },
        hideIntro(index) {
            if (this.introChosen == index) return
            document.querySelector(`li:nth-child(${index + 1})`).style.transition = "padding-bottom 0s"
            this.introVisible = [];
        },
        choose(index) {
            this.introChosen = index;
            console.log(index)
        }
    },
    created() {
        let themeTitle_en = this.theme['title_en'];
        getArticleSetList(themeTitle_en).then((res) => {
            this.articleSetList = res;
            this.articleSetList[1] = res[0];
            this.articleSetList[2] = res[0];
            this.$emit("dataLoaded")
        }).catch(err => {

        })
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";
@import "@/style/transition.scss";

#article-set-list {
    height: calc(100vh - 230px);
    overflow: scroll;
    padding-top: 60px;
    position: relative;
}

ul {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    padding: 20px 20px 50px;
    padding-left: 10vw;
    gap: 100px;
    max-width: 1500px;
    flex-direction: column;
    overflow-x: scroll;
    overflow-y: visible;
}

li {
    position: relative;
    cursor: pointer;
    display: inline;

    &.active {
        padding-bottom: 220px;
    }
}


.title_zh {
    font-size: 20px;
    position: relative;
    line-height: 1em;
    font-weight: 500;

    &:before {
        display: block;
        position: absolute;
        content: "";
        width: 0.5em;
        height: 0.5em;
        top: 0.25em;
        left: -1em;
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

    .active &:before {
        height: 250px;
    }
}

.intro_zh {
    position: absolute;
    // top: 40px;
    z-index: 10;
    width: 350px;
    font-size: 13px;
    padding: 1em 1.5em;
    border-radius: 1em;
    color: whitesmoke;
    height: 200px;
    transform: translate(5em, 0.9em);
    line-height: 1.5em;
    text-indent: 2em;

    .theme0 & {
        box-shadow: rgba($theme0-light, 0.4) -10px 0px, rgba($theme0-light, 0.3) -20px 0px, rgba($theme0-light, 0.2) -30px 0px, rgba($theme0-light, 0.1) -40px 0px, rgba($theme0-light, 0.05) -50px 0px;
    }

    .theme1 & {
        box-shadow: rgba($theme1-light, 0.4) -10px 0px, rgba($theme1-light, 0.3) -20px 0px, rgba($theme1-light, 0.2) -30px 0px, rgba($theme1-light, 0.1) -40px 0px, rgba($theme1-light, 0.05) -50px 0px;
    }

    .theme2 & {
        box-shadow: rgba($theme2-light, 0.4) -10px 0px, rgba($theme2-light, 0.3) -20px 0px, rgba($theme2-light, 0.2) -30px 0px, rgba($theme2-light, 0.1) -40px 0px, rgba($theme2-light, 0.05) -50px 0px;
    }


    .theme0 & {
        background-color: $theme0-light;
    }

    .theme1 & {
        background-color: $theme1-light;
    }

    .theme2 & {
        background-color: $theme2-light;
    }
}

.from-left-enter-active {
    transition: opacity 0.2s ease 0.3s, transform 0.2s ease 0.3s;
}
</style>
