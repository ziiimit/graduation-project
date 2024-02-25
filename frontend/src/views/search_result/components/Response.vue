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
    props: ['response_zh', 'userInput_zh'],
    data() {
        return {
            nextMessageIndex: 1,
        }
    },
    methods: {
        typeWriter(text, i, resolve) {
            if (i < (text.length)) {
                document.querySelector("#response-content").innerHTML = text.substring(0, i + 1);
                setTimeout(() => {
                    this.typeWriter(text, i + 1, resolve)
                }, 40);
            } else {
                resolve()
            }
        },
        typeMessage(message) {
            return new Promise((resolve, reject) => {
                this.typeWriter(message, 0, resolve)
            })
        },
    },
    mounted() {
        this.typeMessage(this.response_zh);
    }
}
</script>
<style scoped lang='scss'>
$header-bg: #31363b;
$msg-bg: #717579;

#response {
    width: 80vw;
    height: calc(100vh - 80px);
    padding: 30px 20px 100px;
    margin: 0 auto;
    max-width: 900px;
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
}

.left-msg .msg-bubble {
    border-top-left-radius: 0;
    text-indent: 2em;
    width: clamp(300px, 50%, 450px);
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
</style>
