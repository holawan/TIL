## Lifecycle Hooks

### Lifecycle Hooks

- 각 Vue 인스턴스는 생성될 때 일련의 초기화 단계를 거침
  - 예를 들어 데이터 관찰 설정이 필요한 경우, 인스턴스를 DOM에 마운트 하는 경우, 데이터가 변경되어 DOM을 업데이트하는 경우 등
- 그 과정에서 사용자 정의 로직을 실행할 수 있는 Lifecycle Hooks도 호출됨
- 공식문서를 통해 각 라이프사이클 훅의 상세 동작을 참고 



### Lifecycle Hooks 예시

- 예를 들어 created hook은 vue 인스턴스가 생성된 후에 호출 됨

```html
<script>
	new Vue({
        data: {
            a:1
        },
        created : function() {
            console.log('a is :' +this.a) // => 'a is :1'
        }
    })
</script>
```

- created를 사용해 애플리케이션 초기 데이터를 API 요청을 통해 불러올 수 있음

```html
<body>
  <div id="app">
    <img v-if="imgSrc" :src="imgSrc" alt="sample img">
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const API_URL = 'https://dog.ceo/api/breeds/image/random'
    const app = new Vue({
      el: '#app',
      data: {
        imgSrc: '',
      },
      methods: {
        getImg: function () {
          axios.get(API_URL)
            .then(response => {
              this.imgSrc = response.data.message
            })
        }
      },
    })
  </script>
```

