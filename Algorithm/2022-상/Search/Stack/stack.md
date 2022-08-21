## 스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.
- 스택에 저장된 자료는 선형 구조를 갖는다.
  - 선형구조 : 자료간의 관계가 1대 1의 관계를 갖는다.
  - 비선형구조 : 자료간의 관계가 1대 N의 관계를 갖는다. (ex. Tree)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 먼저 꺼낸다 후입선출(LIFO, Last-In-First-Out)
  - 예를 들어 스택에 1,2,3 순으로 자료를 삽입한 후 꺼내면 역순으로 즉 3,2,1 순으로 꺼낼 수 있다. 

## 스택의 구현

- 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산
  - 자료구조 : 자료를 선형적으로 저장할 저장소
    - 배열을 사용할 수 있다.
    - 저장소 자체를 스택이라고 부르기도 한다.
    - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다. 
  - 연산 
    - 삽입 : 저장소에 자료를 저장한다. 보통 push라고 부른다.
    - 삭제 : 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 pop이라고 부른다.
    - 스택이 공백인지 아닌지를 확인하는연산 . is Empty
    - 스택의 top에 있는 item을 반환하는 연산 (peek)
- 스택의 삽입 삭제과정
  - 빈 스택에 원소 A,B,C를 차례로 삽입 후 한번 삭제하는 연산과정 

- 스택의  push 알고리즘 

  - append 메소드를 통해 리스트의 마지막에 데이터를 삽입

  ```python
  def push(item) :
      s.append(item)     
  ```

  

- 스택의 pop 알고리즘

  ```python
  def pop() :
      if len(s) == 0 :
          #underflow
          return
     	else :
          return s.pop(-1)
  ```

  ```python
  def push(item,size) :
      global top
      top += 1 
      if top == size :
          print('overflow') #push가 너무 크거나, size가 너무 작거나 
         else :
          stack[top] = item
  size = 10
  stack = [0]*size
  top = -1
  
  push(10,size)
  top += 1     #push (20)
  stack[top] = 20
  ```

  ```python
  def push(item,size) :
      global top
      if top == -1 :
          print('underflow') #push가 너무 크거나, size가 너무 작거나 
         else :
          top -=1
          return stack[top+1]
  print(pop())
  
  if top > -1 :
      top -= 1 
      print(stack[top+1])
  ```

  