<template>
    <div id="response">
        <div class="msg right-msg">
            <div class="msg-header">YOU</div>
            <div class="msg-bubble">
                <div class="msg-text">{{ userInput }}</div>
            </div>
        </div>
        <div class="msg left-msg">

            <div class="msg-header">APP</div>
            <div class="msg-bubble">
                <div class="msg-text">
                    <div id="response-content"></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "Response",
    props: ['response'],
    data() {
        return {
            userInput: this.$route.query['input'],
        }
    },
    methods: {
        typeWriter(text, i) {
            if (i < (text.length)) {
                document.querySelector("#response-content").innerHTML = text.substring(0, i + 1);
                setTimeout(() => {
                    this.typeWriter(text, i + 1)
                }, 80);
            } else {
                this.$emit('typingFinished')
            }
        },
    },
    mounted() {
        this.typeWriter(this.response, 0);
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";


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
    background: #ddd;
    font-size: 16px;
    font-weight: 500;
}


.msg-bubble {
    max-width: 450px;
    padding: 15px;
    border-radius: 15px;
    font-size: 14px;
}

.left-msg .msg-bubble {
    border-top-left-radius: 0;
    background: $search-main;
    color: white
}

.right-msg {
    flex-direction: row-reverse;
}

.right-msg .msg-bubble {
    background: #c8c8c8;
    color: $article-font;
    border-top-right-radius: 0;
}

.right-msg .msg-header {
    margin: 0 0 0 10px;
}
</style>
