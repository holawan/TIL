# JavaScript

## async & await

### 개념 

- 비동기 코드를 작성하는 새로운 방법
  - ECMAScript 2017에서 등장
- 기존 Promise 시스템 위에 구축된 syntactic sugar
  - Promise 구조의 then chaining을 제거
  - 비동기 코드를 조금 더 동기 코드처럼 표현
  - Sytntactic sugar
    - 더 쉽게 읽고 표현할 수 있도록 설계된 프로그래밍 언어 내의 구문
    - 즉, 문법적 기능은 그대로 유지하되 사용자가 직관적으로 코드를 읽을 수 있게 만듦 

### Promise -> async & await 적용

##### Promise 

```javascript
const URL = 'https://dog.ceo/api'

function fetchFirstDogImage() {
    axios.get(URL + 'breeds/list/all')
    .then(res => {
        const breed = Object.keys(res.data.message)[0]
        return axios.get(URL + `breed/${breed}/images`)
    })
    .then(res => {
        console.log(res)
    })
    .catch(err => {
        console.error(err.response)
    })
}
fetchFirstDogImage()
```

##### async & await

```javascript
const URL = 'https://dog.ceo/api'

async function fetchFirstDogImage() {
    const res = await axios.get(URL = 'breeds/list/all')
    const breed = Object.keys(res.data.message)[0]
    const images = await axios.get(URL + `breed/${breed}images`)
    console.log(images)
}
fetchFirstDogImage()
	.catch(err => console.error(err.response))
```



