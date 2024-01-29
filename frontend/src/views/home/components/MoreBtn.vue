<template>
    <div class="button-more" @click="showCurtain">
        <button @click="showCurtain">
            <svg aria-hidden="true" class="progress" width="70" height="70" viewbox="0 0 70 70">
                <path class="progress__circle"
                    d="m35,2.5c17.955803,0 32.5,14.544199 32.5,32.5c0,17.955803 -14.544197,32.5 -32.5,32.5c-17.955803,0 -32.5,-14.544197 -32.5,-32.5c0,-17.955801 14.544197,-32.5 32.5,-32.5z" />
                <path class="progress__path"
                    d="m35,2.5c17.955803,0 32.5,14.544199 32.5,32.5c0,17.955803 -14.544197,32.5 -32.5,32.5c-17.955803,0 -32.5,-14.544197 -32.5,-32.5c0,-17.955801 14.544197,-32.5 32.5,-32.5z"
                    pathLength="1" />
            </svg>
        </button>
        <span class="text">More</span>
    </div>
</template>
<script>
export default {
    name: "HomeMoreBtn",
    methods: {
        showCurtain() {
            this.$emit("showCurtain")
        }
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

.button-more {
    position: relative;


    .text {
        position: absolute;
        transition: all 0.4s;
        left: 30px;
        top: 39px;
        font-weight: 500;
        cursor: pointer;

        .theme0 & {
            color: $theme0-moreBtn-text
        }

        .theme1 & {
            color: $theme1-moreBtn-text
        }

        .theme2 & {
            color: $theme2-moreBtn-text
        }
    }

}

.button-more button {
    width: 100px;
    height: 100px;
    cursor: pointer;
    border: none;
    position: relative;
    background: none;
    -webkit-clip-path: circle(50% at 50% 50%);
    clip-path: circle(50% at 50% 50%);

}

.progress {
    position: absolute;
    top: calc(50% - 36px);
    left: calc(50% - 36px);
    transition: transform 0.4s cubic-bezier(0.7, 0, 0.3, 1);
    background-color: #ffffff50;
    border-radius: 50%;
}

.button-more:hover {
    .progress {
        transform: scale3d(1.2, 1.2, 1);
    }

    .text {
        // font-size: 20px;
        font-weight: 500;
    }
}



.progress__circle,
.progress__path {
    fill: none;
    stroke: #f0f0f0;
    stroke-width: 1px;
}


.progress__path {
    .theme0 & {
        stroke: $theme0-moreBtn-cricle
    }

    .theme1 & {
        stroke: $theme1-moreBtn-cricle
    }

    .theme2 & {
        stroke: $theme2-moreBtn-cricle
    }

    stroke-dasharray: 1;
    stroke-dashoffset: 1;
    transition: stroke-dashoffset 0.4s cubic-bezier(0.7, 0, 0.3, 1);
}

.button-more:hover .progress__path {
    stroke-dashoffset: 0;
}
</style>
