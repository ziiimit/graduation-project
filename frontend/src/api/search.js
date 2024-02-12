import axios from 'axios';

// params = {userInput_zh}
export function getSearchResult(params) {
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