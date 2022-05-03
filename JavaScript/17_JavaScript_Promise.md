# JavaScript

## Promise

### Promise object

- 비동기 작업의 최종 완료 또는 실패를 나타내는 객체
  - 미래의 완료 또는 실패와 그 결과 값을 나타냄
  - 미래의 어떤 상황에 대한 약속
- 성공(이행)에 대한 약속
  - .then()

- 실패(거절)에 대한 약속
  - .catch()

```javascript
const myPromise = axios.get(URL)
//console.log(myPromise) // PromiseObject

myPromise
	.then(response =>{
    return response.data
})

//charging
//axios.get(URL)이 성공하면 Promise 객체가 리턴됨 
axios.get(URL)
	//get이 성공되면 then 함수를 진행한다. 
  .then(response => {
    return response.data
})
	//위의 then함수도 성공하면 이어서 then 함수를 진행한다. 
    .then(response =>{
    return response.title
})
	//중간에실패가 있었다면 이 행동을 하겠다.
    .catch(error => {
    console.log(error)
})
	//성공했던 망했건 최종적으로 이렇게 행동할거야 
    .finally(function(){
    console.log('마지막에 무조건  리턴 ')
})
```

### Promise methods 

#### .then(callback)

- 이전 작업(promise)이 성공했을 때 수행할 작업ㅇ르 나타내는 callback 함수
- 그리고 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
- 따라서 성공했을 때의 코드를 callback 함수 안에 작성

#### .catch(callback)

- .then이 하나라도 실패하면(거부 되면)동작 (동기식의 'try - except' 구문과 유사)
- 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음 

#### 각각의 .then()블록은 서로 다른 Promise를 반환

- 즉, .then()을 여러개 사용하여 연쇄적인 작업을 수행할 수 있음
- 결국 여러 비동기 작업을 차례대로 수행할 수 있음

##### .then()과 .catch() 메서드는 모두 promise를 반환하기 때문에 chainig 가능

#### 주의

- 반환값이 반드시 있어야 함
- 없다면 callback 함수가 이전의 promise 결과를 받을 수 없음 

### 예시

##### 피라미드 구조

```javascript
work1(function(result){
    work2(result1, function(result2){
        work3(result2,function(result3){
            console.log('최종결과 : ' + result3)
        })
    })
})
```

##### Promise 구조

```javascript
work1().then(function(result){
    return work2(result1)
})
.then(function(result2){
    return work3(result2)
})
.then(function(result3){
    console.log('최종결과:' + result3)
})
.catch(failuerCallback)
```

### Promise가 보장하는 것

- Async callback 작성 스타일과 딜리 Promise가 보장하는 특징

1. callback 함수는 JavaScript의 Event Loop가 현재 실행중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
   - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
   - Chaining은 Promise의 가장 뛰어난 장점 
