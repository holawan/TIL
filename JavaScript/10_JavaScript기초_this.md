# JavaScript 자료형

## this

### this is window? object

- JS의 this는 실행 문맥(execution context)에 따라 다른 대상을 가리킨다.
- class 내부의 생성자(constructor)함수
  - this는 생성되는 객체를 가리킴(python의 self)
- 메서드(객체.메서드명()으로 호출 가능한 함수)
  - this는 해당 메서드가 소속된 객체를 가리킴
- 위의 두가지 경우를 제외하면 모두 최상위 객체 (window)를 가리킴

```javascript
function getFullName(){
    return this.firstName + this.lastName
}

const me = {
    firstName : 'John',
    lastName : 'Doe',
    getFullName : getFullName,
}

const you = {
    firstName : 'Jack',
    lastName : 'Lee',
    getFullName : getFullName,
}

me.getFullName() //'JohnDoe'
you.getFullName() //JackLee'
getFullName() //NaN
```

### function 키워드와 화살표 함수 차이

- this.radiuses는 메서드(객체.메서드명()으로 호출 가능) 소속이기 때문에 정상적으로 접근 가능
- forEach의 콜백함수의 경우 메서드가 아님(객체.메서드명()으로 호출 불가능)
- 때문에 콜백함수 내부의 this는 window가 되어 this.PI는 정상적으로 접근 불가능
- 이 콜백함수 내부에는 this.PI에 접근하기 위해서 함수객체.bind(this) 메서드를 사용
- 이 번거로운 bind 과정을 없앤 것이 화살표 함수

```javascript
const obj = {
    pI:3.14,
    radiuses : [1,2,3,4,5],
    printArea : function(){
        this.radiuses.forEach(function (r) {
            console.log(this.PI * r *r)
        }.bind(this))
    },
}
```

```javascript
const obj = {
    PI : 3.14,
    radiuses : [1,2,3,4,5],
    printArea : function() {
        this.radiuses.forEach((r) => {
            console.log(this.PI * r *r)
        })
    },
}
```

#### Summary

- 함수 내부에 this 키워드가 존재할 경우
  - 화살표 함수와  function 키워드로 선언한 함수가 다르게 동작
- 함수 내부에 this 키워드가 존재하지 않을 경우
  - 완전히 동일하게 동작 
