# Vue Syntax

### Basic syntax of Vue.js

### Vue instance

- 모든 Vue 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작
- Vue 인스턴스를 생성할 때는 Option 객체를 전달해야 함(중괄호)
- 여러 Option들을 사용하여 원하는 동작을 구현
- Vue Instance === Vue Component

```vue
const app = new Vue({

})
```

### Options/DOM

####  `el`

- Vue 인스턴스에 연결(마운트) 할 기존 DOM 요소가 필요
- CSS 선택자 문자열 혹은 HTML Element로 작성
- new를 이용한 인스턴스 생성 때만 사용

```javascript
const app = new Vue({
    el : '#app'
})
```

#### `data`

- Vue 인스턴스의 데이터 객체
- Vue 인스턴스의 상태 데이터를 정의하는 곳
- Vue template에서 interpolation을 통해 접근 가능
- v-bind, v-on과 같은 directive에서도 사용 가능
- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능

```javascript
cosnt app = new Vue({
    el : '#app',
    data :{
        message : 'Hello',
    }
})
```

#### `methods`

- Vue 인스턴스에 추가할 메서드
- Vue template에서 interpolation을 통해 접근 가능
- v-on과 같은 directive에서도 사용 가능
- Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능
- 주의
  - 화살표 함수를 메서드를 정의하는데 사용하면 안됨
  - 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에, 'this'는 Vue 인스턴스가 아님 

```javascript
cosnt app = new Vue({
    el : '#app',
    data :{
        message : 'Hello',
    },
    methods : {
        greeting : function() {
            console.log('hello')
        }
    }
})
```

#### `this` keyword in vue.js

- Vue 함수 객체 내에서 vue 인스턴스를 가리킴
- 화살표 함수를 사용하면 안되는 경우
  - data
  - methods

```html
<body>
  <div id="app">
    <p>{{message}}</p>
    <p>{{greeting( )}}</p>
  </div>
  <div id="app2">
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>

    const app = new Vue({
      el : '#app',
      data : {
        message:'안녕' 
      },
      methods : {
        greeting: function() {
          const newMessage = this.message + '!!!'
          console.log(newMessage)
          return newMessage
        }
      }
    })
  </script>
</body>
```

