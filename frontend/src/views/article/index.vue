<template>
    <div id="article">
        <Loading v-if="loadingVisible" :articleSetTitle_en="articleSetTitle_en" />
        <div v-else>
            <div id="top-bar">
                <HomeBtn />
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
            article: null,
            loadingVisible: true
        }
    },
    created() {
        getArticle(this.articleSetTitle_en, this.articleSequence).then(res => {
            this.article = res
            this.loadingVisible = false
        }).catch(err => { })
    }
}
</script>
<style scoped lang='scss'>
#loading {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
}
</style>
