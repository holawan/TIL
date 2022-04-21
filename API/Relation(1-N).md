## 1:N Relation

### DRF with 1:N Relation

- 1:N 관계에서의 모델 data를 직렬화(serialization)하여 JSON으로 변환하는 방법
- 2개 이상의 1:N 관계를 맺는 모델을 두고 CRUD 로직을 수행하도록 설계

#### Model

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model) : 
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py seed articles --number=20
```



### 1. GET - Comment List

- CommentSerializer 작성

```python
class CommentSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Comment
        fields = '__all__'
```

- urls,views

```python
#urls.py
urlpatterns = [
    path('comments/',views.comment_list),
]
#views.py
@api_view(['GET'])
def comment_list(request) :
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments,many=True)
    return Response(serializer.data)
```

![comment_listview](Relation(1-N).assets/comment_listview.PNG)

### 2. GET - Comment_detail

```python
#urls.py
urlpatterns = [
    path('comments/<int:comment_pk>/', views.comment_detail),
]
#views.py
@api_view(['GET'])
def comment_detail(request, comment_pk) :
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
```

![comment_detail](Relation(1-N).assets/comment_detail.PNG)



### 3. POST - Create Comment 

- url 및 comment_create 함수 작성

```python
#urls.py
urlpatterns = [
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
#views.py
@api_view(['POST'])
def comment_create(request,article_pk) :
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
```

- 요청 보낸 결과 400에러 발생

  - 응답 : {"article":["This field is required."]}

  - 몇 번 게시글에 작성할지에 대한 명시가 없기 때문 

#### Passing Additional attributes to .save()

- .save() 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
  - 인스턴스를 저장하는 시점에서 추가 데이터 삽입이 필요한 경우 

```python
@api_view(['POST'])
def comment_create(request,article_pk) :
    article = get_object_or_404(Article,pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.save(article=article)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
```

- 유효성 검사에서 article이 없기 때문에 똑같이 400에러가 발생 
- 어떤 게시글에 작성하는 댓글인지 정보가 넘어오지 않았기 때문, 따라서 유효성 검사를 할 때 통과를 하지 못함 
- 읽기 전용 필드가 필요

#### Read Only Field

- 어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에 직렬화하는 과정에서 article 필드가 유효성 검사(is_valid)를 통과하지 못함
  - CommentSerializer에서 article field에 해당하는 데이터 또한 요청으로부터 받아서 직렬화 하는 것으로 설정되었기 때문

- 이때는 읽기 전용 필드 설정을 통해 직렬화하지 않고 반환값에만 해당 필드가 포함되도록 설정할 수 있음

```python
class CommentSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
```

- 이제 article은 직렬화는 되지 않지만 리턴에는 포함된다. 

### 4. DELETE * PUT - delete, update Comment

- Article 생성 로직에서와 마찬가지로 comment_detail 함수가 모두 처리할 수 있도록 구성 

```python
@api_view(['GET','PUT','DELETE'])
def comment_detail(request, comment_pk) :
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method=='GET' : 
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method=='DELETE' :
        comment.delete()
        data = {
            #pk는 url에서 가져온 article_pk이다. 
            'delete' : f'데이터 {comment_pk}번이 삭제 되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='PUT' :
        serializer = CommentSerializer(comment,data=request.data) 
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)
```

### 1:N Serializer

#### 특정 게시글에 작성된 댓글 목록 출력하기

- Serializer는 기존 필드를 override 하거나 추가 필드를 구성할 수 있음
- 우리가 작성한 로직에서는 크게 2가지 형태로 구성할 수 있음
  - PrimaryKeyRelatedFiedl
  - Nested relationships

##### case1) PrimaryKeyRelatedField

- pk를 사용하여 관계된 대상을 나타내는데 사용할 수 있음
- 필드가 to many relationships(N)를 나타내는데 사용되는 경우 many=True 속성 필요
- comment_set 필드 값을 form-data로 받지 않으므로 read_only=True 속성 필요

```python
class ArticleSerializer(serializers.ModelSerializer) :
    comment_set = serializers.PrimaryKeyRelatedField(many=True,read_only = True)
    class Meta:
        model = Article
        fields = '__all__'
```

- 역참조시 생성되는 comment_set을 다른 매니저 이름으로 override 할 수 있음
  - 단 다음과 같이 수정할 경우 이전 serializers.py에서의 클래스 변수명도 일치하도록 수정해야함

```python
class Comment(models.Model) : 
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='comments')
```

##### case2) Nested relationships

- 모델 관계상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첩될 수 있음
- 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음
- 두 클래스의 상하 위치 변경 

```python
class CommentSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
class ArticleSerializer(serializers.ModelSerializer) :
    comment_set = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
```



#### 특정 게시글에 작성된 댓글의 개수 구하기

- comment_set 매니저는 모델 관계로 인해 자동으로 구성되기 때문에 커스텀 필드를 구성하지 않아도 comment_set이라는 필드명을 fields 옵션에 작성만 해도 사용 할 수 있었음
- 하지만 지금처럼 별도의 값을 위한 필드를 사용하려는 경우 자동으로 구성되는 매니저가 아니기 때문에 직접 필드값을 작성해야함

##### 'source' argument

- 필드를 채우는데 사용할 속성 이름
- 점 표기법을 사용하여 속성을 탐색할 수 있음
- comment_set이라는 필드에 .(dot)을 통해 전체 댓글의 개수 확인 가능
- .count()는 built-in Queryset API 중 하나 

```python
class ArticleSerializer(serializers.ModelSerializer) :
    comment_set = CommentSerializer(many=True,read_only = True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
```

![comment_num](Relation(1-N).assets/comment_num.PNG)



#### 주의사항

- 특정필드를 override 혹은 추가한 경우 read_only_fields shorcut으로 사용할 수 없다.
- 불가능한 경우 예시

```python
class ArticleSerializer(serializers.ModelSerializer) :
    comment_set = serializers.PrimaryKeyRelatedField(many=True)
    comment_count = serializers.IntegerField(source='comment_set.count')
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('comment_set','comment_count')
```

