<template>
  <div class="home">
    <TodoForm @todoCreate-event="todoCreate" /> <!-- PascalCase, upperCamelcase -->
    <!-- kebab-case -->
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'

export default {
  name: 'home',
  components: {
    TodoList,
    TodoForm
  },
  data() {
    // 컴포턴트에서는 반드시 data를 함수로 작성하고, object를 리턴한다.
    return {
      todos: [],
    }
  },
  methods: {
    todoCreate(title){
      const data = {
        title: title,
        user: 1
      }
      // request.POST인 경우는 아래 FormData를 사용한다!
      // const formData = new FormData()
      // formData.append('title', title)
      // formData.append('is_completed', false)
      // formData.append('user', 1)
      axios.post('http://127.0.0.1:8000/api/v1/todos/', data)
        .then(response =>{
          this.todos.push(response.data)
        })
    },
    getTodos(){
      axios.get('http://127.0.0.1:8000/api/v1/todos/')
        .then(response => {
        // console.log(response) // 만약, 오류가 발생하게 되면 ESlint 설정을 package.json에 추가
        this.todos = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  mounted() {
    this.getTodos()
  }
}
</script>
