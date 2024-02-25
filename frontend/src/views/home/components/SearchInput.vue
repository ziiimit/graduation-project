<template>
    <div id="search" class="demo-2">
        <svg class="hidden">
            <defs>
                <symbol id="icon-arrow" viewBox="0 0 24 24">
                    <title>arrow</title>
                    <polygon points="6.3,12.8 20.9,12.8 20.9,11.2 6.3,11.2 10.2,7.2 9,6 3.1,12 9,18 10.2,16.8 " />
                </symbol>
                <symbol id="icon-drop" viewBox="0 0 24 24">
                    <title>drop</title>
                    <path
                        d="M12,21c-3.6,0-6.6-3-6.6-6.6C5.4,11,10.8,4,11.4,3.2C11.6,3.1,11.8,3,12,3s0.4,0.1,0.6,0.3c0.6,0.8,6.1,7.8,6.1,11.2C18.6,18.1,15.6,21,12,21zM12,4.8c-1.8,2.4-5.2,7.4-5.2,9.6c0,2.9,2.3,5.2,5.2,5.2s5.2-2.3,5.2-5.2C17.2,12.2,13.8,7.3,12,4.8z" />
                    <path
                        d="M12,18.2c-0.4,0-0.7-0.3-0.7-0.7s0.3-0.7,0.7-0.7c1.3,0,2.4-1.1,2.4-2.4c0-0.4,0.3-0.7,0.7-0.7c0.4,0,0.7,0.3,0.7,0.7C15.8,16.5,14.1,18.2,12,18.2z" />
                </symbol>
                <symbol id="icon-search" viewBox="0 0 24 24">
                    <title>search</title>
                    <path
                        d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" />
                </symbol>
                <symbol id="icon-cross" viewBox="0 0 24 24">
                    <title>cross</title>
                    <path
                        d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
                </symbol>
            </defs>
        </svg>
        <div class="search" :class="{ 'search--open': isSearchOpened }">
            <button id="btn-search-close" class="btn btn--search-close" aria-label="Close search form"
                @click="closeSearch"><svg class="icon icon--cross">
                    <use xlink:href="#icon-cross"></use>
                </svg></button>
            <div class="search__form">

                <input id="search-input" class="search__input" name="search" placeholder="有一个问题/想法？" autocomplete="off"
                    autocorrect="off" autocapitalize="off" spellcheck="false" @focus="openSearch"
                    @keyup.enter="(e) => search(e)" />
                <button class="btn btn--search"><svg class="icon icon--search">
                        <use xlink:href="#icon-search"></use>
                    </svg></button>
            </div>

            <div class="search__suggestion">
                <h3>输入示例</h3>
                <ul>
                    <li>什么是OCD?</li>
                    <li>为什么每次在我取得成功以后，都有种怅然若失的感觉？</li>
                    <li>晚上不想刷牙</li>
                </ul>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "Search",
    data() {
        return {
            isSearchOpened: false
        }
    },
    methods: {
        openSearch() {
            this.isSearchOpened = true;
        },
        closeSearch() {
            const inputSearch = document.querySelector('.search .search__input');
            inputSearch.blur();
            inputSearch.value = '';
            this.isSearchOpened = false;
        },
        search(e) {
            e.preventDefault()
            const userInput_zh = e.target.value
            this.$router.push({ name: 'SearchResult', query: { userInput_zh } })
        }
    },

}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";

.hidden {
    position: absolute;
    overflow: hidden;
    width: 0;
    height: 0;
    pointer-events: none;
}

.icon {
    display: block;
    width: 1.5em;
    height: 1.5em;
    margin: 0 auto;
    fill: currentColor;
}


/* Reset Buttons */
.btn {
    margin: 0;
    padding: 0;
    cursor: pointer;
    border: none;
    background: none;
    text-decoration: none;
    outline: none;

    &:focus {
        outline: none;
    }
}

.btn--search {
    font-size: 3em;
    position: absolute;
    right: 0;
    bottom: 0.5em;
    pointer-events: none;
}

.search--open .btn--search {
    pointer-events: auto;
}


.search {
    position: absolute;
    z-index: 101;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;

    &.search--open {
        background-color: #dbd3cde1;
    }
}

.search__form {
    position: relative;
    top: 0px;
    width: 60%;
    min-width: 300px;
    margin: 0 auto;
}

.search__input {
    border: 0;
    background: transparent;
    border-radius: 0;
    -webkit-appearance: none;

    &:focus {
        outline: none;
    }
}

.search__input {
    font-family: inherit;
    font-size: 4em;
    display: inline-block;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    width: 100%;
    padding: 0 1em 0.15em 0;
    pointer-events: auto;
    border-bottom: 4px solid;
}

.search__input::-webkit-search-cancel-button,
.search__input::-webkit-search-decoration {
    -webkit-appearance: none;
}

.search__input::-ms-clear {
    display: none;
}


.search__suggestion {
    width: 50%;
    max-width: 450px;
    margin: calc(40vh + 2em) auto 0;
    text-align: left;
    pointer-events: none;
}

.search__suggestion:nth-child(2) {
    margin: 0 3em;
}

.search__suggestion h3 {
    font-size: 1.5em;
    margin: 0;
}

.search__suggestion h3::before {
    content: '\21FE';
    display: inline-block;
    padding: 0 0.5em 0 0;
}

.search__suggestion li {
    font-size: 1.25em;
    line-height: 1.4;
    margin: 0.75em 0 0 0;
}

.search--open {
    pointer-events: auto;
}

.search__form {
    transform: translate3d(0, 40px, 0) scale3d(0.5, 0.5, 1);
    transition: transform 0.5s;
    transition-timing-function: cubic-bezier(0.7, 0, 0.3, 1);
}

.search--open .search__form {
    transform: translate3d(0, 40vh, 0) translate3d(0, -50%, 0);
}

.btn--search-close {
    font-size: 2em;
    position: absolute;
    z-index: 4;
    top: 1.25em;
    right: 1.25em;
    opacity: 0;
    pointer-events: none;
    transform: scale3d(0.8, 0.8, 1);
    transition: opacity 0.5s, transform 0.5s;
    transition-timing-function: cubic-bezier(0.7, 0, 0.3, 1);
}

.search--open .btn--search-close {
    opacity: 1;
    transform: scale3d(1, 1, 1);
    transition-delay: 0.1s;
    pointer-events: auto;
}

/* Dummy blocks */
.search__suggestion h3,
.search__suggestion li {
    opacity: 0;
    transform: translate3d(0, 100px, 0);
    transition: opacity 0.2s, transform 0.5s;
    transition-timing-function: cubic-bezier(0.7, 0, 0.3, 1);
}

.search--open .search__suggestion h3,
.search--open .search__suggestion li {
    opacity: 1;
    transform: translate3d(0, 0, 0);
    transition: opacity 0.5s, transform 0.5s;
    transition-timing-function: cubic-bezier(0.7, 0, 0.3, 1);
}

.search--open .search__suggestion li {
    transition-delay: 0.1s;
}

@media screen and (max-width: 40em) {
    .search__form {
        width: 100%;
        padding: 2em 1em 0;
    }

    .search__input {
        font-size: 2em;
    }

    .btn--search {
        font-size: 1.25em;
        right: 1em;
    }

    .btn--search-close {
        font-size: 1.15em;
    }

    .search__suggestion {
        font-size: 0.85em;
        width: 100%;
        margin-top: 40vh;
        padding: 0 1em;
    }
}
</style>
