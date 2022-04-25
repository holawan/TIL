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

#### 재할당

- let (재할당 가능)

```javascript
let number = 10 //1. 선언 및 초기값 할당 
number = 100     //2. 재할당

console.log(number) //100
```

- const (재할당 불가능)
  - 값을 바꾸는건 할 수 있지만, 재할당은 불가능하다. '='을 못쓴다. 


```javascript
const number = 10 //1. 선언 및 초기값 할당
number = 10       // 2. 재할당 불가능 

=> Uncaught TypeError 
	:Assignment to constant variable.
```

#### 재선언

- let (재선언 불가능)

```javascript
let number = 10 //1. 선언 및 초기값 할당
let number = 50 //2. 재선언 불가능
=> Uncaught Syntax Error
	:Identifier 'number' has already been deciared 
```

- const (재선언 불가능)

```javascript
const number = 10 //1. 선언 및 초기값 할당
const number = 50 //2. 재선언 불가능
=> Uncaught SyntaxError
	: Identifier 'number' has already been declared
```

#### 변수 선언 키워드 (let, const) 

```javascript
let x = 1 
if (x === 1) {
    let x = 2 
    console.log(X) //2 
}
console.log(x) //1 
```

```python
x = 1 
if x==1 :
    x = 2 
    print(x) #2
print(x) #2
```



- 블록 스코프
  - if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
  - 파이썬에서는 if문이 함수가 아니라서 접근이 가능했지만 여기선 안된다. 

#### 변수 선언 키워드 'var'

- var로 선언한 변수는 재선언 및 재할당 모두 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- 호이스팅되는 특성으로 인해 예기치 못한 문제 발생 가능
  - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 재선언 및 재할당 모두 가능 

```javascript
var number = 10 //1. 선언 및 초기값 할당
var number = 50 //2. 재할당

console.log(number) //50
```

- 함수 스코프
  - 함수의 중괄호 내부를 가리킴
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능 

```javascript
function foo() {
    var x = 5 
    console.log(x) //5 
}
//ReferenceError : x is not defined 
console.log(x)
```

- 호이스팅
  - 변수를 선언 이전에 참조할 수 있는 현상
  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환

```javascript
//선언을 나중에 했는데도 입력이 되는 이상한 문제가 발생 
a
var a = 100
// undefined
a
// 100
```

```javascript
//에러인데 지금은 없다고 표현함 
console.log(username) // undefined
var username = '홍길동'

console.log(email) //Uncaught ReferenceError
let email = 'gildong@gmail.com'

console.log(age)  // Uncaught ReferenceError
const age = 50 
```

#### 정리

- 자바스크립트 변수 사용 시 사용 가능한 키워드는 const, let, var이다.
- const 키워드로 선언한 변수는 재할당이 불가능하다.
- let 키워드로 선언한 변수는 재할당이 가능하다. 

#### let, const, var 비교

| 키워드 | 재선언 | 재할당 |   스코프    |     비고     |
| :----: | :----: | :----: | :---------: | :----------: |
|  let   |   X    |   O    | 블록 스코프 | ES6부터 도입 |
| const  |   X    |   X    | 블록 스코프 | ES6부터 도입 |
|  var   |   O    |   O    | 함수 스코프 |  사용 지양   |

