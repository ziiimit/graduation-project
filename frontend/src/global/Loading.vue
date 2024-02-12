<template>
    <div class="loading"></div>
</template>
  
<script>
export default {

};
</script>
  
<style scoped lang="scss">
@import "@/style/color.scss";

.loading {
    display: flex;
    justify-content: center;
    align-items: center;
}

.loading::after {
    content: "";
    width: 30px;
    height: 30px;
    border: 3px solid transparent;
    border-radius: 50%;
    animation: loading 1s ease infinite;
    border-top-color: #353d4e; // defalut color

    .theme0 & {
        border-top-color: $theme0-path-fill-3;
    }

    .theme1 & {
        border-top-color: $theme1-path-fill-3;
    }

    .theme2 & {
        border-top-color: $theme2-path-fill-3;
    }
}

@keyframes loading {
    to {
        transform: rotate(1turn);
    }
}
</style>