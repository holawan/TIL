## DB

### Foreign Key 

#### Foreign Key 개념

- 외래 키
- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 속성에 해당하고, 이는 참조되는 테이블의 기본 키(PK)를 가리킴
- 참조하는 테이블의 외래 키는 참조되는 테이블의 행 1개에 대응됨
  - 이  때문에 참조하는 테이블에서 참조되는 테이블의 존재하지 않는 행을 참조할 수 없음
- 참조하는 테이블의 행 여러개가 참조되는 테이블의 동일한 행을 참조할 수 있음

![forien_key](C:\Users\SAMSUNG\Desktop\forien_key.PNG)

- 참조하는 모델에서 외래 키는 참조되는 모델의 PK를 가리킨다.

#### Foreign Key 특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함 
- 참조 무결성
  - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
  - 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함 

#### Foreign Key field

- A many-to-one relationsship
- 2개의 위치 인자가 반드시 필요
  - 참조하는 model class
  - on_delete 옵션
- migrate 작업 시 필드 이름에 _id를 추가하여 데이터베이스 열 이름을 만듦
- 자기가 자기자신을 참조하는 경우도 있음

#### on_delete

- 외래키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할지를 정의
  - 게시글에 댓글이 있는데 게시글이 삭제되었을 때 댓글을 어떻게 처리할 것인가?
- 데이터 무결성을 위해 매우 중요한 설정
- on_delete 옵션에 사용 가능한 값들
  - **CASCADE**
  - PROTECT
  - SET_NULL
  - SET_DEFAULT
  - SET()
  - DO_NOTHING
  - RESTRICT

```python
class Comment(models.Model) :
    #게시글 참조 on_delete를 이용해 게시글이 삭제되면 댓글도 자동 삭제되게 설정
    # 참조하는 모델과 1:N 관계일 때, 소문자 단수형으로 사용
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) :
        return self.content
```

#### 데이터 무결성

- 데이터의 정확성과 일관성을 유지하고 보증하는 것을 가리키며, 데이터베이스나 RDBMS 시스템의 중요한 기능임
- 무결성 제한의 유형
  - 개체 무결성
    - PK의 개념과 관련

#### 데이터베이스의 ForeignKey 표현

- 만약 ForeignKey 인스턴스를 abcd로 생성하면 abcd_id로 만들어짐
- 하지만 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)으로 작성하는 것이 바람직함(1:N)

### 1:N 관계 related manager

#### 역참조('commet_set')

- Article(1) -> Comment(N)
- article.comment 형태로는 사용할 수 없고 article.commetn_set manager가 생성됨
- 게시글에 몇 개의 댓글이 작성되었는지 Django ORM이 보장할 수 없기 때문
  - article은 comment가 있을 수도 있고, 없을 수도 있음
  - 실제로 Article 클래스에는 Comment와 어떠한 관계도 작성되어 있지 않음

#### 참조 ('article')

- Comment(N) -> Article(1)
- 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로, comment.article과 같이 접근할 수 있음
- 실제 ForeignKeyField 또한 Comment 클래스에서 작성됨 

```sqlite
article.comment_set.all()
Out[4]: <QuerySet [<Comment: first comment>, <Comment: second comment>]>

In [8]: comments = article.comment_set.all()

In [9]: for comment in comments :
   ...:     print(comment.content)
   ...: 
first comment
second comment

```

##### Foreign_key argumetns  - 'related_name'

article.commet_set.all() -> 1:N관계에서의 조회

article.comments.all() -> M:N 관계에서 조회 하는 것을 권장 

```python
article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='comments')
```

- 위와 같이 변경하면 article.commetn_set은 더이상 사용할 수 없고 article.comments로 대체됨
- 역참조시 사용할 이름 수정 후 migration 필수 