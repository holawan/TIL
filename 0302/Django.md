# Django

- Django is a high-level **Python Web framework** that encourages rapid development and clean, pragmatic design.
- It takes care of much of the hassle of Web development, so **you can focus on writing your app without needing to reinvent the wheel.** (우리는 앱을 작성할 때 수레바퀴를 다시 만들 수 없이 만들 수 있다.)

### Web

- World Wide Web
- 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간

### Static web page(정적 웹 페이지)

- 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
- 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
- 모든 상황에서 모든 사용자에게 동일한 정보를 표시
- 일반적으로 HTML, CSS, JavaScript로 작성됨
- flat page라고 함 

![img](img/keyword.png)

- 클라이언트 : 네트워크를 통해 서버라는 시스템에 접속할 수 있는 응용 프로그램(데스크탑, 스마트폰, 웹 브라우저)
- 서버 : 클라이언트에게 네트워크를 통해 정보나 서비스를 제공하는 네트워크 서비스(django) 요청과 응답
- 요청 : 네이버의 메인 페이지를 줘! 크롬에서 www.naver.com검색
- 응답 : 네이버의 메인 페이지 html 파일을 제공함 

### Dynamic web page (동적 웹 페이지)

- 웹 페이지에 대한 요청을 받은 후 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
- 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때끄때 다름
- 서버 사이드 프로그래밍 언어(Python, Java, C++ 등)이 사용되며, 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

### Framework

- 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- Application framework라고도 함 
- Framework가 클래스, 라이브러리 등 다양한 툴 제공 개발자는 개발에만 집중 



### Web framework

- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함
- 동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework의 일종



### Django를 사용해야 하는 이유

- 검증된 python 언어 기반 web framework
- 대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용됨 



### Framework Architecture

- MVC Design Pattern (model-view-controller)
- 소프트웨어 공학에 사용되는 디자인 패턴 중 하나
- 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
- Django는 MTV Pattern이라고 함 (view를 templet으로 보고, controller를 view로 봄)



### MTV Pattern

- Model
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
- Template
  - 파일의 구조나 레이아웃을 정의
  - 실제 내용을 보여주는데 사용(presentation)
- View
  - HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김 

![img](img/mtv.png)

1. 서버에서 클라이언트로부터 요청을 받음 (HTTP)
2. URLS에서 요청을 받고 적절한 View를 찾아서 요청을 보냄
3. View는 HTML로 응답을 줄 수 있다.
   1. 사용자에게 보여줄 템플릿이 있다면 가져온다.
   2. 모델과 상호작용이 필요하면 상호작용을 진행한다.

### Django 실행

1. 가상환경 생성 및 화럿오하
2. Django 설치
3. 프로젝트 생성
4. 서버 켜서 로켓 확인하기
5. 앱 생성
6. 앱 등록



### Project & Application

- Project
  - project는 Application의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
  - 하나의 프로젝트는 여러 앱을 가짐
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함 

### 앱 등록

- 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 추가해야함
- INSTALLED_APPS
  - Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록

- 해당 순서를 지키지 않아도 과정에 문제가 없지만, 추후 advanced한 내용을 대비하기 위해 지키는 것을 권장



### 요청과 응답

