# JavaScript 기초

## 연산자

### 할당 연산자

- 오른쪽에 있는 피연산자의 평과 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- Increment 및 Decrement 연산자
  - Increment(++) : 피연산자의 값을 1 증가시키는 연산자
  - Decrement(--) : 피연산자의 값을 1 감소시키는 연산자
  - Airbnb Style Guide에서는 '+=' 또는 '-='와 같이 더 분명한 표현으로 적을 것을 권장

```javascript
let x = 0

x += 10
console.log(x) //10

x -= 3
console.log(x) //7

x *=10
console.log(x) //70

x /= 10 
console.log(x) //7

x+=
console.log(x) //8
x--
console.log(x) //7
```

### 비교 연산자

- 피연산자들 (숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하여 표준 사전 순서를 기반으로 비교
  - ex) 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 크다
    - 소문자가 대문자보다 더 크다 

```javascript
const numOne = 1
const numTwo = 100
console.log(numOne < numTwo) //true

const charOne = 'a'
const charTwo = 'z'
console.log(charOne > charTwo) //false
```

### 동등 비교 연산자(==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 압묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예살치 못한 결과가 발생할 수 있으므로 특병한 경우를 제외하고 사용하지 않음

```javascript
const a = 1004
const b = '1004'
console.log(a==b) //true

const c = 1 
const d = true
console.log(c==d) //true

//자동 타입 변환 예시
console.log(a+b) //10041004
console.log(c+d) // 2 
```

### 일치 비교 연산자(===)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교가 이뤄지며 압묵적 타입 변환이 발생하지 않음
  - 엄격한 비교 : 두 비교 대상의 타입고 값 모두 같은지 비교하는 방식
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별 

```javascript
const a = 1004
const b = '1004'
console.log(a===b) //false

const c = 1 
const d = true
console.log(c===d) //false
```

### 논리 연산자

- 세 가지 논리 연산자로 구성
  - and 연산은 '&&' 연산자로 이용
  - or 연산은 '||' 연산자를 이용
  - not 연산은 '!' 연산자를 이용
- 단축 평가 지원
  - ex) false && true = > false
  - ex ) true || false => treu

```javascript
/*
and 연산
*/
console.log(true && false) //false
console.log(true && true) //true
console.log(1 && 0) //0
console.log(4 && 7) //7
console.log('' && 5) //''

/*
or 연산
*/
console.log(true || false) //true
console.log(false || false) //false
console.log(1 && 0) //1
console.log(4 && 7) //4
console.log('' && 5) /5


/*
not  연산
*/
console.log(!true) //false
console.log(!'Bonjour!') //false
```

### 삼항 연산자

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능
- 한 줄에 표기하는 것을 권장

```javascript
console.log(true ? 1:2) //1
console.log(false ? 1:2) //2

const result = Math.PI >4 ? 'YES' : 'NO'
console.log(result) //NO
```

#### 정리

1. 자바스크립트의 데이터 타입은 크게 원시 타입과 참조 타입으로 분류된다.
2. Number 타입은 0,-0,NaN을 제외한 모든 경우 참으로 형변환 된다.
3. 일치 비교 연산자(===)는 자동 형변환이 일어나지 않는다. 
