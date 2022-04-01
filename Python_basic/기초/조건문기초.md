# 제어문

## 제어문

파이썬은 기본적으로 위에서 아래로 순차적으로 명령 수행

특정상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함

제어문은 순서도(Flow chart)로 표현 가능 

## 조건문

조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용 

기본형식

- expression에는 참/거짓에 대한 조건식
  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 싱행
  - 이외의 경우 else이후 들여쓰기 되어있는 코드 블럭을 실행
    - else는 선택적으로 활용 가능함 

- ``` python
  #조건문을 통해 변수 num의 값의 홀수/ 짝수 여부를 출력하는 코드
  
  num = int(input('숫자입력:	'))
  if nm %2 : #if num% 2 ==1 :
    print('홀수입니다.')
  else :
    print('짝수입니다. ')
  ```
  
- 복수 조건문
  - 복수의 조건식을 활용할 경우 elif를 활용하여 표현함 
  
  - ``` python
      dust = 80
      
      if dust >150 :
        print('매우 나쁨')
      elif dust >80 :
        print('나쁨')
      elif dust >30 :
        print('보통')
      else :
        print('좋음')
      ```
  
- 중첩 조건문
  
  - 조건문은 다른 조건문에 중첩되어 사용될 수 있음
  
    - 들여쓰기를 유의하여 작성할 것 
  
  - ``` python
    dust = -10
    
    if dust >150 :
      print('매우나쁨')
      if dust >300 :
        print('실외 활동을 자제하세요')
    elif dust >80 :
      print('나쁨')
    elif dust >30 :
      print('보통')
    else :
      if dust >= 0:
        print('좋음')
      else :
        print('값이 잘못 되었습니다.')
    ```
  
  - 
  
- 조건 표현식
  - 조건표현식을 일반적으로 조건에 따라 값을 정할 때 활용

  - 삼항 연산자로 부르기도 함 

  - ``` python
      <true인 경우 값>if<expression>else<false인 경우 값>
      ```

  - 절대값 계산기

      - ``` python
          num = int(input('숫자 : '))
          value = num if num >=0 else -num
          ```

      - value는 num이 0보다 크면 그대로, 0보다 작으면 -num을 반환 즉 절대값 

  - ``` python
      num = 2 
      if num % 2 :
        result = '홀수'
      else :
        result = '짝수'
      print(result)
      
      result = '홀수' if num %2 else '짝수'
      print(result)
      ```

  - 같은 함수임 

- 반복문

  - 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

  - while문 

    - 조건식이 참인 경우 반복적으로 코드를 실행

    - 조건이 참인 경우 들여쓰기 되어있는 코드 블록 실행

    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적 실행

    - while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요

    - 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드

    - ``` python
      n = 0
      total = 0
      user_input = int(input())
      
      while n <= user_input :
        total += n
        n += 1
      print(total)
      ```

    - 

  - for 문 

    - 반복가능한 객체를 모두 순회하면 종료(별도의 종료조건이 필요없음)

    - For문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)요소를 모두 순회

      - 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음 

    - 문자열 순회

      ``` python
      chars = input()
      for char in chars:
        print(char)
      for i in range(1:len(chars)):
        print(chars[i])
      ```

    - 딕셔너리 순회

        - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

            ``` python
            grades = {'john' : 80, 'eric' : 90}
            for student in grades : 
              print(student)
            #john
            #eric
            for studnet in grades :
              print(student, grades[student])
            #john 80
            #eric 90
            ```

        - 추가메서드를 활용한 순회

            - keys() : Key로 구성된 결과

            - values() : value로 구성된 결과

            - items() : (Key, value)의 튜플로 구성된 결과

            - ``` python
                grades = {'john' : 80, 'eric' : 90}
                print(grades.keys())
                print(grades.values())
                print(grades.items())
                ```

        - enumerate 순회

            - 인덱스와 객체를 쌍으로 담은 열거형 객체 반환

                - (index, value)형태의 tuple로 구성된 열거 객체를 반환

                ``` python
                members = ['민수', '영희', '철수']
                for idx, member in enumerate(members) :
                  print(idx, member)
                  
                enumerate(members)
                list(enumerate(members))
                #[(0,'민수'), (1,'영희'), (2,'철수')]
                list(enumerate(members), start = 1)
                #[(1,'민수'), (2,'영희'), (3,'철수')]
                ```

        - List Comprehension

            - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
            - [<expression> for <변수> in <iterable>]
            - [<expression> for <변수> in <iterable> if <조건식> ]

            ``` python
            # 1~3의 세제곱 리스트 만들기
            cubic_list = []
            for number in range(1,4) :
              cubic_list.append(number ** 3)
              
            cubic_list
            # [1,8,27]
            
            [number **3 for number in range(1,4)]
            ```

        - Dictionary Comprehension

            - 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
            - {key:value for <변수> in <iterable>}
            - {key:value for <변수> in <iterable> if <조건식> }

             ``` python
             # 1 ~ 3의 세제곱 딕셔너리 만들기
             cubic_dict = {}
             
             for number in range(1,4) :
               cubic_dict[number] = number **3
             cubic_dict
             # {1: 1, 2: 8, 3:27}
             {number:number**3 for number in range(1,4)}
             ```

        ``` python
        #반복문과 조건문만 활용하여 1~30까지 숫자중에 홀수만 출력 
        for i in range(1:31) :
          if i %2 :
            print(i)
        ```

        

  - 반복 제어

    - break - 반복문을 종료

      - break문을 만나면 반복문은 종료

      - ``` python
        n = 0 
        while True :
          if n==3 :
            break
          print(n)
          n += 1
        
        for i in range(10) :
            if i >1 :
            	print('0과 1만 필요해')
                break
            print(i)
        ```
        
      - 

    - continue

      - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

          ``` python
          for i in range(6) :
              if i%2 ==0:
                  continue
              print(i)
          #continue를 만나면, 이후 코드인 print(i)가 실행되지 않고 바로 다음 반복을 시행
          # 즉 홀수만 출력 짝수는 건너뜀 
          ```
    
          
    
    - for-else
    
      - 끝까지 반복문을 실행한 이후에 else문 실행
        - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음

