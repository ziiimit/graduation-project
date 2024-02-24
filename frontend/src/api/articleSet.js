import axios from 'axios';


//获取某个theme下的as列表
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

// 获取某个as下的所有article列表
export function getArticleSet(articleSetTitle_en) {
    const params = {
        articleSetTitle_en
    }
    return new Promise((resolve, reject) => {
        axios.get('/articleSet', {
            params
        }).then(res => {
            resolve(res.data)
        }).catch(err => {
            reject(err)
        })
    })
}

