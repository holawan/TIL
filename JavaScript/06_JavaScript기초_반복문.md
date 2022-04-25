# JavaScript 기초

## 반복문

### 반복문 종류와 특징

- while
- for
- for ... in
  - 주로 객체(obejct)의 속성들을 순회할 때 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
- for ... of
  - 반복 가능한(iterable)객체를 순회하며 값을 꺼낼 때사용
    - Array, Map, Set, string 등

### while

- 조건문이 참인 동안 반복 시행
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
while (condition) {
    //do something
}
```

```javascript
let i =0
while (i<6) {
    console.log(i) //0,1,2,3,4,5
    i += 1 
}
```

### for

- 세미콜론(;)으로 구분되는 세 부분으로 구성
- initialization
  - 최초 반복문 진입 시 1회만 실행되는 부분
- condition
  - 매 반복 시행 전 평가되는 부분
- expression
  - 매 반복 시행 이후 평가되는 부분
- 블록 스코프 생성

```javascript
for (initialization; condition; expression){
    //do something
}
```

```javascript
for (let i=0; i<6; i++) {
    console.log(i) //0,1,2,3,4,5,6
}
//1. 반복문 진입 및 변수 i 선언 (let i =0;)
//2. 조건문 평가 후 코드 블럭 실행 (i<6)
//3. 코드 블록 실행 이후 i 값 증가(i ++)
```



### for ..in

- 객체(obejct)의 속성(key)들을 순회할 때사용
  - javascript에서 객체는 dictionary를 의미하는 경우가 많다. 

- 배열도 순회 가능하지만 권장하지 않음
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
for (variable in object) {
    //do something
}
```

```javascript
// object(객체) > key-balue로 이루어진 자료 구조
const capitals = {
    korea : 'seoul',
    france : 'paris',
    USA : 'washington D.C.'
}

for (let nation in capitals){
    console.log(nation) //korea, france, USA
}
for (let nation in capitals){
    console.log(capitals[nation]) //seoul, paris,washington D.C
}
```

### for ...of

- 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
for (variable of iterables) {
    //do something
}
```

```javascript
const fruits = ['딸기', '바나나','메론']
for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}

for (const fruit of fruits) {
    //재할당 불가
    console.log(fruit)
}
```

### for ...in vs for ...of

- for ...in(객체 순회 적합)

```javascript
///aray
const fruits = ['딸기', '바나나','메론']

for (let fruit in fruits) {
    console.log(fruit) //0,1,2
}

//object
const capitals = {
    korea : 'seoul',
    france : 'paris',
    USA : 'washington D.C.',
}

for (let capital in capitals){
    console.log(capital) //korea, france, USA
}
```

- for ...of(배열 순회 적합)

```javascript
//object
const capitals = {
    korea : 'seoul',
    france : 'paris',
    USA : 'washington D.C.'
}

for (let capital in capitals){
    console.log(capital) //korea, france, USA
}const fruits = ['딸기', '바나나','메론']
for (let fruit of fruits) {
    console.log(fruit) ///딸기, 바나나, 메론
}

//object
const capitals = {
    korea : 'seoul',
    france : 'paris',
    USA : 'washington D.C.'
}

for (let capital in capitals){
    console.log(capital) // Uncaught TypeError : capital is not iteralbe
}
```

### 조건문과 반복문 정리

| 키워드     | 종류   | 연관 키워드          | 스코프     |
| ---------- | ------ | -------------------- | ---------- |
| if         | 조건문 | -                    | 블록스코프 |
| switch     | 조건문 | case, break, default | 블록스코프 |
| while      | 반복문 | break, continue      | 블록스코프 |
| for        | 반복문 | break, continue      | 블록스코프 |
| for ... in | 반복문 | 객체 순회            | 블록스코프 |
| for ... of | 반복문 | 배열등 iterable순회  | 블록스코프 |

