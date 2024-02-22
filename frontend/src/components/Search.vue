<template>
    <div id="search">
        <svg class="hidden">
            <defs>
                <symbol id="icon-search" viewBox="0 0 24 24">
                    <path
                        d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" />
                </symbol>
                <symbol id="icon-cross" viewBox="0 0 24 24">
                    <path
                        d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
                </symbol>
            </defs>
        </svg>


        <!-- 搜索按钮 -->
        <button id="btn-search" class="btn btn--search" @click="openSearch"><svg class="icon">
                <use xlink:href="#icon-search"></use>
            </svg></button>

        <!-- 搜索主体 -->
        <div class="search" :class="{ 'search--open': searchOpened }">
            <button id="btn-search-close" class="btn btn--search-close" aria-label="Close search form"
                @click="closeSearch"><svg class="icon icon--cross">
                    <use xlink:href="#icon-cross"></use>
                </svg></button>
            <div class="search__form">
                <input class="search__input" name="search" autocomplete="off" autocorrect="off" autocapitalize="off"
                    spellcheck="false" @keyup.enter="search" v-model="inputContent" />
                <span class="search__info">按回车键触发搜索</span>
            </div>
            <div class="search__related">
                <div class="search__suggestion" v-for="item in searchSuggestions" :key="item.title">
                    <h3>{{ item.title }}</h3>
                    <p>{{ item.content }}
                    </p>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
export default {
    name: "Search",
    data() {
        return {
            searchOpened: false,
            searchSuggestions: [
                {
                    title: "我可以输入什么?",
                    content: "没有特定的限制，可以是一个问题，一个感兴趣的话题，甚至是对当前心情的描述。"
                },
                {
                    title: "App会返回什么？",
                    content: "我们会从数据库中的所有文本数据内，查找和你的输入最相关的那些内容，在做出回答的同时，推荐给你可能感兴趣的文章。"
                },
                {
                    title: "输入示例",
                    content: "1) 什么是OCD? \n2) 我最近有点失眠。 \n3) 如何提升专注力？"
                }
            ],
            inputContent: ""
        }
    },
    methods: {
        openSearch() {
            // @ts-ignore
            this.searchOpened = true;
            let searchContainer = document.querySelector('.search');
            // @ts-ignore
            let inputSearch = searchContainer.querySelector('.search__input');
            // @ts-ignore
            inputSearch.focus();

        },
        closeSearch() {
            // @ts-ignore
            this.searchOpened = false;
            let searchContainer = document.querySelector('.search');
            // @ts-ignore
            let inputSearch = searchContainer.querySelector('.search__input')
            // @ts-ignore
            inputSearch.blur();

        },
        search() {
            this.closeSearch()
            this.$router.push({ name: "SearchResult", query: { input: this.inputContent } })
        }
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";


#search {
    position: absolute;
    width: 100%;
    z-index: 2000;
}


.icon {
    display: block;
    width: 1.5em;
    height: 1.5em;
    margin: 0 auto;
}


/* 搜索按钮以及取消按钮 */

.btn--search {
    position: absolute;
    font-size: 1.5em;
    right: 40px;
    top: 20px;
    color: rgb(133, 133, 133);
}

.btn--search-close {
    color: rgb(51, 61, 80);
}


// 搜索主体
.search {
    position: fixed;
    z-index: 2000;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: rgba(255, 255, 255, 0.843);
}


.search::before,
.search::after {
    content: '';
    position: absolute;
    width: calc(100% + 15px);
    height: calc(100% + 15px);
    pointer-events: none;
    border: 1.5em solid rgb(51, 61, 80);
}

.search::before {
    top: 0;
    left: 0;
    border-right-width: 0;
    border-bottom-width: 0;
}

.search::after {
    right: 0;
    bottom: 0;
    border-top-width: 0;
    border-left-width: 0;
}

.btn--search-close {
    font-size: 2em;
    position: absolute;
    top: 1.25em;
    right: 1.25em;
    display: block;
}

.search__form {
    margin: 5em 0;
}

/* Reset Search Input */

.search__input {
    border: 0;
    background: transparent;
    border-radius: 0;
}

.search__input:focus {
    outline: none;
}

.search__input {
    font-family: inherit;
    font-size: 10vw;
    line-height: 1;
    display: inline-block;
    box-sizing: border-box;
    width: 75%;
    padding: 0.05em 0;
    color: rgb(51, 61, 80);
    border-bottom: 2px solid rgba(51, 61, 80, 0.615);
}

.search__input::-webkit-search-cancel-button,
.search__input::-webkit-search-decoration {
    -webkit-appearance: none;
}

.search__input::-ms-clear {
    display: none;
}

.search__info {
    font-size: 90%;
    font-weight: bold;
    display: block;
    width: 75%;
    margin: 0 auto;
    padding: 0.85em 0;
    text-align: right;
    color: rgba(51, 61, 80, 0.688);

}

.search__related {
    display: flex;
    width: 75%;
    pointer-events: none;
}

.search__suggestion {
    width: 33.33%;
    text-align: left;
    color: rgb(51, 61, 80)
}

.search__suggestion:nth-child(2) {
    margin: 0 3em;
}

.search__suggestion h3 {
    font-size: 1.35em;
    margin: 0;
}

.search__suggestion h3::before {
    content: '\21FE';
    display: inline-block;
    padding: 0 0.5em 0 0;
}

.search__suggestion p {
    font-size: 1.15em;
    line-height: 1.4;
    margin: 0.75em 0 0 0;
    white-space: pre-line;
}

/************************/
/* Transitions 			*/
/************************/

.search {
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.5s;
}

.search--open {
    pointer-events: auto;
    opacity: 1;
}

/* Border */
.search::before,
.search::after {
    transition: transform 0.5s;
}

.search::before {
    transform: translate3d(-15px, -15px, 0);
}

.search::after {
    transform: translate3d(15px, 15px, 0);
}

.search--open::before,
.search--open::after {
    transform: translate3d(0, 0, 0);
}

/* Close button */
.btn--search-close {
    opacity: 0;
    transform: scale3d(0.8, 0.8, 1);
    transition: opacity 0.5s, transform 0.5s;
}

.search--open .btn--search-close {
    opacity: 1;
    transform: scale3d(1, 1, 1);
}

/* Search form with input and description */
.search__form {
    opacity: 0;
    transform: scale3d(0.8, 0.8, 1);
    transition: opacity 0.5s, transform 0.5s;
}

.search--open .search__form {
    opacity: 1;
    transform: scale3d(1, 1, 1);
}

.search__suggestion {
    opacity: 0;
    transform: translate3d(0, -30px, 0);
    transition: opacity 0.5s, transform 0.5s;
}

.search--open .search__suggestion {
    opacity: 1;
    transform: translate3d(0, 0, 0);
}

.search--open .search__suggestion:nth-child(2) {
    transition-delay: 0.1s;
}

.search--open .search__suggestion:nth-child(3) {
    transition-delay: 0.2s;
}

@media screen and (max-width:40em) {
    .search__form {
        margin: 5em 0 1em;
    }

    .btn--search-close {
        font-size: 1.25em;
        top: 1.5em;
        right: 1.5em;
    }

    .search__info {
        text-align: left;
    }

    .search__suggestion {
        font-size: 80%;
        width: 100%;
    }

    .search__suggestion:nth-child(2),
    .search__suggestion:nth-child(3) {
        display: none;
    }
}
</style>
