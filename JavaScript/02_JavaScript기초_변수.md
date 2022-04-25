# JavaScript 기초

## 변수

### 변수와 식별자

#### 식별자 정의와 특징

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작 
- 예약어* 사용 불가능
  - for, if, function 등

### 식별자 작성 스타일

- 카멜 케이스(camelCase, lower-camel-case)
  - 변수, 객체, 함수에 사용
  - 두 번째 단어의 첫글자부터 대문자

```javascript
//변수
let dog
let variableName

//객체
const userInfo = {name : 'TOM', age : 20}

//함수
function add() {}
function getName() {}
```

- 파스칼 케이스(PascalCase, upper-camel-case)
  - 클래스, 생성자에 사용
  - 모든 단어의 첫 번째 글자를 대문자로 작성

```javascript
//클래스
class User{
    constructor(options) {
        this.name = options.name
    }
}

//생성자 함수
function User(options) {
    this.name = options.name
}
```

- 대문자 스네이크 케이스(SNAKE_CASE)
  - 상수(constants)*에 사용
    - 상수의 정의 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미
    - API_KEY
  - 모든 단어 대분자 작성 & 단어 사이에 **언더스코어** 삽입

```javascript
// 값이 바뀌지 않을 상수
const API_KEY = 'my-key'
const PI = Math.PI

//재할당이 일어나지 않는 변수
const numbers = [1,2,3]
```



#### 변수 선언 키워드 (let, const)

- let
  - 재할당 할 예정인 변수 선언 시 사용
  - 변수 재선언 불가능
  - 블록 스코프
- const 
  - 재할당 할 예정이 없는 변수 선언시 사용 
  - 변수 재선언 불가능
  - 블록 스코프

#### 선언, 할당, 초기화

```javascript
let foo //선언
console.log(foo) // undefined

foo = 11 //할당
console.log(foo)  // 11

let bar = 0 //선언 + 할당
console.log(bar) //0
```

- 선언
  - 변수를 생성하는 행위 또는 시점
- 할당
  - 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점 

