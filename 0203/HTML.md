#### 크롬 개발자 도구

- 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공
- 주요 기능
  - Elements - Dom 탐색 및 CSS 확인 및 변경
    -  Styles - 요소에 적용된 CSS 확인
    - Computed - 스타일이 계산된 최종 결과
    - Event Listeners - 해당 요소에 적용된 이벤트(JS)
  - Sources, Network, Performance, Application, Security, Audits 등

## HTML 기본 구조

- html : 문서 최상위(root)요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용 

#### head  예시

- title : 브라우저 상단 타이틀
- meta : 문서레벨 메타데이터 요소
- link : 외부 리소스 연결 요소 (css파일, favicon 등)
- script : 스크립트 요소(javascript 파일 코드) 
- style : CSS 직접 작성

```  html
<head>
    <title>HTML 수업</title>
    <meta charset="UTF-8">
    <link href="style.css" rel="stylesheet">
    <script src="javascript.js"></script>
    <style>
    p {
      color: black
     }
    </style>
	
</head>
```

### head 예시 :Open Graph Protocol

- 메타데이터를 표현하는 새로운 규약
  - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의



### DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에 렌더링 하기 위한 구조 
  - HTML 문서에 대한 모델을 구성함 
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함 



### 속성 작성 방식 통일 

- 쌍따옴표 쓰기 
- href='ww.~~' 할 때 공백 금지 
- 열기 닫기 잘 안하면 디버깅 힘듬 



### HTML Global Attribute

모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성

- id : 문서 전체에서 유일한 고유 식별자 지정

- class : 공백으로 구분된 해당 요소의 클래스의 목록
- data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
-  style : inline 스타일
- title : 요소에 대한 추가 정보 지정
- tabindex : 요소의 탭 순서 