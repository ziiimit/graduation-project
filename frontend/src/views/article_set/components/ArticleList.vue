<template>
    <div id="article-list">
        <ul>
            <li v-for="(article, index) in articleList" @click="navigateToArticle(index)">
                <ArticleListItem :articleTitle_en="article['title_en']" :articleTitle_zh="article['title_zh']"
                    :summary_zh="article['summary_zh']" />
            </li>
        </ul>
    </div>
</template>
<script>
import { getArticleSet } from "@/api/articleset.js";
import ArticleListItem from "./ArticleListItem.vue";
export default {
    name: "ArticleList",
    components: { ArticleListItem },
    props: ['themeTitle_en', 'articleSetTitle_en'],
    data() {
        return {
            articleList: null
        }
    },
    methods: {
        navigateToArticle(articleSequence) {
            this.$router.push({
                name: "Article", params: {
                    articleSetTitle_en: this.articleSetTitle_en,
                    articleSequence: articleSequence
                }
            })
        }
    },
    created() {
        console.log("loading")
        getArticleSet(this.articleSetTitle_en).then(res => {
            console.log(res)
            this.articleList = res
            this.$emit("dataLoaded", res[0]['articleSetTitle_zh'])
        }).catch(err => {

        })
    }
}
</script>
<style scoped lang='scss'>
ul {
    padding-top: 40px;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
</style>
