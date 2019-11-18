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





1. 브라우저에서 다른 도메인 요청 x
2. policy (CORS) ! 서버가 설정
3. 장고 서버로 가서 설정해주자!

