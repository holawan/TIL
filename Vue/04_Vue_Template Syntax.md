# Template Syntax

### Template Syntax

- 렌더링 된 DOM을 기본 Vue 인스턴스의 데이터에 선언적으로 바인딩 할 수 있는 HTML 기반 템플릿 구문을 사용

1. Interpolation
2. Directive

### Interpolation(보간법)

1. TEXT
   - \<span>메시지 : {{ msg }}\</span>
2. Raw HTML
   - \<span v-html="rawHtml">\</span>
3. Attributes
   - \<div v-bind:id="dynamicId">\</div>
4. JS 표현식
   - {{ number + 1}}
   - {{ message.split(''). reverse().join('') }}

### Directive(디렉티브)

- v-접두사가 있는 특수 속성
- 속성 값은 단일 JS 표현식이 됨 (v-for는 예외)
- 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할을 함

#### 전달인자 (arguments)

- `:` (콜론)을 통해 전달 인자를 받을 수도 있음

```html
<a v-bind:href="url">...</a>
<a v-on:clikc="doSomething">...</a>
```



#### 수식어(Modifiers)

- `.`(점)으로 표시되는 특수 접미사
- directive를 특별한 방법으로 바인딩 해야 함을 나타냄 

```html
<form v-on:submit.prevent="onSubmit">...</form>
```



### v-text

- 엘리먼트의 text Content를 업데이트
- 내부적으로 interpolation 문법이 v-text로 컴파일 됨

```html
<body>
  <div id="app">
    <p> {{ message }}</p>
    <p v-text="message"> </p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message : 'Hello'
      }
    })
  </script>
```



### v-html

- 앨리먼트의 innerHTML을 업데이트
  - XSS 공격에 취약할 수 있음
- 임의로 사용자로부터 입력 받은 내용은 v-html에 '절대' 사용 금지

```html
<body>
  <div id="app">
    <p v-html="message"></p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data:{
        message: '<strong>강하다</strong>'
      }
    })
  </script>
```



### v-show

- 조건부 렌더링 중 하나
- 요소는 항상 렌더링 되고 DOM에 남아있음
- 단순히 엘리먼트에 display CSS 속성을 토글하는 것
- false처리 되어도 화면상에 존재하지만 style이 display-none이 되는 것 뿐 
  - v-if와의 차이 

```html
<body>
  <div id="app">
    <p v-show="isTrue">True</p>
    <p v-show="isFalse">False</p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data:{
        isTrue: true ,
        isFalse: false
      }
    })
  </script>
```

### v-if, v-else-if, v-else

- 조건부 렌더링 중 하나
- 조건에 따라 요소를 렌더링
- directive의 표현식이 true일 때만 렌더링
- 엘리먼트 및 포함된 directive는 토글하는 동안 삭제되고 다시 작성됨

```html
<body>
  <div id="app">
    <p v-if="seen"> seen is TRUE </p>
    <p v-if="myType ==='A'">A</p>
    <p v-else-if="myType ==='B'">B</p>
    <p v-else-if="myType ==='B'">C</p>
    <p v-else>X</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el :'#app',
      data:{
        seen:false,
        myType:'A',
      }
    })
  </script>
```

#### v-show와 v-if

- v-show(Expensive initial load, cheap toggle)
  - CSS display 속성을 hidden으로 만들어 토글
  - 실제로 렌더링은 되지만 눈에서 보이지 않는 것이기 때문에 딱 한 번만 렌더링이 되는 경우라면 v-if에 비해 상대적으로 렌더링 비용이 높음
  - 하지만, 자주 변경되는 요소라면 한 번 렌더링 된 이후부터는 보여주는지에 대한 여부만 판단하면 되기 때문에 토글 비용이 적음
- v-if(Cheap initial load, expensive toggle)
  - 전달인자가 false인 경우 렌더링 되지 않음
  - 화면에서 보이지 않을 뿐만 아니라 렌더링 자체가 되지 않기 때문에 렌더링 비용이 낮음
  - 하지만, 자주 변경되는 요소의 경우 다시 렌더링 해야 하므로 비용이 증가할 수 있음



### v-for

- 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록을 여러 번 렌더링
- item in items 구문 사용
- item 위치의 변수를 각 요소에서 사용할 수 있음
  - 객체의 경우는 key
- v-for 사용 시 반드시 key 속성을 각 요소에 작성
- v-if와 함께 사용하는 경우 v-for가 우선순위가 더 높음
  - 단, 가능하면 v-if와 v-for를 동시에 사용하지 말 것 

