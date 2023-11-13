<template>
  <div>
      <p>{{ store.count }} </p>
      <p>{{ newNumber }}</p>
      <p>{{ store.doubleCount }}</p>
      <button @click="store.increment()">버튼</button>
  </div>
</template>

<script setup>
import { useCounterStore} from '@/stores/counter.js'

const store = useCounterStore()

store.count = 100

const newNumber = store.count + 1

</script>

<style scoped>

</style>