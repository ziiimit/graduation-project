import axios from 'axios';

export function getCandidatesList(params) {
    return new Promise((resolve, reject) => {
        axios.get('/jobFit/selectPerson', {
            params
        }).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err);
        })
    })
}


export function getCandidateProfile(params) {
    return new Promise((resolve, reject) => {
        axios.get('/jobFit/selectSingle', {
            params
        }).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err);
        })
    })
}

