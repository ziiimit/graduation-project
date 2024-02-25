<template>
    <div id="loading"></div>
</template>
  
<script>
export default {
};
</script>
  
<style scoped lang="scss">
@import "@/style/variable.scss";

#loading {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
}

#loading {
    display: flex;
    justify-content: center;
    align-items: center;
}

#loading::after {
    content: "";
    width: 50px;
    height: 50px;
    border: 3px solid transparent;
    border-radius: 50%;
    animation: loading 1s ease infinite;
    border-top-color: #353d4e; // defalut color

    .theme0 & {
        border-top-color: $theme0;
    }

    .theme1 & {
        border-top-color: $theme1;
    }

    .theme2 & {
        border-top-color: $theme2;
    }
}

@keyframes loading {
    to {
        transform: rotate(1turn);
    }
}
</style>