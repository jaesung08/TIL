<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('hello world!')
</script>

<style scoped>
.greeting {
  color: crimson;
}
</style>
