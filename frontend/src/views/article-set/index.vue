<template>
    <div id="article-set" :class="[colorTheme]">
        <Side @setColorTheme="(colorTheme) => this.colorTheme = colorTheme" @changeCurrentArticle=getArticle />
        <div class="article-main">
            <Loading v-if="showLoading" />
            <Article v-else :article="currentArticle" />
        </div>
    </div>
</template>
<script>
import Side from './components/Side.vue'
import Article from './components/Article.vue'
import Loading from '@/global/Loading.vue'
import { getArticle } from '@/api/articleSet'

export default {
    name: "ArticleSet",
    components: { Side, Article, Loading },
    data() {
        return {
            currentArticle: null,
            colorTheme: null,
            showLoading: true
        }
    },
    methods: {
        getArticle(article) {
            this.showLoading = true
            getArticle(article).then(res => {
                console.log(res)
                this.currentArticle = res
                this.showLoading = false
            }).catch(err => {
                console.log(err)
            })
        }
    },

}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

#article-set {
    position: relative;
    width: 100%;
    height: 100vh;
    background-color: $article-bg;
    color: $article-font;
}

.article-main {
    width: 100%;
    height: 100vh;
    padding: 20px;
    padding-left: 320px;
}

.loading {
    height: 100%;
}
</style>
