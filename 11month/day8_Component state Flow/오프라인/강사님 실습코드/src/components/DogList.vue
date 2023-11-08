<template>
  <div class="header">
    <h2>랜덤한 강아지</h2>
    <button @click="getRandomDogData" class="styled-button">새로운 강아지 가져오기</button>
  </div>
  <div v-if="dogIsEmpty" class="dog-container">
    <div v-for="dog in dogs" class="dog-box">
      <!-- 하위 컴포넌트로 분리해보기 -->
      <!-- <DogDetail /> -->
      <img :src="dog.url" alt="">
      <div v-if="dog.detail" class="dog-info">
        <p><strong>이름: </strong>{{ dog.detail.name }}</p>
        <p><strong>품종: </strong>{{ dog.detail.breed_group }}</p>
        <p><strong>높이:</strong> {{ dog.detail.height.imperial }} 인치 ({{ dog.detail.height.metric }} cm)</p>
        <p><strong>수명:</strong> {{ dog.detail.life_span }}</p>
        <p><strong>성격:</strong> {{ dog.detail.temperament }}</p>
        <p><strong>무게:</strong> {{ dog.detail.weight.imperial }} 파운드 ({{ dog.detail.weight.metric }} kg)</p>
      </div>
      <div v-else class="dog-info">
        상세 정보 없음
      </div>
    </div>
  </div>
  <div v-else>
    아직 데이터를 받아오지 않았다
  </div>
</template>

<script setup>
import { computed, watch } from 'vue';

const emit = defineEmits(['getDogData'])

const getRandomDogData = () => {
  emit('getDogData')
}

const props = defineProps({
  dogs: Array
})

watch(props, () => {
  console.log('in props = ', props.dogs)
})

const dogIsEmpty = computed(() => {
  // script 에서는 props.<변수> 로 접근해야한다.
  return props.dogs.length > 0 ? true : false
})

</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.styled-button {
    background-color: #4CAF50; /* 배경색 */
    border: none; /* 테두리 없음 */
    color: white; /* 텍스트 색상 */
    padding: 15px 32px; /* 안쪽 여백 */
    text-align: center; /* 텍스트 중앙 정렬 */
    text-decoration: none; /* 텍스트에 밑줄 없음 */
    display: inline-block; /* 인라인 블록 요소로 표시 */
    font-size: 16px; /* 폰트 크기 */
    margin: 4px 2px; /* 바깥쪽 여백 */
    cursor: pointer; /* 포인터 커서로 변경 */
    border-radius: 8px; /* 둥근 테두리 */
}

.styled-button:hover {
    background-color: #45a049; /* 호버 상태에서의 배경색 */
}

.dog-container {
  border: 1px solid #000;
}

.dog-box {
  border: 1px solid #000;
  margin: 10px;
  border-radius: 10px;
  display: flex;
}

.dog-box img {
  width: 200px;
  height: 200px;
  object-fit: fill;
  border-radius: 10px;
}

.dog-info {
  margin-left: 10px;
}

</style>