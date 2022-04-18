## Relation

### Like 구현하기

- 여러 유저가 한 Article에 좋아요를 누를 수 있고, 한 유저가 여러 Article에 좋아요를 누를 수 잇다.

#### model 구성

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
```

![error](django_relation.assets/error.PNG)

- error 발생 원인
  - user와 접근과 like_user의 접근이 겹쳤기 때문
  - user : Article이 1:N 관계일 때 참조 역참조를 article.user.all(), user.article_set.all()로 진행할 수 있었다.
  - 하지만 이번 like와 진행할 때 고려해보면 User : Article이 M:N관계이다. 그렇다면 참조를 article.like_user.all(),  **user.article_set.all()**로 역참조가 겹치는 문제가 발생한다.
  - 따라서 하나의 필드에 relate_name을 설정해줘서 문제를 해결해야한다. 일반적으로 M:N관계 모델에 이를 설정해준다. 

#### model 수정

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
```

