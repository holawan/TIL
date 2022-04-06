## Django_form_class



### Intro

- 우리는 지금까지 HTML form, input을 통해서 사용자로부터 데이터를 받음
- 이렇게 직접 사용자의 데이터를 받으면 입력된 데이터의 유효성을 검증하고, 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시해야 함 
  - 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있음을 항상 생각해야 함
- 이렇게 사용자가 입력한 데이터를 검증하는 것을 '유효성 검증'이라고 하는데, 이 과정을 코드로 모두 구현하는 것은 많은 노력이 필요한 작업임
- Django는 이러한 과중한 작업과 반복 코드를 줄여줌으로써 이 작업을 훨씬 쉽게 만들어줌



### Django's forms

- Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
- Django는 Form과 관련한 유효성 검사를 단순화 하고 자동화 할 수 있는 기능을 제공하여 개발자로 하여금 직접 작성하는 코드보다 더 안전하고 빠르게 수행 하는 코드를 작성할 수 있게 함
- Django는 form에 관련된 작업의 아래 세 부분을 처리해 줌 
  - 렌더링을 위한 데이터 준비 및 재구성
  - 데이터에 대한 HTML form 생성
  - 클라이언트로부터 받은 데이터 수신 및 처리

###  The Django 'Form Class'

- Django Form 관리 시스템의 핵심
- Form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러메시지를 결정
- Django는 사용자의 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등 )과 반복 코드를 줄여 줌 



### Form 선언하기

```python
#forms.py
from django import forms

class ArticleForm(forms.Form) :
    # Models.py와 유사한 구조 (form 클래스를 상속받음)
    title = forms.CharField(max_length=10)
    #글자는 10글자로 고정 
    content = forms.CharField()
```

- Model을 선언하는 것과 유사하며 같은 필드타입을 사용(또한, 일부 매개변수도 유사함)
- forms 라이브러리에서 파생된 Form 클래스를 상속받음

```python
#new.html
  <h1>NEW</h1>
  <hr>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">back</a>
```

```python
#views.py new함수
def new(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html',context)
```

- Form의 정렬이나 옵션을 자유롭게 생성할 수 없는 문제 발생 

### Form rendering options

1. as_p()

   - 각 필드가 단락(\<p>태그로 감싸져서 렌더링 됨 )

2. as_ul()

   - 각 필드가 목록 항목(\<li> 태그)로 감싸져서 렌더링 됨 
   - \<ul> 태그는 직접 작성해야함 

3. as_table()

   - 각 필드가 테이블(\<tr> 태그)행으로 감싸져서 렌더링 됨
   - \<table> 태그는 직접 작성해야함 

   

#### as_p 적용 전

![기본_form](django_form.assets/기본_form.PNG)

#### as_p 적용 후 

![as_p 적용 후](django_form.assets/as_p 적용 후.PNG)

### Django의 HTML 요소 표현 방법 2가지

1. Form fields
   - input에 대한 유효성 검사 로직을 처리하여 템플릿에 직접 사용됨
2. Widgets
   - 웹 페이지의 HTML input 요소 렌더링
   - GET/POST 딕셔너리에서 데이터 추출
   - widgets은 반드시 Form fields에 할당 됨 

#### Widgets

- Django의 HTML input element 표현
- HTML 렌더링 처리
- 주의사항
  - Form Fields와 혼동되어서는 안됨
  - Form Fields는 input 유효성 검사를 처리
  - Widgets은 웹페이지에서  input element의 단순한 raw한 렌더링 처리 

```python
from django import forms

class ArticleForm(forms.Form) :
    # Models.py와 유사한 구조 (form 클래스를 상속받음)
    title = forms.CharField(max_length=10)
    #Textarea 위젯 사용 ! 
    content = forms.CharField(widget=forms.Textarea)
```

#### SELECT 만들기

