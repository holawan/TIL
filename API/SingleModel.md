## SingleModel

### DRF with Single Model

- 단일 모델의 data를 직렬화(serialization)하여 JSON으로 변화는 방법에 대한 학습
- 단일 모델을 두고 CRUD 로직을 수행 가능도록 설계
- API 개발을 위한 핵심 기능을 제공하는 도구 활용
  - DRF built-in form
  - POSTMAN

#### POSTMAN

- API를 구축하고 사용하기 위해 여러 도구를 제공하는 API 플랫폼
- 설계, 테스트, 문서화 등의 도구를 제공하으로써 API를 더 빠르게 개발 및 생성 할 수 있도록 도움 



### ModelSerializer

- 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shorcut
- 아래 핵심 기능을 제공
  - 모델 정보에 맞춰 자동으로 필드 생성
  - serializer에 대한 유효성 검사기를 자동으로 생성
  - .create() & . update() 의 간단한 기본 구현이 포함됨 

- Model의 필드를 어떻게 '직렬화' 할 지 설정하는 것이 핵심
- 이 과정은 Django에서 Model의 필드를 설정하는 것과 동일함 

```python
#articles/serializer.py
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id','title')
```

### Serializer in Shell

##### 단일객체 직렬화 

```shell
#작성한 Serializer import
>>> from articles.serializers import ArticleListSerializer
#기본 인스턴스 구조 확인 
>>> serializer = ArticleListSerializer()
>>> serializer
ArticleListSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=100)
# Model instance 객체 
>>> article = Article.objects.get(pk=3)
>>> article
<Article: Article object (3)>
#직렬화 
>>> serializer = ArticleListSerializer(article)
>>> serializer
ArticleListSerializer(<Article: Article object (3)>):
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=100)
>>> serializer.data
{'id': 3, 'title': 'Along several increase teacher to wind kid stock.'}
```

##### QuerysSet 객체 many=True 옵션 없이 직렬화 

```shell
>>> serializer = ArticleListSerializer(articles)
>>> serializer.data
Traceback (most recent call last):
  File "C:\Users\SAMSUNG\Desktop\SSAFY\Django\07_DRF\01_drf\venv\lib\site-packages\rest_framework\fields.py", line 457, in get_attribute
    return get_attribute(instance, self.source_attrs)
  File "C:\Users\SAMSUNG\Desktop\SSAFY\Django\07_DRF\01_drf\venv\lib\site-packages\rest_framework\fields.py", line 97, in get_attribute
    instance = getattr(instance, attr)
AttributeError: 'QuerySet' object has no attribute 'title'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\SAMSUNG\Desktop\SSAFY\Django\07_DRF\01_drf\venv\lib\site-packages\rest_framework\serializers.py", line 555, in data   
    ret = super().data
  File "C:\Users\SAMSUNG\Desktop\SSAFY\Django\07_DRF\01_drf\venv\lib\site-packages\rest_framework\serializers.py", line 253, in data   
    self._data = self.to_representation(self.instance)
  File "C:\Users\SAMSUNG\Desktop\SSAFY\Django\07_DRF\01_drf\venv\lib\site-packages\rest_framework\serializers.py", line 509, in to_representation
    attribute = field.get_attribute(instance)
  File "C:\Users\SAMSUNG\Desktop\SSAFY\Django\07_DRF\01_drf\venv\lib\site-packages\rest_framework\fields.py", line 490, in get_attribute
    raise type(exc)(msg)
AttributeError: Got AttributeError when attempting to get a value for field `title` on serializer `ArticleListSerializer`.
The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
Original exception text was: 'QuerySet' object has no attribute 'title'.
>>>    
```

##### many =True 설정 

```shell
#many =True 설정 
>>> serializer = ArticleListSerializer(articles,many=True)
>>> serializer.data
[OrderedDict([('id', 3), ('title', 'Along several increase teacher to wind kid stock.')]), OrderedDict([('id', 4), ('title', '수정')]), OrderedDict([('id', 5), ('title', 'Major vote direction accept growth history.')]), OrderedDict([('id', 6), ('title', '제목')]), OrderedDict([('id', 7), ('title', 'title')])]
```

### 'many' argument

- many = True
  - "Serializing multiple objects"
  - 단일 인스턴스 대신 QuerySet 등을 직렬화하기 위해서는 serilizer를 인스턴스화 할 때 many=True를 키워드 인자로 전달해야 함 

### Build RESTful API

|             | GET          | POST    | PUT         | DELETE      |
| ----------- | ------------ | ------- | ----------- | ----------- |
| articles/   | 전체 글 조회 | 글 작성 |             |             |
| articles/1/ | 1번 글 조회  |         | 1번 글 수정 | 1번 글 삭제 |



### 1. GET - Article List

- url 및 view 함수 작성

```python
#urls.py

#views.py
```

