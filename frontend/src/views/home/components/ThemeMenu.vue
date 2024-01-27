<template>
    <div id="theme-menu">
        <ul>
            <li v-for="(item, index) in themes" :class="{ active: currentThemeIndex == index }" @click="changeTheme(index)">
            </li>
        </ul>
    </div>
</template>
<script>
export default {
    name: "HomeThemeMenu",
    data() {
        return {
            themes: this.$store.state.theme.themes
        }
    },
    computed: {
        currentThemeIndex() {
            return this.$store.state.theme.currentThemeIndex
        }
    },
    methods: {
        changeTheme(index) {
            this.$store.commit('theme/setCurrentThemeIndex', index)
        }
    }
}
</script>
<style scoped lang='scss'>
@import "@/style/color.scss";

#theme-menu {
    position: absolute;
    z-index: 10;
    width: 100vw;
    bottom: 30px;
}

ul {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
}

li {
    width: 10px;
    height: 10px;
    border-radius: 50%;

    cursor: pointer;

    .theme0 & {
        background-color: $theme0-menu-not-active;
    }

    .theme1 & {
        background-color: $theme1-menu-not-active;
    }

    .theme2 & {
        background-color: $theme2-menu-not-active;
    }



    .theme0 &.active {
        background-color: $theme0-menu-active
    }

    .theme1 &.active {
        background-color: $theme1-menu-active
    }

    .theme2 &.active {
        background-color: $theme2-menu-active
    }
}
</style>
