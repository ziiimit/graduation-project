<template>
<div id="search-result">
    <Loading v-if="loadingVisible" />
    <div v-else>
        <HomeBtn />
        <Response :userInput_zh="userInput_zh" :response_zh="response_zh" :recommendedArticleList="recommendedArticleList" />
    </div>
</div>
</template>

<script>
import Loading from "@/components/Loading.vue";
import HomeBtn from "@/components/HomeBtn.vue";
import Response from "./components/Response.vue";
import { getSearchResult } from "@/api/search.js";

export default {
    name: "SearchResult",
    components: { Loading, HomeBtn, Response },
    data() {
        return {
            userInput_zh: this.$route.query['userInput_zh'],
            previousInput:"",
            response_zh: "",
            recommendedArticleList: [],
            loadingVisible: true,
        }
    },
    methods: {
        getResult(userInput_zh) {
            console.log('get result')
            this.loadingVisible = true;
            getSearchResult(userInput_zh).then(res => {
                this.response_zh = res['response_zh']
                for (let para of res['paragraphList']) {
                    let currentArticleTitle_en = para['articleTitle_en']
                    let exists = false
                    for (let item of this.recommendedArticleList) {
                        if (item['articleTitle_en'] == currentArticleTitle_en) {
                            exists = true;
                            break;
                        }
                    }
                    if (!exists) {
                        this.recommendedArticleList.push(para)
                    }
                }
                this.loadingVisible = false;
            }).catch(err => {

            })
        }
    },
    created() {
        console.log("create")
        this.getResult(this.userInput_zh)
    },
    deactivated(){
        console.log("deactivated")
        this.previousInput = this.userInput_zh
    },
    activated(){
        
        // 第一次进入组件
        if (this.previousInput == "") return


        console.log("activated")
        this.userInput_zh = this.$route.query['userInput_zh']
        if(this.userInput_zh != this.previousInput){
            this.getResult(this.userInput_zh)
        }
    }
}
</script>

<style lang="scss" scoped>
#search-result {
    padding-top: 80px;
}
</style>
