# JavaScript 자료형

## 객체

### 객체의 정의와 특징

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
  - key이름에 띄어쓰기 등의 구분자가 있다면 따옴표로 묶어서 표현
- value는 모든 타입(함수포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```javascript
const me = {
    name : 'jack',
    phoneNumber:'01012345678',
    'samsung product': {
        buds : 'Galaxy Buds pro',
        galaxy : 'Galaxy s20',
    },
}
console.log(me.name) //jack
console.log(me.phoneNumber) //01012345678
console.log(me['samsung product']) //{buds: 'Galaxy Buds pro', galaxy: 'Galaxy s20'}
console.log(me['samsung product'].buds) //Galaxy Buds pro
```



### 객체와 메서드

- 메서드는 어떤 객체의 속성이 참조하는 함수.
- 객체.메서드명()으로 호출 가능
- 메서드 내부에는 this 키워드가 객체를 의미함.
  - fullName은 메서드가 아니기 때문에 정상출력 되지 않음 (NaN)
  - getFullName은 메서드이기 때문에 해당 객체의 firstName과 lastName을 정상적으로 이어서 반환 

```javascript
const me = {
    firstName : 'John',
    lastName : 'Doe',
    
    fullName : this.firstName + this.lastName,
    
    getFullName: function() {
        return this.firstName + this.lastName
    }
}
```



### 객체 관련 ES6 문법 익히기

- ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
  - 속성명 축약
  - 메서드 명 축약
  - 계산된 속성명 사용하기
  - 구조 분해 할당
    - 구조 분해 할당은 배열도 가능함
  - 객체 전개 구문(Spread Operator)

#### 속성명 축약

- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 아래와 같이 축약 가능

```javascript
var books = ['Learnig JS', 'Learning Python']
var magazines = ['Vogue', 'Science']

//ESS
var bookShop = {
    books : books,
    magazines : magazines,
}
console.log(bookShop)
/*
{books: Array(2), magazines: Array(2)}
books: (2) ['Learnig JS', 'Learning Python']
magazines: (2) ['Vogue', 'Science']
[[Prototype]]: Object
*/
```

```javascript
const books = ['Learning JS', 'Learning Python']
const magazines = ['Vogue', 'Science']

const bookShop = {
    books,
    magazines,
}
console.log(bookShop)
/*
{books: Array(2), magazines: Array(2)}
books: (2) ['Learnig JS', 'Learning Python']
magazines: (2) ['Vogue', 'Science']
[[Prototype]]: Object
*/
```

#### 메서드명 축약

- 메서드 선언시 function 키워드 생략 가능

```javascript
var obj = {
    greeting : function(){
        console.log('Hi!')
    }
}
obj.greeting()
//Hi!
```

```javascript
const obj = {
    greeting() {
        console.log('Hi!')
    }
}
obj.greeting()
//Hi!
```

#### 계산된 속성

- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

```javascript
const key = 'regions'
const value = ['광주','대전','구미','전주','서울']

const korea = {
    [key]:value,
}
console.log(korea) //{regions: Array(5)}
console.log(korea.regions)//['광주', '대전', '구미', '전주', '서울']
```

#### 구조 분해 할당

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```javascript
const userInformation = {
    name : 'dongwan kim',
    userId : 'asdf134652',
    phoneNumber:'010-1234-5678',
    email :'asdf@gmail.com',
}
const name = userInformation.name
const userId = userInformation.userId
const phoneNumber = userInformation.phoneNumber
const email = userInformation.email
```

#### Spread operator

- spread operator(...)를 사용하면 객체 내부에서 객체 전개 가능.
- ES5까지는 Object.assign() 메서드를 사용
- 얕은 복사에 활용가능

```javascript
const obj = {b:2,c:3,d:4}
const newObj = {a:1,...obj,e:5}
console.log(newObj)
//{a: 1, b: 2, c: 3, d: 4, e: 5}
```



### Json

- key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
  - 따라서 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수
- 자바스크립트에서는  JSON을 조작하기 위한 두 가지 내장 메서드를 제공
  - JSON.parse()
    - JSON => 자바스크립트 객체
  - JSON.stringify()
    - 자바스크립트 객체 => JSON

#### Object -> JSON

```javascript
// Object => JSON

const jsonData = JSON.stringify({
    coffe : 'Americano',
    iceCream : 'Cookie and cream',
})

console.log(jsonData)
console.log(typeof JsonData)

/*
// Object => JSON

const jsonData = JSON.stringify({
    coffe : 'Americano',
    iceCream : 'Cookie and cream',
})

console.log(jsonData)
console.log(typeof JsonData)
VM323:8 {"coffe":"Americano","iceCream":"Cookie and cream"}

*/
```

#### JSON -> Object

```javascript
// JSON => object

const jsonData = JSON.stringify({
    coffe : 'Americano',
    iceCream : 'Cookie and cream',
})

const parseData = JSON.parse(jsonData)

console.log(parseData)
console.log(typeof parseData)

/*
{coffe: 'Americano', iceCream: 'Cookie and cream'}
Object
*/
```



### 배열은 객체다

- 키와 속성들을 담고 있는 참조 타입의 객체
- 배열은 인덱스를 키로 갖으며 length 프로퍼티를 갖는 특수한 객체

```javascript
Object.getOwnPropertyDescriptors([1,2,3])
/*
0: {value: 1, writable: true, enumerable: true, configurable: true}
1: {value: 2, writable: true, enumerable: true, configurable: true}
2: {value: 3, writable: true, enumerable: true, configurable: true}
length: {value: 3, writable: true, enumerable: false, configurable: false}
*/
```

