<template>
    <div>
        <!-- {{  my-props }} -->
        <p>{{ myMsg }}</p>
        <p>{{ dynamicProps }}</p>
        
        <ParentGrandChild 
        :my-msg="myMsg" 
        @update-name="updateName"
        />

        <!-- 이벤트 선언을 안하고 바로 HTML에서 사용 -->
        <button @click="$emit('someEvent')">클릭</button>
        <!-- 이벤트를 'script'에서 선언하고 사용 -->
        <button @click="buttonClick">클릭</button>
        <button @click="emitArgs">추가 인자 전달</button>

    </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'
// 1. 문자열 배열 선언 방식
// defineProps(['myMsg'])

// 2. 객체 선언 방식
// defineProps({
//     myMsg: String,
//     // myMsg: {
//     //     type: String,
//     //     required: true,
//     // }
// })

//props 데이터를 script에서 사용하려면
const props = defineProps({
    myMsg: String,
    dynamicProps: String,
})

// console.log(props);
// console.log(props.myMsg);

// 3. 다양한 객체 선언 방식
// defineProps({
//     myMsg: {
//         type: String,
//         required: true,
//         // validator(value) {
//         //   return[ 'success', 'warning', 'danger'].includes(value)
//         // }
//         // 유효성 검사?
//         validator(value) {
//             const validValues = ['success', 'warning', 'danger']
//             if (!validValues.includes(value)){
//                 console.error('에러입니다!');
//                 return false
//             }
//             return true
//         }
//     }
// })


//emit 선언 방식
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName']) // 객체 방식으로도 가능함

const buttonClick = function () {
    emit('someEvent')
}

const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
    emit('updateName')
}

</script>

<style scoped>

</style>