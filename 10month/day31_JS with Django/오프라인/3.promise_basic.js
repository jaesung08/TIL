const myPromise = new Promise((resolve, reject) =>
{   
    resolve('성공일까?')
    reject('실패일까?')


    // console.log("Promise 생성됨");
    // let num = 0
    // if (num === 0) {
    //     resolve('로직 수행 성공!')
    // } else {
    //     reject("로직 수행 실패!")
    // }
})

myPromise.then((result) => {
    console.log(result);
}).catch((error) =>{
    console.log(`error = ${error}`);
})