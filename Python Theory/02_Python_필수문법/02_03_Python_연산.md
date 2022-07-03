# 파이썬 연산

### 연산이란

- 수나 식을 일정한 규칙에 따라 계산하는 것 

### 연산의 종류

#### 대입연산

- 변수이름= 데이터

  ```python
  a = 3 
  print(a)
  # 3 
  ```

  - a에 3을 대입한다.

#### 산술연산

- 숫자연산

| 연산자 | 설명   |
| ------ | ------ |
| +      | 더하기 |
| -      | 빼기   |
| /      | 나누기 |
| //     | 몫     |
| %      | 나머지 |
| **     | 제곱   |

```python
x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y) # 나머지
print(x ** y) # 제곱
'''
7
3  
10 
2.5
2  
1  
25
'''
```

- 문자열 연산

```python
# - 문자열연산
tag1 = "#내꺼하자"
tag2 = "#오늘부터1일"
tag3 = "#여친생김"

tag = tag1 + tag2 + tag3
print(tag)
# #내꺼하자#오늘부터1일#여친생김
```

```python
message = "우린 모두 파이썬을 사랑합니다.\n" * 5
#\n은 줄바꿈 문자 
print(message)
'''
우린 모두 파이썬을 사랑합니다.
우린 모두 파이썬을 사랑합니다.
우린 모두 파이썬을 사랑합니다.
우린 모두 파이썬을 사랑합니다.
우린 모두 파이썬을 사랑합니다.
'''
```

#### 비교연산

| 연산자 | 설명        |
| ------ | ----------- |
| >      | 크다        |
| <      | 작다        |
| >=     | 크거나 같다 |
| <=     | 작거나 같다 |
| ==     | 같다        |
| !=     | 다르다      |



```python
x =2 ;y = 3 
print(x>y)
#False
print(x<y)
#True
print(x==y)
#False

print("- 비교연산 문제")
print(2 > 3) # False
print(15 < 30) # True
print(1.5 >= 0) # True
print(3 <= 3) # True
print("팙팗팚" == "팙팗팗") # False
print("1111111111111111111" != "111111111111111111") # True
```

#### 논리연산

| 연산자  | 설명                                  |
| ------- | ------------------------------------- |
| A and B | A, B 모두가 참이면 True               |
| A or B  | A,B 중 하나라도 참이면 True           |
| not A   | A가 참이라면 False, A가 거짓이면 True |

```python
print("- 논리연산 문제")
print(4 < 6 and 10 >= 10) # True and True -> True
print("포기하지말아요" != "포기하지말아요" or "나는 할 수 있다" == "나는 할 수 있다") # False or True -> True
print(not 5==5) # not True -> False
```

- and

```python
print(True and True)
#True
print(True and False)
#False
print(False and True)
#False
print(False and False)
#False

```

- or 

```python
print(True or True)
#True
print(True or False)
#True
print(False or True)
#True
print(False or False)
#False

```

#### 멤버십 연산

| 연산자 | 설명               |
| ------ | ------------------ |
| in     | 포함되어 있다      |
| not in | 포함되어 있지 않다 |



```python
print("a" in "abc") # 포함되어 있다면 True
print("d" not in "abc") # 포함되어 있지 않다면 True
```



#### 복합할당 연산자 

- +=, -=, *=, /=

```python

level = 10 # (레벨 1 증가)
level += 1 # level = level + 1

health = 2000 # (체력 300 감소)
health -= 300 # health = health - 300

attack = 300 # (공격력 1.5배 증가)
attack *= 1.5 # attack = attack * 1.5

speed = 420 # (이동속도 50% 감소)
speed /= 2 # speed = speed / 2
print(level, health, attack, speed)
```

