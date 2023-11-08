<template>
    <div class='header'>
        <h1>랜덤한 강아지</h1>
        <button @click ="getRandomDogData" class="custom-button">새로운 강아지 가져오기</button>
    </div>

    <div v-if="dogIsEmpty" class="dog-container">
        <DogDetail v-for="dog in dogs" :dogData="dog" />
    </div>
    <div v-else>
        불러온 데이터가 없습니다.
    </div>

</template>



<script setup>
import { computed, watch } from 'vue';
import DogDetail from './DogDetail.vue';


const emit = defineEmits(['getDogData'])

const getRandomDogData = () => {
    emit('getDogData')
}

const props = defineProps({
    dogs: Array,
})


const dogIsEmpty = computed(() => {
    // script에서는 props.<변수>로 접근해야 한다.
    return props.dogs.length > 0 ? true : false
})



</script>



<style scoped>
.header {
    display: flex;
    justify-content: space-between;
}

.custom-button {
    background-color: #3498db; /* 버튼 배경색 지정 */
    color: #fff; /* 글자색 지정 */
    border: none; /* 테두리 제거 */
    padding: 3px 16px; /* 더 작은 버튼 크기로 조절합니다. */
    border-radius: 5px; /* 버튼 모서리 둥글게 만들기 */
    cursor: pointer; /* 커서 모양 변경 */
    width: 20%;
    /* height: 100%; */
    /* font-size: 10px; */
}

.custom-button:hover {
    background-color: #2980b9; /* 버튼에 마우스를 올렸을 때 배경색 변경 */
}

</style>
