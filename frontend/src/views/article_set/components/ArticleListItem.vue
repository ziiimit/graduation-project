<template>
    <div id="article-list-item">
        <div class="letter">
            <div class="title">
                <div class="title_zh">{{ articleTitle_zh }}</div>
                <div class="title_en">{{ articleTitle_en }}</div>
            </div>
            <p>{{ summary_zh }}</p>
        </div>
    </div>
</template>
<script>
export default {
    name: "",
    props: ['articleTitle_zh', 'articleTitle_en', 'summary_zh']
}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";

.letter {
    cursor: pointer;

    .title {
        text-align: center;

        .title_zh {
            font-size: 16px;

            .theme0 & {
                color: $theme0;
            }

            .theme1 & {
                color: $theme1;
            }

            .theme2 & {
                color: $theme2;
            }
        }

        .title_en {
            color: #585858;
        }
    }

    p {
        font-size: 13px;
        text-indent: 2em;
        color: #323232;
    }
}


.letter {
    background: #d0d0d0;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    margin: 26px auto 0;
    max-width: 550px;
    min-height: 200px;
    padding: 24px;
    position: relative;
    width: 80%;
    z-index: 4;
    font-size: 14px;
    transition: all 0.3s;
}

.letter::before,
.letter::after {
    content: "";
    height: 98%;
    position: absolute;
    width: 100%;
    z-index: -1;
    transition: all 0.4s;

}

.letter::before {
    background: #dcdbdb;
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
    left: -5px;
    top: 4px;
    transform: rotate(-2.5deg);
}

.letter::after {
    background: #ebebeb;
    box-shadow: 0 0 3px rgba(0, 0, 0, 0.2);
    right: -3px;
    top: 1px;
    transform: rotate(1.4deg);

}

.letter:hover {
    &::before {
        left: -6px;
        top: -10px;
        transform: rotate(-10deg);
    }

    & {
        transform: rotate(3deg);
    }


}
</style>