```html
<body>
  <div id="app">
    <h2>String</h2>
      <div v-for="char in myStr">
        {{  char  }}
      </div>
    <h2>Array</h2> 
      <div v-for="fruit in fruits">
        {{fruit}}
      </div>
      <!-- 요소, 인덱스 순으로 뽑을 수 있음  -->
      <div v-for="(fruit,idx) in fruits" :key="idx">
        {{ idx }} => {{fruit}}

      </div>
    <h2>Todos</h2>
      <div v-for="todo in todos">
        <h2>{{todo.title}} => {{todo.completed}}</h2>
      </div>

    <h2>Object</h2>
    <div v-for="value in myObj">
      {{value}}
    </div>
    <div v-for="(value,key) in myObj">
      {{value}} {{key}}
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el : '#app',
      data :{
        myStr : 'Hello World!',
        fruits :['apple','banana','coconut'],
        todos :[
          {id:1, title:'todo1',completed:true},
          {id:2, title:'todo2',completed:false},
          {id:3, title:'todo3',completed:true}
        ],
        myObj:{
          name: 'kim',
          age:100,
        }
      }
    })
  </script>
</body>
```

### v-on

- 엘리먼트에 이벤트 리스너를 연결
- 이벤트 유형은 전달인자로 표시함
- 특정 이벤트가 발생했을 때, 주어진 코드가 실행 됨
- 약어(Shorthand)
  - @
  - v-on:click -> @click

```html
<body>
  <div id="app">
    <!-- 메서드 핸들러 -->
    <button v-on:click="alertHello">Button</button>
    <button @click="alertHello">Button</button>
    <!-- 기본 동작 방지 -->
    <form action="" @submit.prevent="alertHello">
      <button>gogo</button>
    </form>

    <!-- 키 별칭을 이용한 키 입력 수식어 -->    
    <input type="text" @keyup.enter="log">
    <!-- cb 함수에서 특수 문법( ) 실행할 때 a를 넘긴다. 
    log를 실행할 건데 인자로 a를 넘긴다. -->
    <input type="text" @keyup.enter="log('a')">
    <p>{{message}}</p>
    <button @click="changeMessage">change message</button>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app= new Vue({
      el : '#app',
      //값
      data :{
        message : 'Hello Vue',
      },
      //행동
      methods:{
        alertHello : function() {
          alert('hello')
        },
        log : function(event) {
          console.log(event)
        },
        changeMessage() {
          this.message='New message!!'
        }
      }
    })
  </script>
</body>
```

### v-bind

- HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당
- Object 형태로 사용하면 Value가 ture인 key가 class 바인딩 값으로 할당
- 약어(Shorthand)
  - : (콜론)
  - v-bind:href -> :href

```html
  <style>
    .active {
      color: red;
    }

    .my-background-color {
      background-color: yellow;
    }
  </style>
</head>
<body>
  <div id="app">
    <!-- 속성 바인딩 -->
    <img :src="imageSrc" :alt="altMsg">
    <hr>

    <!-- 클래스 바인딩 -->
    <div :class="{ active : isRed }">
      클래스바인딩 
    </div>
    <h3 :class="[activeRed,myBackground]">
      hello vue
    </h3>
    <hr>

    <!-- 스타일 바인딩 -->
    <p :style="{ fontSize : fontSize +'px' }">
      this is paragraph
    </p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el:'#app',
      data:{
        fontSize : 16,
        altMsg: 'this is image',
        imageSrc: 'https://picsum.photos/200/300/',
        isRed :true,
        activeRed:'active',
        myBackground:'my-background-color',
      }
    })
  </script>
</body>
```

### v-model

- HTML form 요소의 값과 data를 양방향 바인딩
- 수식어
  - .lazy
    - input 대신 change 이벤트 이후에 동기화
  - .number
    - 문자열ㅇ르 숫자로 변경
  - .trim
    - 입력에 대한 trim을 진행 

```html
<body>
  <div id="app">
    <!-- 단방향 -->
    <!-- input의 변화가 데이터의 변화를 바꾸지만 데이터의 변화가 input의 변화를 바꾸진  않음  -->
    <h2>Input -> Data</h2>
    <p> {{ msg1 }}</p>
    <input type="text" @input="onInputChange">
    <hr>
    <!-- 양방향 -->
    <h2>input<->Data</h2>
    <p> {{msg2 }}</p>
    <input type="text" v-model="msg2">
    <hr>
    체크
    <input type="checkbox" v-model="checked">
    <p>{{checked}}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el : '#app',
      data :{
        msg1 : '111',
        msg2 : '222',
        checked :true
      },
      methods : {
        onInputChange (event) {
          this.msg1 = event.target.value
        }
      },
    })
  </script>
</body>
```

