## HTML Form

### HTML "form" element

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
- 핵심 속성
  - action : 입력 데이터가 전송될 URL 지정
  - method : 입력 데이터 전달 방식 지정

### HTML "input" element

- 사용자로부터 데이터를 입력 받기 위해 사용
- `type` 속성에 따라 동작 방식이 달라짐
- 핵심 속성
  - **name**
  - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name 은 key , value 는 value)로 `?key=value&key=value` 형태로 전달

### HTML "label" element

- 사용자 인터페이스 항목에 대한 설명(caption)을 나타냄
- label을 input 요소와 연결하기
  - input에 id 속성 부여
  - label에는 input의 id와 동일한 값의 for 속성이 필요
- label과 input 요소 연결의 주요 이점
  - 시각적인 기능 뿐만 아니라 화면 리더기에서 label을 읽어 사용자가 입력해야 하는 텍스트가 무엇인지 더 쉽게 이해할 수 있도록 돕는 프로그래밍적 이점도 있음
  - label을 클릭해서 input에 초점(focus)를 맞추거나 활성화(activate)시킬 수 있음 

### HTML "for" attribute

- for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소를 제어
  - 연결된 요소가 labelable elements인 경우 이 요소에 대한 labeled control이 됨
- "labelable elements"
  - label 요소와 연결할 수 있는 요소
  - button, input(not hidden type), select, textarea ...

### HTML "id" attribute

- 전체 문서에서 고유(must be unique) 해야 하는 식별자를 정의
- 사용목적
  - linking, scripting, styling시 요소를 식별 

### HTTP request methods

#### HTTP

- Hyper Text Transfer Protocol
  - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)


- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의
- HTTP request method 종류
  - GET, POST, PUT, DELETE


#### GET

- 서버로부터 **정보를 조회**하는 데 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버로 전송할 때 body가 아닌 **Query String Parameters**를 통해 전송
- 우리는 서버에 요청을 하면 HTML 문서 파일 한 장을 받는데, 이때 사용하는 요청의 방식이 GET

**throw & catch**

- throw

  ```python
  # first_project/urls.py
  
  path('throw/', views.throw),
  ```

  ```python
  # articles/views.py 
  
  def throw(request):
      return render(request, 'throw.html')
  ```

  ```html
  <!-- articles/templates/throw.html -->
  
  <form action="/catch/" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
  ```

- catch

  ```python
  # first_project/urls.py
  
  path('catch/', views.catch),
  ```

  ```python
  # articles/views.py
  
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message': message,
      }
      return render(request, 'catch.html', context)
  ```

  ```django
  <!-- articles/templates/catch.html -->
  
  <h1>너가 던져서 내가 받은건 {{ message }}야!</h1>
  <a href="/throw/">뒤로</a>
  ```



### Request object 

- 요청 간의 모든 정보를 담고 있는 변수
- 페이지가 요청되면 Django는 요청에 대한 메타 데이터를 포함하는 `HttpRequest` 객체를 만들고
- 그런 다음 Django는 적절한 view 함수를 로드하고 `HttpRequest`를 뷰 함수의 첫 번째 인수로 전달. 
- 그리고 각 view는 `HttpResponse` 개체를 반환한다.

