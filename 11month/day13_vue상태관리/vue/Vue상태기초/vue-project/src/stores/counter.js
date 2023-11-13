import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


// 전체는 store
export const useCounterStore = defineStore('counter', () => {
  // 상태
  // state
  const count = ref(0)
  // getters
  const doubleCount = computed(() => count.value * 2)

  // 기능
  // actions
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
