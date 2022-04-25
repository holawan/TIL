## Improve query

### 쿼리셋 이해하기

#### QuerySets are lazy

- '쿼리셋은 게으르다'
- 쿼리셋을 만드는 작업에는 데이터베이스 작업이 포함되지 않음
- 하루종일 필터를 함께 쌓을 수 있으며 (stack filters), Django는 쿼리셋이 '평가(evaluated) ' 될 때까지 실제로 쿼리를 실행하지 않음
- DB에 쿼리를 전달하는 일이 웹 애플리케이션을 느려지게 하는 주범 중 하나이기 때문

- 다음 구문에서 몇개의 쿼리가 DB에 전달될까?

```python
articles = Article.objects.filter(title__startswith='What')
articles = articles.filter(created_at__lte=datetime.date.today())
articles = articles.exclude(content__icontains='food')
print(articles)
```

##### pinrt(articles)에서 단 한 번 전달됨

- 즉 print가 평가의 개념

#### 평가

- 쿼리셋에 해당하는 DB의 레코드들을 실제로 가져오는 것
  - == ht, access, Queries database
- 평가된 모델들은 쿼리셋의 내장 캐시(cache)에 저장되며, 덕분에 우리가 쿼리셋을 다시 순회하더라도 똑같은 쿼리를 DB에 다시 전달하지 않음 

#### 캐시

- 데이터나 값을 미리 복사해 놓는 임시 장소
- 캐시의 접근 시간에 비해 '원래 데이터를 접근하는 시간이 오래 걸리는 경우' 또는 '값을 다시 계산하는 시간을 절약하고 싶은 경우'에 사용
- 캐시에 데이터를 미리 복사해 놓으면 계산이나 접근 시간 없이 더 빠른 속도로 데이터에 접근할 수 있다.
- 시스템의 효율성을 위해 여러분야에서 두루 사용됨 



### 쿼리셋이 평가되는 시점

1. Iteration

   - QuerySet은 반복 가능하며 처음 반복 할 때 데이터베이스 쿼리를 실행

   ```python
   for article in Article.objects.all() :
       print(article.title)
   ```

2. bool()

   - bool() 또는 if문 사용과 같은 bool 컨텍스트에서 QuerySet을 테스트하면 쿼리가 실행
   - 결과가 하나 이상 존재하는지 확인하기만 한다면 exist가 효율적 

   ```python
   if Article.objects.filter(title='Test') :
       print('hello')
   ```

3. 이외  Pickling/Caching, Slicing, repr(), len(), list() 에서 평가 됨 



### 캐시와 쿼리셋

- 각 쿼리셋에는 데이터베이스 액세스를 최소화하는 '캐시'가 포함되어 있음
  - 새로운 쿼리셋이 만들어지면 캐시는 비어있음
  - 쿼리셋이 처음으로 평가되면 데이터베이스 쿼리가 발생
    - Django는 쿼리 결과를 쿼리셋의 캐시에 저장하고 명시적으로 요청된 결과를 반환
    - 이후 쿼리셋 평가는 캐시 된 결과를 재사용

```python
#나쁜 예 (동일한 데이터베이스 쿼라기 두번 실행)
print([article.title for article in Article.objects.all()])
print([article.content for article in Article.objects.all()])

# 좋은 예
queryset= Article.objects.all()
print([article.title for article in queryset])
print([article.content for article in queryset])
```

#### 쿼리셋이 캐시되지 않는 경우

- 쿼리셋 객체이서 특정 인덱스를 반복적으로 가져오면 매번 데이터베이스를 쿼리

```python
queryset = Article.objects.all()
print(queryset[5]) #호출 
print(queryset[5]) #한 번 더
```

- 그러나 쿼리셋 전체가 이미 평가된 경우 캐시에서 확인

```python
[article for article in queryset]
print(queryset[5]) #캐시 사용
print(queryset[5]) #캐시 사용 
```



#### 쿼리셋 캐시 관련

1. with 템플릿 태그 사용하기

   - 쿼리셋의 캐싱 동작을 사용하여 더 간단한 이름으로 복잡한 변수를 캐시

   ```django
   {% with followers=person.followers.all followings=person.followings.all %}
   	<div>
           팔로워 : {{folowers|length}}/ 팔로잉 {{followings|length}}
   	</div>
   {% endwith %}
   ```

2. iterator() 사용하기
   - 객체가 많을 때 쿼리셋의 캐싱 동작으로 인해 많은 양의 메모리가 사용될 때 사용

