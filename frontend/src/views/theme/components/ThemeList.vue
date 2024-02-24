<template>
    <div id="theme-list">
        <ul>
            <li v-for="theme in themeList" :class="[theme.themeColor]" @click="navigateToTheme(theme['title_en'])">
                <div class="title">
                    <div class="title-zh">{{ theme['title_zh'] }}</div>
                    <div class="title-en">{{ theme['title_en'] }}</div>
                </div>
            </li>
        </ul>
    </div>
</template>
<script>
export default {
    name: "ThemeList",
    data() {
        return {
            // @ts-ignore
            themeList: this.$store.state.theme.themes,
        }
    },
    methods: {
        navigateToTheme(title_en) {
            this.$emit("navigate", title_en)
        },
    }

}
</script>
<style scoped lang='scss'>
@import "@/style/variable.scss";

#theme-list {
    transition: opacity 0.2s;
}

ul {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 30px;
    overflow: scroll;
}

li {
    text-align: center;
    cursor: pointer;

    &.theme0:hover [class^="title"] {
        color: $theme0;
    }

    &.theme1:hover [class^="title"] {
        color: $theme1;
    }

    &.theme2:hover [class^="title"] {
        color: $theme2;
    }
}



.title-zh {
    font-size: 50px;
    font-weight: 600;
    font-family: serif;
    transition: color 0.2s;

}

.title-en {
    font-size: 30px;
    font-family: cursive;
    transition: color 0.2s;
}
</style>
