const backendURL = "http://127.0.0.1:8000/api/v1/articles/"
const getData = function() {
    axios({
        method : 'GET',
        url : backendURL,
    }).then((response)=>{
        console.log(response);
    }).catch((error) =>{
        console.error(error);
    })
}


// CORS 에러 = Cross Origin 
// 요청을 받은 출처(데이터를 보내주는 출처)
// http://127.0.0.1:8000/
// 요청을 보내는 출처(데이터를 받은 출처)
// http://127.0.0.1:5500/
// django-cors -headers 를 활용해서 pip 설치후 pjt 세팅에 추가해주어야함

const postData = function() {
    axios({
        method : "POST",
        url : backendURL,
        data : {
            title : "test",
            content : "test",
        }
        }).then((response)=>{
            console.log(response);
        }).catch((error) =>{
            console.error(error);
        })
    
}