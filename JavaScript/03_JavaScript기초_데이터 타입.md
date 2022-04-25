# JavaScript 기초

## 데이터 타입

### 데이터 타입 종류

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입과 참조 타입으로 분류됨

![datatype](03_JavaScript기초_데이터 타입.assets/datatype.PNG)

### 원시 타입과 참조 타입 비교

- 원시 타입 (Primitive type)
  - 객체 (object)가 아닌 기본 타입
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사됨

```javascript
let message = '안녕하세요' //1. message 선언 및 할당

let greeting = message //2. greeting에 message 복사
console.log(greeting) //3. 안녕하세요 ! 출력

message = 'Hello, world' //4. message 재할당
console.log(greeting) //5. '안녕하세요!'출력

// => 즉, 원시 타입은 실제 해당 타입의 값을 변수에 저장한다. 
```

- 참조 타입(Reference type)
  - 객체(object) 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨

```javascript
const message = ['안녕하세요'] //1. message 선언 및 할당

const greeting = message // 2. greeting에 message 복사
console.log(greeting)  //3. ['안녕하세요!'] 출력 

message[0] = 'Hello,world!' //4. message 재할당
console.log(greeting)  //5. ['Hello world!'] 출력

// => 즉, 참조 타입은 해당 객체를 참조할 수 있는 참조 값을 저장한다.
```

