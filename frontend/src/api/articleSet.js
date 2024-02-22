import axios from 'axios';

export function getArticleSetList(themeTitle_en) {
    const params = {
        themeTitle_en
    }
    return new Promise((resolve, reject) => {
        axios.get('/articleSetList', {
            params
        }).then(res => {
            resolve(res.data)
        }).catch(err => {
            reject(err)
        })
    })
}


// params = theme = {themeName_en}
// export function getThemeArticleSetList(params) {
//     return new Promise((resolve, reject) => {
//         axios.get('/articleSetList', {
//             params
//         }).then(res => {
//             resolve(res.data);
//         }).catch(err => {
//             reject(err);
//         })
//     })
// }

// // params = articleSet = {title}
// export function getArticleSet(params) {
//     return new Promise((resolve, reject) => {
//         axios.get('/themeArticleSet/articleSet', {
//             params
//         }).then(res => {
//             resolve(res.data);
//         }).catch(err => {
//             reject(err);
//         })
//     })
// }

// // params = article = {title,id}
// export function getArticle(params) {
//     return new Promise((resolve, reject) => {
//         axios.get('/themeArticleSet/article', {
//             params
//         }).then(res => {
//             resolve(res.data);
//         }).catch(err => {
//             reject(err);
//         })
//     })
// }


