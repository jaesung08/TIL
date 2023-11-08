<template>
  <div class="container">
    <h1>2023-11-08 실습</h1>
    <DogList 
    :dogs="dogs"
    @get-dog-data="getDogData"
    />
  </div>
</template>



<script setup>
import DogList from './components/dogList.vue';
import axios from 'axios'
import { ref, watch } from 'vue';

const dogs = ref([])

// 비동기 버그 해결 코드
// async : 이 함수가 비동기 함수다 알려주는 키워드
// await : 비동기 함수의 종료를 기다려주는 키워드
// try-catch 와 자주 사용된다!
const getDogData = async ()  => {
  const URL = 'https://api.thedogapi.com/v1/images/search?limit=10'
  try{
    const response = await axios.get(URL)

    const dogData =response.data

    // 비동기 쓸때는 forEach 쓰지 말자
    //    map 으로 변경! -> map : 기존 데이터를 토대로 새로운 배열 반환
    // map 안에 async 쓰면 자동으로 promise 객체 반환됨
    const details = dogData.map( async (dog) => {
      const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`;
      const detailres = await axios.get(detailURL);
      dog.detail = detailres.data.breeds ? detailres.data.breeds[0] : null
      console.log(dog);
    });
    
    // Promise 객체 10개가 출력됨 - 상태가 : fulfilled(성공함)
    // Promise 실행 자체는 성공했는데,
    // 원하는 순서는 보장하지 못했다!
    console.log(details);

    // Promise.all : Promise 배열의 계산이 모두 끝날때까지 기다려줌
    await Promise.all(details)

    dogs.value = dogData
    console.log(dogData);


  } catch (error){
    console.error('강아지 데이터를 못불러옴', error);

  }




}
// const getDogData = () => {
//  const URL = 'https://api.thedogapi.com/v1/images/search?limit=10'
//   비동기 버그 코드
//   axios.get(URL) 
//   .then((response) => {
//     // dogs.value = response.data

//     // 10마리 강아지 데이터
//     const dogData = response.data
    
//     dogData.forEach((dog) => {
//       const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
//       axios.get(detailURL)
//         .then((response) => {
//         // console.log('detail  =', response.data);
//         dog.detail = response.data
//       }).catch((error) => {
//         console.error(error);
//       })
//     });

//     dogs.value = dogData
//     console.log(dogs.value);

//   }).catch((error) => {
//     console.error(error);
//   })
//   console.log('부모에서 호출됨');
// }


</script>



<style scoped>
  .container {
    /* 가로축 80%만 사용 */
    width: 80%; 
    /* 가운데 정렬(좌우 간격 0으로 설정?) */
    margin: 0 auto;
  }
</style>