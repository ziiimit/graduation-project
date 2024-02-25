<template>
    <ul id="recommended-article-list">
        <li v-for="article in recommendedArticleList">
            <ArticleListItem :articleTitle_en="article['articleTitle_en']" :articleTitle_zh="article['articleTitle_zh']"
                :summary_zh="article['summary_zh']" />
        </li>
    </ul>
</template>
<script>
import ArticleListItem from "@/views/article_set/components/ArticleListItem.vue";
export default {
    name: "RecommendedArticleList",
    components: { ArticleListItem },
    props: ['recommendedArticleList']
}
</script>
<style scoped lang='scss'>
#recommended-article-list {
    display: flex;
    flex-wrap: wrap;
    width: 100vw;
    justify-content: center;
    gap: 20px;
}
</style>
