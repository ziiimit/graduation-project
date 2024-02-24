import axios from 'axios';


//获取某个theme下的as列表
export function getArticle(articleSetTitle_en, articleSequence) {
    const params = {
        articleSetTitle_en,
        articleSequence
    }
    console.log(params)
    return new Promise((resolve, reject) => {
        axios.get('/article', {
            params
        }).then(res => {
            resolve(res.data)
        }).catch(err => {
            reject(err)
        })
    })
}