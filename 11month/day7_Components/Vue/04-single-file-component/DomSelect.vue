<template>
  <div>
    <input type="text" ref="ssafy">
  </div>
</template>

<script setup>
// ref 속성으로 직접 DOM 요소 선택하기
import { ref, onMounted } from 'vue'

const ssafy = ref()

onMounted(() => {
  console.log(ssafy.value)
})
</script>

<style lang="scss" scoped>

</style>
