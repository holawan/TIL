# 파이썬 입력과 자료형 변환

### 데이터 입력 받기

```python
x = input()
x =  input("입력할 시 출력할 메세지 : ")
#입력할 시 출력할 메세지 : 하이 
print(x)
#하이
```

1. 할당연산자(=) 오른쪽부터 실행
2. input 함수 실행 시, 입력을 기다린다
3. 사용자가 데이터를 입력하고 엔터를 치면
4. input 함수 자리에 데이터가 들어간다. 



#### 사용자로부터 두개의 숫자를 입력 받고,더한 결과를 출력하기

```python
a = int(input("첫번째 숫자를 입력하세요 >>>>"))
b = int(input("두번째 숫자를 입력하세요 >>>>"))
#20
#40
print(a+b)
#60
```



#### 사용자로부터 태어난 연도를 입력받고, 현재 나이를 출력하기

```python

birth = int(input("태어난 연도를 입력해주세요>>>"))

from datetime import datetime

now = datetime.now().year
print(now-birth)
```

