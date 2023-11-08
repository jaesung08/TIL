<template>
    <div>
        <ParentChild 
        my-msg="message" 
        :dynamic-props="name" 
        @some-event="someCallback"
        @emit-args = "getNumbers"
        @update-name = "updateName"
        />
    </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'

const name = ref('Alice')
const someCallback = function() {
    console.log('ParentChild가 발신한 emit 이벤트를 수신했습니다.');
}

const getNumbers = function (...args) {
    console.log(args);
}
const updateName = function () {
    if (name.value === 'Bella'){
        name.value = 'Alice'
    } else {
        name.value = 'Bella'
    }
}

</script>

<style  scoped>

</style>