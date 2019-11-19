```
- (사전) npm install -g @vue/cli
- vue create todo-vue
```



```
- mkdir todo-django
- cd todo-django
- python -m venv venv
- django-admin startproject todo_django .
```



```
- pip install djangorestframework
- INSTALLED_APPS에 'rest_framework' 추가
```



```
- npm i vue-router
- vue add router
```





# Vue - DRF

## 1. 기본 설정

1. Django

   1. 가상환경 설정

      ```bash
      $ pyton -v
      3.7.4
      $ python -m venv venv
      $ source venv/Scripts/activate
      (venv)
      ```

   2. 패키지 설치

      ```bash
      $ pip install django djangorestframework
      $ pip freeze > requirements.txt
      ```

   3. django 프로젝트 생성

      ```bash
      $ django-admin startproject {프로젝트명} .
      ```

      

2. Vue

   1. VueCLI 설치

      ```bash
      $ npm install -g @vue/cli
      ```

   2. Vue 프로젝트 생성

      ```bash
      $ vue create {프로젝트 이름}
      ```

3. 프로젝트 폴더 구조

   ```\
   todo-django-vue/
   	.git/
   	todo-django/
   		venv/
   		manage.py
   		todo_django/
   	todo-vue/
   		node_modules/
   		public/
   		src/
   		package.json
   ```



## 2. DRF 모델링

## 3. Vue

### Vue-router(경로 부여, 각각의 경로마다 작업을 수행할 수 있도록)

``` bash
$ npm i vue-router
$ vue add router
> y
> y
```



## 4. Todos axios 요청

1. getTodos 메소드 정의

   ```javascript
   // Home.vue
   getTodos(){
   	axios.get('http://127.0.0.1:8000/api/v1/todos/')
   	.then(response => {
   		this.todos = response.data
       })
       .catch(error => {
          	console.log(error)
       })
   }
   ```

2. mounted에서 호출

   ```javascript
   // Home.vue
   mounted() {
       this.getTodos()
   }
   ```

   

3. CORS(Cross-Origin Resorces Sharing) 오류 발생

   ```
   :8080		axios		:8000
   VUE			-> X		Django
   			브라우저
   			① CORS 정책(헤더) 설정
   ```

   - 해결하기 위해서는 django 서버에서 설정이 필요

4. Django, `django-cors-headers` 패키지 활용

   - [Github](https://github.com/adamchainz/django-cors-headers)

   ```bash
   $ pip install django-cors-headers
   ```

   - `INSTALLED_APPS`, `MIDDLEWARE` 설정
   - `CORS_ORIGIN_ALLOW_ALL`: True시 모든 도메인에서 요청 가능
   - `CORS_ORIGIN_WHITELIST`: 위의 옵션을 False로 하고, 화이트리스트에 직접 도메인 등록
   - 기타 옵션들도 확인 해볼 것 

5. Vue에서 다시 요청 보내보기



## 5. TodoForm component를 통해 Todo 등록하기

> 생략



## 6. 로그인 기능

> JWT(JSWON Web Token): 토큰 기반 로그인 인증

​	[Github 참고](https://jpadilla.github.io/django-rest-framework-jwt/)

	1. 클라이언트(Vue) 로그인 정보(username, password)를 서버(Django)로 전송
 	2. 서버는 해당 정보를 바탕으로 Token을 발급 및 암호화
 	3. 클라이언트는 Token을 받아서 매 요청 때마다 헤더에 해당 Token정보를 추가해서 보냄
 	4. 서버에서는 매번 Token이 유효한지 확인
 	5. 클라이언트는 전송된 값을 디코딩

JWT는 기본적으로 헤더, payload(주고받는 데이터), Verify signature로 구성된다.

[https://jwt.io](https://jwt.io)에서 직접 디코딩을 해볼 수 있다.  



### 1) Django

```bash
$ pip install djangorestframework-jwt
```

### 2) Vue

1. 로그인 관련 컴포넌트 생성

2. 이벤트를 통해 axios 요청

3. token 값 저장

   1. `vue-session`

      ```bash
      $ npm i vue-session
      ```

   2. `src/main.js`

      ```javascript
      import VueSession from 'vue-session'
      
      Vue.use(VueSession)
      ```

   3. `vue-session` 활용하여 저장

      ```javascript
      const token = response.data.token
      this.$session.start()
      this.$session.set('jwt', token)
      ```

### 3) 활용

1. 요청시마다 아래의 `options`를 포함하여 전송

   ```javascript 
   this.$session.start()
   	const token = this.$session.get('jwt')
       const options = {
        	headers: {
             Authorization: `JWT ${token}` // JWT 공백
           }
       }
   ```

### 4) 사용자 정보 활용

> 사용자 정보를 활용하고 싶다면, token을 디코딩하여 활용한다.

1. 패키지 설치

```bash
$ npm i jwt-decode
```

2. 활용

```javascript
import jwtDeocde from 'jwt-decode'

this.$session.start()
const token = this.$session.get('jwt')
console.log(jwtDecode(token))
// {user_id: 1, username: 'yeom', exp: 1534356234, email: 'y@y.com'}
```



## 7. User별 Todo

### 1. Django

### 2. Vue



## 8. 비로그인시 로그인 페이지로 이동

