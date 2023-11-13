import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    { id: id++, text: '할일 1', isDone:false},
    { id: id++, text: '할일 2', isDone:false},
  ])
  
  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function (todoId) {
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    todos.value.splice(index, 1)
  }

  const updateTodo = function (todoId) {
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
  })
  }

  const doneTodosCount = computed(() => {
    return todos.value.filter((todo) => todo.isDone).length
  })


  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, {persist: true} )
