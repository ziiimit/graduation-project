<template>
    <div id="article">
        <h2 class="title">{{ article['title'] }}</h2>
        <ul class="paragraph-list">
            <li v-for="paragraph in article['paragraphs']">
                {{ paragraph['content'] }}
            </li>
        </ul>
    </div>
</template>
<script>
export default {
    name: "Article",
    props: ['article']
}
</script>
<style scoped lang='scss'>
.title {
    font-size: 30px;
    padding: 20px;
    text-align: center;
}

.paragraph-list {
    height: calc(100vh - 150px);
    overflow: scroll;
    padding: 20px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
    border-radius: 20px;

    li {
        text-indent: 2em;
        font-size: 18px;
        padding-bottom: 20px;
        max-width: 800px;
        margin: auto;
    }
}
</style>
