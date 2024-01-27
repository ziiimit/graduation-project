const state = {
    themes: [
        {
            themeName_zh: '心理健康与成瘾',
            themeName_en: "Mental Health and Addiction",
        },
        {
            themeName_zh: '专注力，效率与创造力',
            themeName_en: "Focus, Productivity and Creativity",
        },
        {
            themeName_zh: '健康生活的科学',
            themeName_en: "The Science of Well-being",
        }
    ],
    currentThemeIndex: 0
}

const mutations = {
    setCurrentThemeIndex: (state, currentThemeIndex) => {
        state.currentThemeIndex = currentThemeIndex
    }
}


export default {
    namespaced: true,
    state,
    mutations
}