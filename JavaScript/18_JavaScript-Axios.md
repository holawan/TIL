# JavaScript

## Axios

### 개념

- "Promise based HTTP client for the browser and Node.js"
- 브라우저를 위한 Promise 기반의 클라이언트
- 원래는 "XHR"이라는 브라우저 내장 객체를 활용해 AJAX 요청을 처리하는데, 이보다 편리한 AJAX 요청이 가능하도록 도움을 줌
  - 확장 가능한 인터페이스와 함께 패키지로 사용이 간편한 라이브러리를 제공

### XMLHttpRequest - >Axios

#### XMLHttpRequest

```javascript
const xhr = new XMLHttpRequest()
const URL = 'https://jsonplaceholder.typicode.com/todos/1'
xhr.open('GET',URL)
xhr.send()
xhr.onreadystatechange = function(event) {
    if (xhr.readyState === XMLHttpRequest.DONE) {
        const status = event.target.status
        if (status ===0 || (status>=200 && status <400)){
            const res = event.target.response
            const data = JSON.parse(res)
            console.log(data)
            console.log(data.title)
        }else {
            console.error('Error!')
        }
    } 
}
```

#### Axios 

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
	const URL = 'https://jsonplaceholder.typicode.com/todos/1'
    
    axios.get(URL)
    	.then(res => console.log(res.data.title))
    	.catch(err => console.log('Error!'))
</script>
```



### Aixos 예시

#### todos에서 1번 데이터 받아오기 

```javascript
const URL = 'https://jsonplaceholder.typicode.com/todos/1'

// const responsePromise = axios.get(URL)
// responsePromise
//   .then(function(res){return res.data} )
//   .then(function (x) {console.log(x.title)})


axios.get(URL) //Promise 리턴 
	//data 받아오기 
    .then(res => res.data)
	//data에서 title 뽑기 
    .then(todo => todo.title)
	//title 출력하기 
    .then(title => console.log( title ))
	//문제가 발생하면 에러 뱉기 
    .catch(err => console.error(err)
     .finally(x) => console.log('끝'))
```

#### todolist에 접근해서 10번 데이터 받아오기

```javascript
	const URL = 'https://jsonplaceholder.typicode.com/todos/'
    
    // const responsePromise = axios.get(URL)
    // responsePromise
    //   .then(function(res){return res.data} )
    //   .then(function (x) {console.log(x.title)})

    
    axios.get(URL) //Promise 리턴 
	//data 받아오기  
    .then(res => {
      const todoArray = res.data
      const todo = todoArray.find(todo => todo.id === 10)
      return axios.get(`${URL}${todo.id}`)
    } )
    .then(res => console.log(res.data))
	//문제가 발생하면 에러 뱉기 
    .catch(err => console.error(err))
     .finally(x => console.log('끝'))
```

