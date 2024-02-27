<template>
    <div id="response">
        <div class="msg right-msg">
            <div class="msg-header">YOU</div>
            <div class="msg-bubble">
                <div class="msg-text">{{ userInput_zh }}</div>
            </div>
        </div>
        <div class="msg left-msg">
            <div class="msg-header">APP</div>
            <div class="msg-bubble">
                <div class="msg-text" id="response-content"></div>
            </div>
        </div>
        <Transition name="from-bottom">
        <div class="msg left-msg" v-show="recPreVisible">
            <div class="msg-header">APP</div>
            <div class="msg-bubble">
                <div class="msg-text" id="rec-pre"></div>
            </div>
        </div>
        </Transition>
        <Transition name="from-bottom">
            <div class="msg left-msg" v-show="recVisible">
                <div class="msg-header">APP</div>
                <div class="msg-bubble">
                    <div class="msg-text">
                        <ul class="recommended-article-list">
                            <li v-for="item in recommendedArticleList" :class="[getThemeColor(item['themeTitle_en'])]" @click="navigateToArticle(item)">{{
                                item['themeTitle_zh'] }} / {{
        item['articleSetTitle_zh'] }} / {{ item['articleTitle_zh'] }}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </Transition>
    </div>
</template>
<script>
export default {
    name: "Response",
    props: ['response_zh', 'userInput_zh', 'recommendedArticleList'],
    data() {
        return {
            recPreVisible:false,
            recVisible:false,
        }
    },
    methods: {
        getThemeColor(themeTitle_en) {
            return this.$store.state.theme.themeColors[themeTitle_en]
        },
        typeWriter(elem ,text, i, resolve) {
            if (i < (text.length)) {
                elem.innerHTML = text.substring(0, i + 1);
                setTimeout(() => {
                    this.typeWriter(elem,text, i + 1, resolve)
                }, 40);
            } else {
                resolve()
            }
        },
        typeMessage(elem ,message) {
            return new Promise((resolve, reject) => {
                this.typeWriter(elem,message, 0, resolve)
            })
        },
        navigateToArticle(article){
            const articleSequence = article['articleSequence']
            const articleSetTitle_en = article['articleSetTitle_en']
            this.$router.push({name:"Article",params:{
                articleSetTitle_en,
                articleSequence
            }})
        }
    },
    async mounted() {
        const elem1 = document.querySelector("#response-content")
        const message1 = this.response_zh
        await this.typeMessage(elem1,message1)
        const elem2 = document.querySelector("#rec-pre")
        const message2 = "以下是推荐文章:"
        this.recPreVisible = true;
        await this.typeMessage(elem2,message2)
        this.recVisible = true;
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";
@import "@/style/transition.scss";
$header-bg: #31363b;
$msg-bg: #878686;

#response {
    width: 85vw;
    height: calc(100vh - 80px);
    overflow-y: scroll;
    padding: 30px 20px 100px;
    margin: 0 auto;
    max-width: 1000px;
    border-radius: 50px;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    box-shadow: rgba(67, 71, 85, 0.27) 0px 0px 0.25em, rgba(90, 125, 188, 0.05) 0px 0.25em 1em;
}

* {
    color: whitesmoke;
}

.msg {
    display: flex;
    align-items: flex-start;
    margin-bottom: 10px;
}

.msg-header {
    width: 50px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    margin-right: 10px;
    border-radius: 50%;
    background: $header-bg;
    font-size: 16px;
    font-weight: 500;
}


.msg-bubble {
    padding: 15px;
    border-radius: 15px;
    font-size: 14px;
    background: $msg-bg;
    max-width: 50%;
}

.left-msg .msg-bubble {
    border-top-left-radius: 0;
    .recommended-article-list &{
        text-indent: 0;
    }
}

.right-msg {
    flex-direction: row-reverse;
}

.right-msg .msg-bubble {
    border-top-right-radius: 0;
}

.right-msg .msg-header {
    margin: 0 0 0 10px;
}

.recommended-article-list {

    li {
        display: inline-block;
        padding: 10px 10px;
        color: $app-bg;
        cursor: pointer;
        border-radius: 1em;
        margin-bottom: 1em;
        text-indent: 0;
        font-weight: 500;

        &.theme0 {
            background: $theme0;
        }

        &.theme1 {
            background: $theme1;
        }

        &.theme2 {
            background: $theme2;
        }

        &:hover{
            opacity: 0.8;
        }

    }
}
</style>
