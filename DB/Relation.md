## 1:N 관계

### User - Article (1:N)

```python
from django.conf import settings
user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
```

### User 모델 참조하기

1. settings.AUTH_USER_MODEL
   - User 모델에 대한 외래 키 또는 다대다 관계를 정의할 때 사용해야 함 
   - models.py에서 User모델을 참조할 때 사용
2. get_user_model()
   - 현재 활성화된 User 모델을 반환
     - 커스터마이징한 User 모델이 있을 경우에는 Custom User 모델, 그렇지 않으면 User를 반환 
     - User를 직접 참조하지 않는 이유
       - 장고에서 app이 실행되는 순서
         1. installed_app에서 순차적으로 app을 import
         2. 각 앱의 models를 import 
   - models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용 

#### USER와 ARticle간 모델 관계 정의 후 migrations

- null값이 허용되지 않는 user_id필드가 별도의 값 없이 article에 추가되려 하기 때문
- 1을 입력 후 enter
  - 현재 화면에서 기본값을 설정하겠다라는 의미
- 1을 입력 후 enter
  - 기존 테이블에 추가되는 user_id필드의 값을 1로 설정하겠다는 의미

