
<template>
    <div id="article" :class="[themeColor]">
        <Loading v-if="loadingVisible" />
        <div v-else>
            <HomeBtn />
            <div class="article-main">
                <div class="title">
                    <div class="title_zh">
                        {{ articleMeta["articleTitle_zh"] }}
                    </div>
                    <div class="title_en">
                        {{ articleMeta["articleTitle_en"] }}
                    </div>
                    <div class="navigator">
                        <span class="theme" @click="navigate('Theme')">{{ articleMeta["themeTitle_zh"] }}</span>
                        <span class="article-set" @click="navigate('ArticleSet')">{{ articleMeta["articleSetTitle_zh"]
                        }}</span>
                    </div>
                </div>
                <div class="text" v-for="p in paragraphs">
                    <p class="text_zh">{{ p['text_zh'] }}</p>
                    <p class="text_en">{{ p['text_en'] }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Loading from "@/components/Loading.vue";
import HomeBtn from "@/components/HomeBtn.vue";
import { getArticle } from "@/api/article.js"
export default {
    name: "Article",
    components: { Loading, HomeBtn },
    data() {
        return {
            articleSetTitle_en: this.$route.params['articleSetTitle_en'],
            articleSequence: this.$route.params['articleSequence'],
            articleMeta: null,
            paragraphs: null,
            loadingVisible: true,
            themeColor: "",
        }
    },
    methods: {
        navigate(to) {
            let themeTitle_en = this.articleMeta['themeTitle_en']
            let articleSetTitle_en = this.articleMeta['articleSetTitle_en']
            switch (to) {
                case "Theme":
                    this.$router.push({ name: "Theme", params: { themeTitle_en } })
                    break;
                case "ArticleSet":
                    this.$router.push({
                        name: "ArticleSet", params: {
                            "themeTitle_en": themeTitle_en,
                            "articleSetTitle_en": articleSetTitle_en
                        }
                    })
                    break;
            }
        }
    },
    created() {
        getArticle(this.articleSetTitle_en, this.articleSequence).then(res => {
            this.articleMeta = res['meta'][0]
            const themeTitle_en = this.articleMeta['themeTitle_en']
            this.themeColor = this.$store.state.theme.themeColors[themeTitle_en]
            this.paragraphs = res['paragraphs']
            this.loadingVisible = false
        }).catch(err => { })
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";

#loading {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
}

#article {
    padding-top: 50px;
}

.title_zh {
    font-family: $fontFamily_zh;
}

.title_en {
    font-family: $fontFamily_en;
}

.article-main .title {
    text-align: center;
    margin-bottom: 150px;

    .title_zh {
        font-size: 40px;
        margin-bottom: 10px;

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

    .title_en {
        font-size: 25px
    }
}

.navigator {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 20px;


    span:nth-child(odd):after {
        content: "";
        position: absolute;
        top: 0;
        right: -20px;
        width: 0;
        height: 100%;
        border: 1px solid #a6a6a6;
        transform: rotate(20deg)
    }

    span {
        position: relative;
        border: 2px solid;
        border-radius: 50px;
        padding: 5px 10px;
        cursor: pointer;
        color: #373636;
        transition: all 0.1s;

        .theme0 & {
            border-color: $theme0-light;
        }

        .theme1 & {
            border-color: $theme1-light;
        }

        .theme2 & {
            border-color: $theme2-light;
        }

        &:hover {
            color: $app-bg;
            font-weight: 600;

            .theme0 & {
                background: $theme0-light;
            }

            .theme1 & {
                background: $theme1-light;
            }

            .theme2 & {
                background: $theme2-light;
            }
        }
    }
}

.text {
    padding: 0 clamp(20px, 10vw, 10vw);
    margin-bottom: 100px;

    p {
        max-width: 800px;
        margin: 20px auto;
        font-size: 20px;
        text-indent: 2em;

        &.text_en {
            color: #585858
        }
    }
}
</style>
