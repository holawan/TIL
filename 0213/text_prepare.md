# HTML

### Hyper Text Markup Language : 웹 페이지를 작성(구조화)하기 위한 언어

#### Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

#### Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

HTML이란 하이퍼링크를 통해 사용자가 한 문서에서 다른 문서로 접근할 수 있는 Hyper text와 태그등을 이용하여 문서나 데이터의 구조를 명시하는 언어인 Markup Language로 이루어진 웹 페이지를 구조화하기 위한 언어이다. 



## HTML 기본 구조 

- html : 문서 최상위(root)요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용 

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"> #메타데이터
  <meta http-equiv="X-UA-Compatible" content="IE=edge"> #메타디이터
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title> #브라우저 상단에 표시될 타이틀
</head>
<body>
  
</body>
</html>
```

#### head  예시

- title : 브라우저 상단 타이틀
- meta : 문서레벨 메타데이터 요소, 특수 태그로서 사이트의 디자인에는 전혀 영향을 미치지 않고 문서가 어떤 내용을 담고 있고, 문서의 키워드는 무엇이며, 누가 만들었는지 등의 문서 자체의 특성을 담고 있음.
  - facebook이나 instagram 링크를 공유하면 개괄적인 내용
- link : 외부 리소스 연결 요소 (css파일, favicon 등)
- script : 스크립트 요소(javascript 파일 코드) 
- style : CSS 직접 작성(인라인 요소)

``` html
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

## DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에 렌더링 하기 위한 구조 
  - HTML 문서에 대한 모델을 구성함 
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함 

## 요소

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그는 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들
  - br, hr, img, input, link, meta
- 요소는 중첩될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어질 수 있음

## 속성

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성들도 있음

### HTML Global Attribute

모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성

- id : 문서 전체에서 유일한 고유 식별자 지정

- class : 공백으로 구분된 해당 요소의 클래스의 목록
- data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
- style : inline 스타일
- title : 요소에 대한 추가 정보 지정
- tabindex : 요소의 탭 순서 

### 시맨틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장
  - 기존 영역을 의미하는 div태그를 대체하여 사용
- 대표적인 태그 목록
  - header : 문서 전체나 섹션의 헤더(머리말 부분)
  - nav : 네비게이션
  - aside :  사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer : 문서 전체나 섹션의 푸터(마지막 부분)
- Non semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함

### 인라인요소 vs 블록요소

#### 블록요소 

블록요소는 **모든 인라인 요소를 포함할 수 있으며, 블록요소도 포함**할 수 있습니다또한, 너비(width), 높이(height), 안쪽 여백(padding), 바깥 여백(margin)으로 **레이아웃 수정**을 할 수 있으며, 블록요소가 끝나는 지점에서 자동으로 줄바꿈이 됩니다

```
address`, `article`, `aside`, `audio`, `blockquote`, `canvas`, `dd`, `div`, `dl`, `fieldset`, `figcaption`, `figure`, `footer`, `form`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `header`, `hgroup`, `hr`, `noscript`, `ol`, `output`, `p`, `pre`, `section`, `table`, `ul`, `video
```

출처: https://uxgjs.tistory.com/44 [UX 공작소]

#### 인라인요소

인라인 요소는 **다른 인라인 요소를 포함**할 수 있으며, 기본적으로 **컨텐츠가 끝나는 지점가지 넓이**를 가지게 됩니다

또한, 너비(width), 높이(height)를 조절할 수 없으며, line-height(높낮이 조절) 혹은 text-align(텍스트 정렬)을 할 수 있으며, 블록 요소와 다르게 인라인 요소는 끝나는 지점에 줄바꿈이 없습니다.

```
a`, `abbr`, `acronym`, `b`, `bdo`, `big`, `br`, `button`, `cite`, `code`, `dfn`, `em`, `i`, `img`, `input`, `kbd`, `label`, `map`, `object`, `q`, `samp`, `small`, `script`, `select`, `span`, `strong`, `sub`, `sup`, `textarea`, `tt`, `var
```

출처: https://uxgjs.tistory.com/44 [UX 공작소]

### 텍스트 요소

- <a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
- <b> 굵은 글씨 요소
- <strong> 중요한 강조하고자 하는 굵은글씨 </strong>
- <i> 기울임 글씨 요소
- <em> 중요한 강조하고자 하는 기울임 글씨
- \<br> 텍스트 내에 줄바꿈 생성
- <img> src 속성을 이용하여 이미지 표현
- <span> 의미없는 인라인 컨테이너 

### 그룹 컨텐츠

- \<p>  하나의 문단
- \<hr> 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨
- \<ol> 순서가 있는 리스트
- \<ul> 순서가 없는 리스트
- \<pre> HTML에 작성한 내용을 그대로 표현 보통 고정폭 글꼴이 사용되고 공백 문자를 유지
- \<blockquote> 텍스트가 긴 인용문 주로 들여쓰기를 한 것으로 표현됨
- \<div> 의미없는 블록 레벨 컨테이너

# CSS

#### 스타일을 지정하기 위한 언어 선택하고, 스타일을 지정한다.

