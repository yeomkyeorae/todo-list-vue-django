<template>
  <div class="todo-list">
      <h2>투두두두두두둑</h2>
      <ul>
        <li v-for="todo in todos" :key="todo.id"><input @change="checked(todo)" v-model="todo.is_completed" type="checkbox">{{todo.title}}<button @click="deleteTodo(todo)">X</button></li>
      </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'TodoList',
    props: {
        todos: {
            type: Array,
            required: true
        }
    },
    methods: {
      deleteTodo(todo){
        this.$session.start()
        const token = this.$session.get('jwt')
        const options = {
          headers: {
            Authorization: `JWT ${token}` // JWT 공백
          }
        }
        console.log(todo)
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, options)
          .then(response => {
            console.log(response)
            const target = this.todos.find( el => {
              return el === todo
            })
            const idx = this.todos.indexOf(target)
            if (idx > -1){
              this.todos.splice(idx, 1)
            }
          })
      },
      checked(todo){
        this.$session.start()
        const token = this.$session.get('jwt')
        const options = {
          headers: {
            Authorization: `JWT ${token}` // JWT 공백
          }
        }
        // const data ={
        //   'id': todo.id,
        //   'user_id': todo.user_id,
        //   'title': todo.title,
        //   'is_completed': todo.is_completed
        // }
        axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, todo, options)
          .then(response => {
            console.log(response)
          })
      }
    }
}
</script>

<style>

</style>