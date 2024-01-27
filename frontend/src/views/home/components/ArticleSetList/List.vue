<template>
    <div class="grid">
        <a href="#" class="grid__item" v-for="item in articleSets">
            <div class="stack">
                <div class="stack__deco"></div>
                <div class="stack__deco"></div>
                <div class="stack__deco"></div>
                <div class="stack__deco"></div>
                <div class="stack__cover">
                    <h3 class="article-title">{{ item.title }}</h3>
                    <ul class="description">
                        <li>
                            <span class="title">总文章数</span>
                            <span class="content">{{ item.articleTotal }}</span>
                        </li>
                    </ul>
                </div>
            </div>

        </a>
    </div>
</template>
<script>
export default {
    name: "ArticleSetList",
    data() {
        return {
            articleSets: [
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                },
                {
                    title: "你好你好你好你好你奶奶奶奶奶奶奶奶奶奶奶奶奶奶呢",
                    url: '#',
                    articleTotal: 100
                }
            ]
        }
    },
    mounted() {
        const AltairFx = require('./animation.js').AltairFx;
        document.querySelectorAll('.grid > .grid__item').forEach(function (stackEl) {
            new AltairFx(stackEl);
        })

    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

.grid {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 0 7em;
    perspective: 2000px;
    perspective-origin: 50% 100%;
    height: 800px;
    overflow: scroll;
    padding: 90px 30px;
}

.grid__item {
    position: relative;
    display: block;
    flex: none;
    width: 250px;
    margin: 1.5em 2vw;
    cursor: default;
    transform-style: preserve-3d;
}

.grid__item:hover,
.grid__item:focus {
    outline: none;
}


.stack {
    position: relative;
    width: 100%;
    height: 200px;
    transform-style: preserve-3d;

    &>div {
        border-radius: 20px;
    }
}

.stack__deco {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: currentColor;
    transform-origin: 50% 100%;
}

.stack__deco:first-child {
    opacity: 0.2;
}

.stack__deco:nth-child(2) {
    opacity: 0.4;
}

.stack__deco:nth-child(3) {
    opacity: 0.6;
}

.stack__deco:nth-child(4) {
    opacity: 0.8;
}

.stack__cover {
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    height: 100%;
    padding: 20px;
    cursor: pointer;
    transform-origin: 50% 100%;

    .article-title {
        word-wrap: break-word;
        white-space: pre-wrap;
    }

    .theme0 & {
        background-color: $theme0-path-fill-2;
    }

    .theme1 & {
        background-color: $theme1-path-fill-2;
    }

    .theme2 & {
        background-color: $theme2-path-fill-2;
    }

}

.description {
    margin-top: 20px;
    font-size: 14px;

    .content {
        padding-left: 1em;
    }

    .theme0 & {
        .title {
            color: $theme0-path-fill-4;
        }

        .content {
            color: $theme0-path-fill-3;
        }
    }

    .theme1 & {
        .title {
            color: $theme1-path-fill-4;
        }

        .content {
            color: $theme1-path-fill-3;
        }
    }

    .theme2 & {
        .title {
            color: $theme2-path-fill-4;
        }

        .content {
            color: $theme2-path-fill-3;
        }
    }
}



.grid {
    perspective-origin: 50% -50%;
}

.grid .stack__cover,
.grid .stack__deco {
    transform-origin: 50% 100%;
}
</style>
