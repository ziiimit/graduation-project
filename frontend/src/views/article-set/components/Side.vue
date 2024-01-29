<template>
    <div class="side">
        <button class="home-btn" @click="goToHome">
            <svg xmlns=" http://www.w3.org/2000/svg" x="0px" y="0px" width="30" height="30" viewBox="0 0 24 24"
                class="icon">
                <path
                    d="M 12 2 A 1 1 0 0 0 11.289062 2.296875 L 1.203125 11.097656 A 0.5 0.5 0 0 0 1 11.5 A 0.5 0.5 0 0 0 1.5 12 L 4 12 L 4 20 C 4 20.552 4.448 21 5 21 L 9 21 C 9.552 21 10 20.552 10 20 L 10 14 L 14 14 L 14 20 C 14 20.552 14.448 21 15 21 L 19 21 C 19.552 21 20 20.552 20 20 L 20 12 L 22.5 12 A 0.5 0.5 0 0 0 23 11.5 A 0.5 0.5 0 0 0 22.796875 11.097656 L 12.716797 2.3027344 A 1 1 0 0 0 12.710938 2.296875 A 1 1 0 0 0 12 2 z">
                </path>
            </svg>
        </button>

        <h1 class="article-set-title">{{ articleSet.title }}</h1>
        <div class="theme-btn">
            <hr>
            {{ articleSet.theme }}
            <hr>
        </div>
        <ul class="article-list">
            <li v-for="(article, index) in articleSet.articles" @click="setCurrentArticleIndex(index)"
                :class="{ 'active': currentArticleIndex == index }">
                {{ article.title }}
            </li>
        </ul>
    </div>
</template>
<script>
import { getArticleSet } from '@/api/articleSet'

export default {
    name: "ArticleSetSide",

    data() {
        return {
            articleSet: null,
            currentArticleIndex: -1,
        }
    },
    methods: {
        setCurrentArticleIndex(index) {
            this.currentArticleIndex = index
            this.$emit('changeCurrentArticle', this.articleSet.articles[index])
        },
        goToHome() {
            this.$router.push({ name: "Home" })
        },
        getTheme() {
            return this.articleSet['theme']
        }
    },
    created() {
        let articleSetTitle = this.$route.params['title']
        let param = {
            'title': articleSetTitle
        }
        getArticleSet(param).then(res => {
            this.articleSet = res

            for (let item of this.$store.state.theme.themes) {
                if (item['themeName_en'] == this.articleSet['theme']) {
                    this.$emit('setColorTheme', item['colorTheme'])
                }
            }

            this.setCurrentArticleIndex(0)
        }).catch(err => {
            console.log(err)
        })
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

.side {
    position: absolute;
    top: 0;
    left: 0;
    width: 300px;
    height: 100vh;
    padding: 30px 10px;
    box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
    text-align: center;
}

.home-btn {
    margin-bottom: 20px;

    .theme0 & {
        color: $theme0-path-fill-4;
    }

    .theme1 & {
        color: $theme1-path-fill-4;
    }

    .theme2 & {
        color: $theme2-path-fill-4;
    }
}

.article-set-title {
    font-size: 25px;

    .theme0 & {
        color: $theme0-path-fill-3;
    }

    .theme1 & {
        color: $theme1-path-fill-3;
    }

    .theme2 & {
        color: $theme2-path-fill-3;
    }

}

.theme-btn {
    margin-top: 20px;
    cursor: pointer;
    transition: all 0.2s;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    padding: 0 3px;

    hr:nth-child(1) {
        width: 90%;

    }

    hr:nth-child(2) {
        width: 100%;
    }

    &:hover {
        .theme0 & {
            color: $theme0-path-fill-2;

            hr {
                border-color: $theme0-path-fill-1;
            }
        }

        .theme1 & {
            color: $theme1-path-fill-2;

            hr {
                border-color: $theme1-path-fill-1;
            }
        }

        .theme2 & {
            color: $theme2-path-fill-2;

            hr {
                border-color: $theme2-path-fill-1;
            }
        }

    }
}

.article-list {
    margin-top: 50px;
    height: calc(100% - 300px);
    overflow: scroll;
    padding: 0 20px;

    li {
        margin-bottom: 20px;
        text-align: center;
        width: 100%;
        word-wrap: break-word;
        font-weight: 400;
        cursor: pointer;
        color: gray;
        padding: 5px;
        border-radius: 10px;
        transition: all 0.2s;

        &.active {
            color: $article-bg;
            font-weight: 500;
        }

        .theme0 &.active {
            background-color: $theme0-path-fill-2;
        }

        .theme1 &.active {
            background-color: $theme1-path-fill-2;
        }

        .theme2 &.active {
            background-color: $theme2-path-fill-2;
        }
    }
}
</style>
