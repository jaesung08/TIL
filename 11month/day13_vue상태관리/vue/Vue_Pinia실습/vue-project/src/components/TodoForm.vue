<template>
    <div>
        <h1>TodoForm</h1>
        <form @submit.prevent="createTodo(todoText)" ref="formElem">
            <input type="text" v-model="todoText">
            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const todoText = ref('')

const store = useCounterStore()

const formElem = ref(null)

const createTodo = function (todoText) {
    store.addTodo(todoText)
    formElem.value.reset()
}





</script>

<style scoped>

</style>