``` css 
#선택자
h1{
    color : blue;
    #선언
    font-size : 15px;
    # 속성 		# 값
}
```

### CSS

- CSS구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 : 어떤 스타일 기능을 변경할지 결정
  - 값 : 어떻게 스타일 기능을 변경할지 결정

### CSS 정의 방법

- 인라인(권장 X)
- 내부참조  \<style>
- 외부참조 - 분리된 CSS파일

### CSS with 개발자 도구

-  styles : 해당 요소에 선언된 모든 CSS
-  computed : 해당 요소에 최종 계산된 CSS

### CSS Selector

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형체 결합자, 인접 형체 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

```css
<style>
#전체 선택자
*{
    color : red;
}

#요소 선택자 
h2{
    color : orange;
}

h3,
h4{
    font-size:10px
}

#클래스 선택자
.green {
    color : green
}

#id 선택자
#purple {
    color:purple
}
#자식 결합자
.box > p{
    font-size : 30px
}
#자손 결합자
.box p {
    color : blue;
}
#일반 형제 결합자
p~span{
    color:red;
}
#인접형제 결합자
p+span{
    color: red;
}
```

#### CSS 적용 우선순위

1. 중요도
   - !important

2. 우선 순위
   - 인라인 > id > class, 속성, pseudo-class> 요소, pseudo-element

3. CSS 파일 로딩 순서

### CSS 상속

- CSS 는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
- 속성 중에는 상속이 되는 것과 되지않는 것들이 있따.
- 상속 되는 것 예시 
  - Text  관련 요소(font, color, text-align), opacity, visibility 등
- 상속되지 않는 것 예시
  - Box model 관련 요소, position 관련 요소

### 크기 단위 

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한)상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐 

### 결합자

- 자손 결합자
  - selectorA 하위의 모든 selecotr B 요소
- 자식 결합자
  - selectorA 바로 아래의 SelectorB요소
- 일반 형제 결합자
  - selectorA의 형제 요소 중 뒤에 위치하는 selector B 요소를 모두 선택
- 인접 형제 결합자
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

###  Box model

- 모든 HTML 요소는 box 형태로 되어있음
- 하나의 박스는 네 부분으로 이루어짐
  - content
  - padding
  - border
  - margin

``` css

반시계방향으로 작동! 
.margin-1{
    margin:10px;
    # 상하좌우 10
}
.margin-2{
    margin: 10px 20px;
    #상하 10 좌우 20
}
.margin-3{
    margin:10px 20px 30px;
    #상 10 좌우 20 하 30
}
.margin-4 {
    margin : 10px 20px 30px 40px;
    #상 10 우 20 하 30 좌 40
}
```

#### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - padding을 제외한 순수  contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border 까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box으로 설정 

#### 대표적으로 활용되는 display

- display : block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소안에 인라인 레벨 요소가 들어갈 수 있음
- display : inline 
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다. 
- display : inline-block
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시 가능하고, block 처럼 width, height, margin 속성을 모두 지정할 수 있음
- display : none 
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음 
  - 이와 비슷한 visibility : hidden은 해당 요소가 공간은 차지하거나 화면에 표시만 하지 않는다.

#### CSS position

- 문서 상에서 요소를 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative
    - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음(normal position 대비 offset)
  - absolute : 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
  - fixed : 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - 부모 요소와 관계없이 viewport를 기준으로 이동
      - 스크롤시에도 항상 같은 곳에 위치함 

#### CSS 원칙 1

모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.

display에 따라 요소간 배치가 달라짐

#### CSS 원칙2 

position으로 위치의 기준을 변경

- relative : 본인의 원래 위치
- absolute : 특정 부모의 위치 
- fixed : 화면의 위치 

# Flex

### Flex 속성

- 배치 설정

  - flex-direction
    - Main axis  기준 방향 설정
    - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)
    - row(행방향 정렬) row-reverse(행방향 역정렬) column(열방향 정렬) column-reverse(열방향 역정렬) 
  - flex-wrap
    - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
    - 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함 
      - nowrap(기본값) : 한 줄에 배치
      - wrap : 넘치면 그 다음줄로 배치

- 공간 나누기 

  - justify-content (main axis)
  - align-content (cross axis)
    - flex-start(기본 값) : 아이템들을 axis 시작점으로
    - flex-end : 아이템들을 axis 끝 쪽으로
    - center : 아이템들을 axis 중앙으로 
    - space-between : 아이템 사이의 간격을 균일하게 분배
    - space-around : 아이템을 둘러싼 영역을 균일하게 분배(가질 수 있는 영역을 반으로 나눠서 양쪽에)
    - space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배
  - Cross aixs 를 중심으로
    - stretch(기본 값) : 컨테이너를 가득 채움
    - flex-start : 위
    - flex-end : 아래 
    - center : 가운데
    - baseline : 텍스트 baseline에 기준선을 맞춤
  - 기타 속성
    - flex-glow : 남은 영역을 아이템에 분배
    - order : 배치 순서

- 정렬

  - align-items(모든 아이템을 cross axis 기준으로)

  - align-self (개별 아이템)

    