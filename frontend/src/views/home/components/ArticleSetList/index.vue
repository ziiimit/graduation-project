<template>
    <div id="article-set-list">

        <div class="top-bar" :class="{ 'visible': listVisible }">
            <button class="home-btn" @click="changeVisibility">
                <svg xmlns=" http://www.w3.org/2000/svg" x="0px" y="0px" width="30" height="30" viewBox="0 0 24 24"
                    class="icon">
                    <path
                        d="M 12 2 A 1 1 0 0 0 11.289062 2.296875 L 1.203125 11.097656 A 0.5 0.5 0 0 0 1 11.5 A 0.5 0.5 0 0 0 1.5 12 L 4 12 L 4 20 C 4 20.552 4.448 21 5 21 L 9 21 C 9.552 21 10 20.552 10 20 L 10 14 L 14 14 L 14 20 C 14 20.552 14.448 21 15 21 L 19 21 C 19.552 21 20 20.552 20 20 L 20 12 L 22.5 12 A 0.5 0.5 0 0 0 23 11.5 A 0.5 0.5 0 0 0 22.796875 11.097656 L 12.716797 2.3027344 A 1 1 0 0 0 12.710938 2.296875 A 1 1 0 0 0 12 2 z">
                    </path>
                </svg>
            </button>
        </div>



        <div class="list" :class="{ visible: listVisible }">
            <List />
        </div>


        <svg class="shape-overlays" viewBox="0 0 100 100" preserveAspectRatio="none">
            <path class="shape-overlays__path"></path>
            <path class="shape-overlays__path"></path>
            <path class="shape-overlays__path"></path>
            <path class="shape-overlays__path"></path>
        </svg>
    </div>
</template>
<script>
import List from './List.vue'
export default {
    name: "HomeArticleSetList",
    components: { List },
    data() {
        return {
            elm: null,
            path: null,
            numPoints: 4,
            duration: 800,
            delayPointsArray: [],
            delayPointsMax: 180,
            delayPerPath: 70,
            timeStart: null,
            isOpened: false,
            isAnimating: false,
            listVisible: false,
        }
    },
    methods: {
        cubicInOut: (t) => {
            return t < 0.5
                ? 4.0 * t * t * t
                : 0.5 * Math.pow(2.0 * t - 2.0, 3.0) + 1.0;
        },
        toggle() {
            this.isAnimating = true;
            const range = Math.random() * Math.PI * 2;
            for (var i = 0; i < this.numPoints; i++) {
                const radian = (i / (this.numPoints - 1)) * Math.PI * 2;
                // @ts-ignore
                this.delayPointsArray[i] = (Math.sin(radian + range) + 1) / 2 * this.delayPointsMax;
            }
            if (this.isOpened === false) {
                this.open();
                setTimeout(() => {
                    this.listVisible = true
                }, 1000)
            } else {
                this.close();
                this.listVisible = false
            }
        },
        open() {
            this.isOpened = true;
            // @ts-ignore
            this.elm.classList.add('is-opened');
            // @ts-ignore
            this.timeStart = Date.now();
            this.renderLoop();
        },
        close() {
            this.isOpened = false;
            // @ts-ignore
            this.elm.classList.remove('is-opened');
            // @ts-ignore
            this.timeStart = Date.now();
            this.renderLoop();
            this.$emit('closed');
        },
        updatePath(time) {
            const points = [];
            for (var i = 0; i < this.numPoints; i++) {
                // @ts-ignore
                points[i] = this.cubicInOut(Math.min(Math.max(time - this.delayPointsArray[i], 0) / this.duration, 1)) * 100
            }

            let str = '';
            str += (this.isOpened) ? `M 0 0 V ${points[0]} ` : `M 0 ${points[0]} `;
            for (var i = 0; i < this.numPoints - 1; i++) {
                const p = (i + 1) / (this.numPoints - 1) * 100;
                const cp = p - (1 / (this.numPoints - 1) * 100) / 2;
                str += `C ${cp} ${points[i]} ${cp} ${points[i + 1]} ${p} ${points[i + 1]} `;
            }
            str += (this.isOpened) ? `V 0 H 0` : `V 100 H 0`;
            return str;
        },
        render() {
            if (this.isOpened) {
                // @ts-ignore
                for (var i = 0; i < this.path.length; i++) {
                    // @ts-ignore
                    this.path[i].setAttribute('d', this.updatePath(Date.now() - (this.timeStart + this.delayPerPath * i)));
                }
            } else {
                // @ts-ignore
                for (var i = 0; i < this.path.length; i++) {
                    // @ts-ignore
                    this.path[i].setAttribute('d', this.updatePath(Date.now() - (this.timeStart + this.delayPerPath * (this.path.length - i - 1))));
                }
            }
        },
        renderLoop() {
            this.render();
            // @ts-ignore
            if (Date.now() - this.timeStart < this.duration + this.delayPerPath * (this.path.length - 1) + this.delayPointsMax) {
                requestAnimationFrame(() => {
                    this.renderLoop();
                });
            }
            else {
                this.isAnimating = false;
            }
        },
        changeVisibility() {
            // @ts-ignore
            this.elm = document.querySelector('.shape-overlays');
            // @ts-ignore
            this.path = document.querySelectorAll('.shape-overlays__path');
            // @ts-ignore
            this.timeStart = Date.now();
            if (this.isAnimating) {
                return false;
            }
            this.toggle();

        }
    }

}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

.top-bar {
    height: 90px;
    width: 100%;
    position: fixed;
    z-index: 1000;
    top: 0;
    left: 0;
    opacity: 0;
    transition: opacity 0.2s;

    .theme0 & {
        background: linear-gradient($theme0-path-fill-4 60%, transparent);
    }

    .theme1 & {
        background: linear-gradient($theme1-path-fill-4 60%, transparent);
    }

    .theme2 & {
        background: linear-gradient($theme2-path-fill-4 60%, transparent);
    }

    &.visible {
        opacity: 1;
    }
}

.home-btn {
    position: fixed;
    top: 20px;
    left: 40px;
    color: white;
    pointer-events: none;

    .visible & {
        opacity: 0.8;
        pointer-events: auto;

        &:hover {
            opacity: 1;
        }
    }

}

.list {
    position: fixed;
    z-index: 100;
    top: 0;
    left: 0;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
    overflow: scroll;
    width: 100%;
    height: 100vh;

    &.visible {
        pointer-events: auto;
        opacity: 1;
    }
}

.shape-overlays {
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    position: fixed;
    top: 0;
    left: 0;

    &.is-opened {
        pointer-events: auto;

    }
}


.shape-overlays__path:nth-of-type(1) {
    .theme0 & {
        fill: $theme0-path-fill-1
    }

    .theme1 & {
        fill: $theme1-path-fill-1
    }

    .theme2 & {
        fill: $theme2-path-fill-1
    }

}

.shape-overlays__path:nth-of-type(2) {
    .theme0 & {
        fill: $theme0-path-fill-2
    }

    .theme1 & {
        fill: $theme1-path-fill-2
    }

    .theme2 & {
        fill: $theme2-path-fill-2
    }
}

.shape-overlays__path:nth-of-type(3) {
    .theme0 & {
        fill: $theme0-path-fill-3
    }

    .theme1 & {
        fill: $theme1-path-fill-3
    }

    .theme2 & {
        fill: $theme2-path-fill-3
    }
}

.shape-overlays__path:nth-of-type(4) {
    .theme0 & {
        fill: $theme0-path-fill-4
    }

    .theme1 & {
        fill: $theme1-path-fill-4
    }

    .theme2 & {
        fill: $theme2-path-fill-4
    }
}
</style>
