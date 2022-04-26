# JavaScript 자료형

## lodash

### A modern JavaScript utility library

- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
- array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공
- 함수 예시
  - reverse, sortBy, range,random,cloneDeep ..

### 사용 예시

```html
<body>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js" integrity="sha512-WFN04846sdKMIP5LKNphMaWzU7YpMyCU245etK3g/2ARYbPK9Ub18eG+ljU96qKRCWh+quCY7yefSmlkQw1ANQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script>
    _.sample([1,2,3,4])// 3 (1개 랜덤추출)
    _.sampleSize([1,2,3,4,],2) //[2,3] (2개 랜덤 추출)

    _.reverse([1,2,3,4]) //[4,3,2,1]

    _.range(5) //[0,1,2,4]
    _.range(1,5) //[1,2,3,4]
    _.range(1,5,2) [1,3]
  </script>
</body>
```



```html
<body>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js" integrity="sha512-WFN04846sdKMIP5LKNphMaWzU7YpMyCU245etK3g/2ARYbPK9Ub18eG+ljU96qKRCWh+quCY7yefSmlkQw1ANQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script>
    const original = {a:{b:1}}
    const ref = original
    const copy = _.cloneDeep(original)
    
    console.log(original.a.b, ref.a.b, copy.a.b) //1,1,1
    ref.a.b = 10
    console.log(original.a.b, ref.a.b, copy.a.b)//10,10,1
    ref.a.b = 100
    console.log(original.a.b, ref.a.b, copy.a.b)//10,10,100
    
  </script>
</body>
```

