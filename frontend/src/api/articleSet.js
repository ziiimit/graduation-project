import axios from 'axios';

export function getThemeArticleSetList(params) {
    return new Promise((resolve, reject) => {
        axios.get('/themeArticleSet/articleSetList', {
            params
        }).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err);
        })
    })
}

export function getArticleSet(params) {
    return new Promise((resolve, reject) => {
        axios.get('/themeArticleSet/articleSet', {
            params
        }).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err);
        })
    })
}

export function getArticle(params) {
    return new Promise((resolve, reject) => {
        axios.get('/themeArticleSet/article', {
            params
        }).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err);
        })
    })
}


