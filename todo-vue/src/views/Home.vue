<template>
  <div class="home">
    <TodoForm @todoCreate-event="todoCreate" /> <!-- PascalCase, upperCamelcase -->
    <!-- kebab-case -->
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'   // import requests 하는 느낌
// import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex' // from bs4 import BeautifulSoup 하는 느낌
import router from '../router'
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
  computed: {
    ...mapGetters([   // spread ES6 문법, object를 풀 때
      'options',
      'user'
    ])
    // options() {
    //   return this.$store.getters.options
    // },
    // user() {
    //   return this.$store.getters.user
    // }
  },
  methods: {
    todoCreate(title){
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const options = {
      //   headers: {
      //     Authorization: `JWT ${token}` // JWT 공백
      //   }
      // }
      // console.log(jwtDecode(token))
      // {user_id: 1, username: 'yeom', exp: 1534356234, email: 'y@y.com'}
      const data = {
        title: title,
        // user: jwtDecode(token).user_id
        user: this.user
      }
      // request.POST인 경우는 아래 FormData를 사용한다!
      // const formData = new FormData()
      // formData.append('title', title)
      // formData.append('is_completed', false)
      // formData.append('user', 1)
      axios.post('http://127.0.0.1:8000/api/v1/todos/', data, this.options)
        .then(response =>{
          this.todos.push(response.data)
        })
    },
    getTodos(){
      // axios 요청시마다 헤더를 추가해서 보내야 함!
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const options = {
      //   headers: {
      //     Authorization: `JWT ${token}` // JWT 공백
      //   }
      // }
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.user}/`, this.options)
        .then(response => {
          // console.log(response) // 만약, 오류가 발생하게 되면 ESlint 설정을 package.json에 추가
          this.todos = response.data.todo_set
        })
        .catch(error => {
          console.log(error)
      })
    },
    isLogined(){
      this.$session.start()
      // session에 jwt가 없다면, 즉 토큰이 없다면, 비로그인이라면.
      if (!this.$session.has('jwt')){
        router.push('/login')
      } else {
        // 로그인 되어 있다면, vuex token 업데이트
        this.$store.dispatch('login', this.$session.get('jwt'))
      }
    }
  },
  mounted() {
    this.isLogined()
    this.getTodos()
  }
}
</script>
