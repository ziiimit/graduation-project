import axios from 'axios';

export function getSearchResult(userInput_zh) {
    const params = {
        userInput_zh
    }
    return new Promise((resolve, reject) => {
        axios.get('/search', {
            params
        }).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err);
        })
    })
}