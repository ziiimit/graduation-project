<template>
    <div id="article-set-list">
        <ul>
            <li v-for="(articleSet, index) in articleSetList" :class="{ 'active': introVisible[index] }"
                @mouseenter="showIntro(index)" @mouseleave="hideIntro(index)" @click="navigateToArticleSet(index)">
                <div class="title">
                    <div class="title_zh">{{ articleSet['title_zh'] }}</div>
                    <div class="title_en">{{ articleSet['title_en'] }}</div>
                </div>
                <Transition name="from-left-to-left">
                    <div class="intro" v-show="introVisible[index]">
                        <div class="intro_zh"><div class="content">{{ articleSet['intro_zh'] }}</div></div>
                        <!-- <div class="intro_en">{{ articleSet['intro_en'] }}</div> -->
                    </div>
                </Transition>
            </li>
        </ul>
    </div>
</template>
<script>
import { getArticleSetList } from "@/api/articleset";
export default {
    name: "ArticleSetList",
    props: ['themeTitle_en'],
    data() {
        return {
            articleSetList: null,
            introVisible: [],
            introChosen: null,
        }
    },

    methods: {
        showIntro(index) {
            // UI操作流畅度考虑:
            let currentItem = document.querySelector(`li:nth-child(${index + 1})`)
            currentItem.style.transition = "padding-bottom 0.2s"
            this.introVisible = [];
            this.introVisible[index] = true;
        },
        hideIntro(index) {
            if (this.introChosen == index) return
            // UI操作流畅度考虑:
            let currentItem = document.querySelector(`li:nth-child(${index + 1})`)
            currentItem.style.transition = "padding-bottom 0s"
            this.introVisible = [];
        },
        navigateToArticleSet(index) {
            this.introChosen = index;
            this.$router.push({
                name: "ArticleSet",
                params:
                {
                    themeTitle_en: this.themeTitle_en,
                    articleSetTitle_en: this.articleSetList[index]['title_en']
                }
            })
        }
    },
    created() {
        getArticleSetList(this.themeTitle_en).then((res) => {
            this.articleSetList = res;
            this.$emit("dataLoaded")
        }).catch(err => {

        })
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";
@import "@/style/transition.scss";

#article-set-list {
    height: calc(100vh - 222px);
    overflow: scroll;
    padding-top: 60px;
    position: relative;
}

ul {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    padding-left: 10vw;
    padding-bottom: 250px; //让最后一个元素不要太贴着列表底部，不然操作体验感不好
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
        padding-bottom: 210px;
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
    z-index: 10;
    width: 350px;
    font-size: 13px;
    padding: 10px;
    border-radius: 1em;
    height: 200px;
    transform: translate(5em, 0.9em);
    line-height: 20px;
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

.intro_zh .content{
    position: relative;
    color: whitesmoke;
    height: 180px;
    overflow: hidden;
    &::after{
        content:"......";
        text-indent: 0;
        display: block;
        position: absolute;
        color: whitesmoke;
        width: 2em;
        bottom: 0px;
        right: 4.5px;
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
}

.from-left-enter-active {
    transition: opacity 0.2s ease 0.3s, transform 0.2s ease 0.3s;
}
</style>
