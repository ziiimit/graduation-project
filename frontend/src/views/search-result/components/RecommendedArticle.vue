<template>
    <div id="article">
        <div class="article-main">
            <Loading v-if="showLoading" />
            <div class="content" v-else>
                <h2 class="title">{{ article['title'] }}</h2>
                <ul class="paragraph-list">
                    <li v-for="  paragraph   in   article['paragraphs']">
                        {{ paragraph['content'] }}
                    </li>
                </ul>
            </div>
            <button class="hide" @click="() => this.$emit('hide')"><svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                    width="24" height="24" viewBox="0 0 24 24">
                    <path
                        d="M 4.7070312 3.2929688 L 3.2929688 4.7070312 L 10.585938 12 L 3.2929688 19.292969 L 4.7070312 20.707031 L 12 13.414062 L 19.292969 20.707031 L 20.707031 19.292969 L 13.414062 12 L 20.707031 4.7070312 L 19.292969 3.2929688 L 12 10.585938 L 4.7070312 3.2929688 z">
                    </path>
                </svg></button>
        </div>
    </div>
</template>
<script>
import { getArticle } from '@/api/articleSet';
import Loading from "@/global/Loading.vue"
export default {
    name: "RecommendedArticle",
    components: { Loading },
    props: ['articleMeta'],
    data() {
        return {
            showLoading: true,
            article: {}
        }
    },
    created() {
        this.showLoading = true;
        getArticle(this.articleMeta).then(res => {
            this.article = res
        }).catch(err => {

        })
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

#article {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #3f3e3e5e;
}


.article-main {
    position: relative;
    width: 80vw;
    height: 90vh;
    background-color: $article-bg;
    overflow: scroll;
    border-radius: 20px;
    padding: 20px;
}

.loading {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

button.hide {
    position: absolute;
    right: 20px;
    top: 20px;

    &:hover {
        opacity: 0.7;
    }
}

.title {
    text-align: center;
    font-size: 30px;
    margin-bottom: 20px;
    color: $search-main;
}

.paragraph-list {
    text-indent: 2em;
    font-size: 20px;
    color: $article-font;
}
</style>
