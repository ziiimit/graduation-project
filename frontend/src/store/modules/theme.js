const state = {
    themes: [
        {
            title_zh: '心理健康与成瘾',
            title_en: "Mental Health and Addiction",
        },
        {
            title_zh: '专注力，效率与创造力',
            title_en: "Focus, Productivity and Creativity",
        },
        {
            title_zh: '健康生活的科学',
            title_en: "The Science of Well-being",
        }
    ],
    themeColors: {
        "Mental Health and Addiction": "theme0",
        "Focus, Productivity and Creativity": "theme1",
        "The Science of Well-being": "theme2",
    }

}


export default {
    namespaced: true,
    state,
}