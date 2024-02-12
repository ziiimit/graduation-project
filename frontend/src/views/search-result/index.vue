<template>
    <div id="search-result">
        <div class="title">回复 & 相关文章推荐</div>
        <button class="home-btn" @click="goToHome">
            <svg xmlns=" http://www.w3.org/2000/svg" x="0px" y="0px" width="30" height="30" viewBox="0 0 24 24"
                class="icon">
                <path
                    d="M 12 2 A 1 1 0 0 0 11.289062 2.296875 L 1.203125 11.097656 A 0.5 0.5 0 0 0 1 11.5 A 0.5 0.5 0 0 0 1.5 12 L 4 12 L 4 20 C 4 20.552 4.448 21 5 21 L 9 21 C 9.552 21 10 20.552 10 20 L 10 14 L 14 14 L 14 20 C 14 20.552 14.448 21 15 21 L 19 21 C 19.552 21 20 20.552 20 20 L 20 12 L 22.5 12 A 0.5 0.5 0 0 0 23 11.5 A 0.5 0.5 0 0 0 22.796875 11.097656 L 12.716797 2.3027344 A 1 1 0 0 0 12.710938 2.296875 A 1 1 0 0 0 12 2 z">
                </path>
            </svg>
        </button>
        <Loading v-if="showLoading" />
        <div class="result" v-else>
            <Response :response="response" @typingFinished="showArticles" />
            <RecommendedArticleList ref='recommendedArticleList' :recommendedArticleList="recommendedArticleList" />
        </div>
    </div>
</template>
<script>
import Loading from '@/global/Loading.vue';
import Response from './components/Response.vue';
import RecommendedArticleList from './components/RecommendedArticleList.vue';
import { getSearchResult } from '@/api/search'
export default {
    name: "SearchResult",
    components: { Loading, Response, RecommendedArticleList },
    data() {
        return {
            showLoading: false,
            userInput: this.$route.query['input'],
            response: "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈。",
            recommendedArticleList: [
                {
                    title: "测试测试测试测试",
                    id: 12,
                    sequence: 0,
                    articleSet: "噢噢噢噢噢噢噢噢噢噢噢噢噢噢哦哦",
                    theme: "Mental Health and Addiction"
                },
                {
                    title: "测试测试测试测试",
                    id: 12,
                    sequence: 3,
                    articleSet: "噢噢噢噢噢噢噢噢噢噢噢噢噢噢哦哦",
                    theme: "The Science of Well-being"
                },
                {
                    title: "测试测试测试测试",
                    id: 12,
                    sequence: 3,
                    articleSet: "噢噢噢噢噢噢噢噢噢噢噢噢噢噢哦哦",
                    theme: "Focus, Productivity and Creativity"
                },
            ]
        }
    },
    methods: {
        goToHome() {
            this.$router.push({ name: "Home" })
        },
        getResult() {
            this.showLoading = true;
            let params = {
                userInput: this.userInput
            }
            getSearchResult(params).then(res => {
                this.response = res.response;
                this.recommendedArticleList = res.recommendedArticleList;
                this.showLoading = false;
            }).catch(err => {
                console.log(err)
            })
        },
        showArticles() {
            this.$refs['recommendedArticleList'].showArticles()
        }
    },
    created() {
        this.getResult()
    },
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

.title {
    position: absolute;
    font-size: 25px;
    font-weight: 500;
    color: $search-main;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
}

.home-btn {
    color: #858585;
    position: absolute;
    top: 20px;
    left: 40px;
}

.loading {
    padding-top: 45vh;
}

.result {
    width: 100%;
    padding-top: 100px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 30px;
}


#response {
    width: 1060px;
    padding: 20px 30px;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
    border-radius: 20px;
}

#recommend-article-list {
    width: 1060px;
}
</style>
