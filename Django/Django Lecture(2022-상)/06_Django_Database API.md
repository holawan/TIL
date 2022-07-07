## Database API

### DB API

- DB를 조작하기 위한 도구
- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듬
- database-abstract API 혹은 database-access API라고도 함 

#### DB API 구문 - Making Queries

- ex) Article은 Class명, objects는 Manager, all()은 QuerySet API

```python
Article.Objects.all()
```

- Manager
  - Django 모델에 데이터베이스 Query 작업이 제공되는 인터페이스
  - 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가
- QuerySet
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음

#### Django shell

- 일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
- 그래서 장고 프로젝트설정이 load된 Python shell을 활용해 DB API구문 테스트 진행
- 기본 Django shell보다 더 많은 기능을 제공하는 Shell_plus를 사용해서 진행 
  - django-extension 설치 필요 

#### 라이브러리 설치

```
$ pip install ipython
$ pip install django-extensions
```

INSTALLED_APPS에 추가

shell_plus 실행

```
$python manage.py shell_plus
```
