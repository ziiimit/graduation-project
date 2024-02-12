<template>
    <div id="recommend-article-list">
        <ul>
            <li v-for="item in recommendedArticleList" :class="getThemeClass(item.theme)" @click="setArticleClicked(item)">
                <div class="article-title">{{ item.title }}</div>
                <div class="article-set-title">{{ item.articleSet }}</div>
                <div class="theme-name">{{ item.theme }}</div>
            </li>
        </ul>
        <RecommendedArticle :articleMeta="this.articleClicked" v-show="showRecommendedArticle"
            @hide="() => this.showRecommendedArticle = false" />
    </div>
</template>
<script>
import RecommendedArticle from './RecommendedArticle.vue'
export default {
    name: "RecommendedArticleList",
    props: ['recommendedArticleList'],
    components: { RecommendedArticle },
    data() {
        return {
            currentArticleSetList: null,
            articleClicked: null,
            showRecommendedArticle: false,
        }
    },
    methods: {
        setArticleClicked(articleClicked) {
            this.articleClicked = { 'id': articleClicked['id'], 'title': articleClicked['title'] };
            this.showRecommendedArticle = true;
        },
        getThemeClass(theme) {
            for (let item of this.$store.state.theme.themes) {
                if (item['themeName_en'] == theme) return item.colorTheme
            }
        },
        showArticles() {
            let articles = document.querySelectorAll('#recommend-article-list li');
            let i = 0;
            let show = function (item) {
                item.style.transitionDelay = ``;
                item.style.opacity = "1";
                item.style.pointerEvents = "auto";
                item.style.transform = 'translateY(0px)';
                i = i + 1;
                if (i == articles.length) return;
                setTimeout(() => { show(articles[i]) }, 300);
            }
            if (i == articles.length) {
                return;
            }
            show(articles[i])
        }
    },
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

ul {
    display: flex;
    width: 100%;
    gap: 5%;
}

li {
    width: 30%;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
    border-radius: 20px;
    padding: 20px;
    position: relative;
    overflow: hidden;

    &.theme0 {
        &::after {
            background: $theme0-path-fill-2;
        }
    }

    &.theme1 {
        &::after {
            background: $theme1-path-fill-2;
        }
    }

    &.theme2 {
        &::after {
            background: $theme2-path-fill-2;
        }
    }
}

li::after {
    display: block;
    content: "";
    position: absolute;
    z-index: -1;
    width: 80px;
    height: 100px;
    right: -40px;
    top: -50px;
    border-radius: 90px;
    transition: all 0.5s;
}

.article-title {
    text-align: center;
    margin-bottom: 30px;
    padding: 0 20px;
    color: $search-main;
    font-weight: 600;
    font-size: 18px;
}

.article-set-title {
    margin-bottom: 10px
}

.article-set-title,
.theme-name {
    font-size: 15px;
    color: #727272;
}

.article-set-title::before {
    display: block;
    content: "所属文章系列";
    color: $search-main;
    font-size: 13px;
    font-weight: 600;
}

.theme-name::before {
    display: block;
    content: "主题";
    color: $search-main;
    font-size: 13px;
    font-weight: 600;
}

li {
    opacity: 0;
    transform: translateY(10px);
    pointer-events: none;
    transition: all 0.5s;
    cursor: pointer;
}

li:hover {
    &::after {
        height: 400px;
    }
}
</style>
