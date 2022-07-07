## URL

### Variable routing

- URL 주소를 변수로 사용하는 것

- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

  - 사용예시

  ```python
  path('account/user/<int:user_pk>/',views.user)
  ```

  - accounts/user/1 -> 1번 user페이지
  - accounts/user/2 -> 2번 user 페이지 

- 동적 라우팅
  - 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것

### URL Path converters

- str
  - '/'를 제외하고 비어 있지 않은 모든 문자열과 매치
  - 작성하지 않을 경우 기본 값
- int
  - 0 또는 양의 정수와 매치
- slug
  - ASCII  문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 모든 슬러그 문자열과 매치
  - ex) 'building-your-1st-django-site'

```python
# urls.py

urlpatterns = [
    ...,
    # path('hello/<name>/', views.hello),
    path('hello/<str:name>/', views.hello),
]
```

```python
# views.py

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```

```django
<!-- hello.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워 {{ name }}!</h1>
{% endblock %}
```



### App URL mapping

- 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁하게 가능
- app의 view 함수가 많이자면서 사용하는 path() 또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- 각 app에 urls.py를 작성해 URL을 매핑시킨다. 

**두번째 app 생성 및 등록**

```bash
$ python manage.py startapp pages
```

```python
INSTALLED_APPS = [
    'articles',
    'pages',
    ...,
]
```

```python
# articles/urls.py

from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
```

```python
# pages/urls.py

from django.urls import path


urlpatterns = [

]
```

**[주의] urlpatterns list가 없는 경우 에러가 발생한다.**

### Including other URLconfs

```python
# firstpjt/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

#### include()

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도움
- 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달
- Django는 명시적 상대경로(`from .module import ..`)를 권장



### Naming URL patterns

- Django는 URL에 이름을 지정하는 방법을 제공하므로써 뷰 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움
- Django Template Tag 중 하나인 url 태그를 사용해서 path() 함수에 작성한 name을 사용할 수 있음
- url 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음

```python
# articles/urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
```

### url tag 사용하기

```django
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock %}
```

```django
{% url '' %}
```

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않고 링크를 출력하는 방법



### Namespace

- 개체를 구분할 수 있는 범위를 나타내는 namespace

**두번째 app의 index 페이지 작성**

```python
# pages/urls.py

from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

```django
<!-- pages/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>두번째 앱의 index</h1>
{% endblock %}
```

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'dtl_practice' %}">dtl-practice</a>
  <a href="{% url 'throw' %}">throw</a>

  <a href="{% url 'index' %}">두번째 앱 index로 이동</a>
{% endblock %}
```

#### 2가지 문제

1. articles app index 페이지에서 두번째 앱 index로 이동 하이퍼 링크를 클릭 시 현재 페이지로 이동
   - `URL namespace`
2. pages app index url로 이동해도 articles app의 index 페이지 출력
   - `Template namespace`

### URL namespace

**app_name attribute 작성**

```python
# pages/urls.py

app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
]
```

#### 'app_name' attribute

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
- urls.py에 `app_name` attribute 값 작성

##### 참조

- `:` 연산자를 사용하여 지정
  - 예를들어, app_name이 `articles`이고 URL name이 `index`인 주소 참조는 `articles:index`

#### URL tag 변경

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'articles:greeting' %}">greeting</a>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:throw' %}">throw</a>

  <h2><a href="{% url 'pages:index' %}">두번째 앱 index로 이동</a></h2>
{% endblock %}
```



### Template namespace

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, INSTALLED_APPS에 작성한 app 순서로 tamplate을 검색 후 렌더링

- 임의로 templates의 폴더 구조를 `app_name/templates/app_name` 형태로 변경해 임의로 이름 공간 생성 후 변경된 추가 경로 작성

  ```python
  # articles/views.py
  
  return render(request, 'articles/index.html')
  ```

  ```python
  # pages/views.py
  
  return render(request, 'pages/index.html')
  ```