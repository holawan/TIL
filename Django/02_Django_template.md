# Template

### Django Template Language(DTL)

- Django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
- 단순히 python이 HTML 에 포함 된 것이 아니며, 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- Python처럼 일부 프로그래밍 구조 (if, for 등)을 사용할 수 있지만, 이것이 해당 Python 코드로 실행되는 것은 아님

### DTL Syntax

1. Variable

   ```django
   {{ variable }}
   ```

   - ender를 사용하며 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것

   - 변수명은 영어, 숫자와 밑줄의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
     - 공백이나 구두점 문자 또한 사용 불가

   - dot(.)를 사용하여 변수 속성에 접근할 수 있음
   - render()의 세번째 인자로 {'key':value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨 

2. Filters

   ```django
   {{ variable|filter }}
   ```

   - 표시할 변수를 수정할 때 사용

   - 60개의 built-in template filters를 제공

   - 예시

     - name 변수를 모두 소문자로 출력

     ```django
     {{ name|lower}}
     ```

   - chained가 가능하며 일부 필터는 인자를 받기도 함 

   ```django
   {{ variable|truncatewords:30 }}
   ```

   

3. Tag

   ```django
   {% tag %}
   ```

   - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
   - 일부 태그는 시작과 종료 태그가 필요

   ```django
   {% if %}{% endif %}
   ```

   

4. Comments

```django
{# #}
```

- Django template에서 라인의 주석을 표현하기 위해 사용
- 아래처럼 유요하지 않은 템플릿 코드가 포함될 수 있음

```django
{# {% if _ %} texxt {%else%} #}
```

- 한 줄 주석에만 사용할 수 있음 (줄 바꿈이 허용되지 않음)
- 여러줄 주석은 {% comment %}와 {% endcomment %}사이에 입력
  - Ctrl + /

### Template inheritance

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수있는 블록을 정의하는 기본 “skeleton” 템플릿을 만들 수 있음

  ```python
  # settings.py
  
  TEMPLATES = [
      {
          ...,
          'DIRS': [BASE_DIR / 'firstpjt' / 'templates'],
  ...
  ]
  ```

  - `app_name/templates` 디렉토리 외 추가 경로 설정

### tags

##### extends

```django
{% extends '' %}
```

- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림

- 반드시 템플릿 최상단에 위치해야 함(== 템플릿의 첫번째 템플릿 태그여야 함)
  - 즉, 2개 이상 사용할 수 없음

##### block

- 하위 템플릿에서 재지정(overriden)할 수 있는 블록을 정의

- 하위 템플릿이 채울 수 있는 공간

- 가독성을 높이기 위해 선택적으로 `{% endblock %}` 태그에 이름 지정

  ```django
  {% block content %}
  {% endblock content %}
  ```

##### include

```django
{% include '' %}
```

- 템플릿을 로드하고 현재 페이지로 렌더링
- 템플릿 내에 다른 템플릿을 '포함(including)하는 방법'

### Template system

- 표현과 로직(view)을 분리

  - 우리는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각한다. 

  - 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 한다.


- 중복을 배제

  - 대다수의 동적 웹사이트는 공통 헤더, 푸터, 네이게이션 바 같은 사이트 공통 디자인을 갖는다. 

  - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야  한다.
  - 이것이 템플릿 상속의 기초가 되는 철학이다.  
