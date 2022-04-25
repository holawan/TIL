# JavaScript 기초

## 조건문

### 조건문의 종류와 특징

- 'if' statement
  - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓 을 판단
- 'switch' statement
  - 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
  - 주로 특정변수의 값에 따라 조건을 분기할 때 활용
    - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

### if statement

#### if, else if , else

- 조건은 소괄호(condition) 안에 작성
- 실행할 코드는 중괄호{} 안에 작성
- 블록 스코프 생성

```javascript
if (condition){
    //do something
}else if (condition) {
    //do something
}else {
    //do someting
}
```

#### 예시

```javascript
const nation = 'Korea'

if (nation === 'Korea') {
    console.log('안녕하세요!')
}else if (nation=='France') {
    console.log('Bonjur!')
}else {
    console.log('Hello!')
}
```

### switch statement

#### switch

- 표현식의 결과값을 이요한 조건문 
- 표현식의 결과값과 case 문의 오른쪽 값을 비교
- break 및 default문은 [선택적]으로 사용 가능
- break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
- 블록 스코프 생성

#### 예시

- break가 있는 경우

```javascript
const nation = 'Korea'

switch (nation) {
    case 'Korea' :{
    console.log('안녕하세요!')
    break
	}
	case 'France' : {
    console.log('Bonjur!')
    break
	}
    default:{
        console.log('Hello!')
    }
}
//Korea
```

- break가 없는 경우
  - Fall-through 이 경우에는 모두 출력 

```javascript
const nation = 'France'

switch (nation) {
    case 'Korea' :{
    console.log('안녕하세요!')
	}
	case 'France' : {
    console.log('Bonjur!')
	}
    default:{
        console.log('Hello!')
    }
}
//France
//Hello!
```



#### if vs switch

- if

```javascript
const numOne = 5
const numTwo = 10
let operator = '+'

if (operator === '+'){
    console.log(numOne + numTwo)
}else if (operator === '-') {
    console.log(numOne-numTwo)
}else if (operator === '*'){
    console.log(numOne * nomTwo)
}else if (operator === '/') {
    console.log(numOne/numTwo)
}else {
    console.log('유효하지 않은 연산자입니다. ')
}
```

- switch

```javascript
const numOne = 5
const numTwo = 10
let operator = '+'

switch(operator) {
    case '+' :{
        console.log(numOne + numTwo)
        break
    }
    case '-' :{
        console.log(numOne-numTwo)
        break
    }
    case '*' :{
        console.log(numOne * numTwo)
        break
    }
    case '/' :{
        console.log(numOne/numTwo)
        break
    }
    default:{
        console.log('유효하지 않은 연산자입니다.')
    }
}
```

