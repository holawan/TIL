## Customizing authentication in Django

### Substituting a custom Usermodel

 ### User 모델 대체하기

- 일부 프로젝트에서는 Django의 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음
  - ex) username 대신 email을 식별 토큰으로 사용하는 것이 더 적합한 사이트
- Django는 User을 참조하는데 사용하는 AUTH_USER_MODEL 값을 제공하여, default user model을 재정의(override) 할 수 있도록 함
- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, 커스텀 유저 모델을 설정하는 것을 강력하게 권장 (highly recommentded)
  - 단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함 

#### AUTH_USER_MODEL

- User을 나타내는 모델
- 프로젝트가 진행되는 동안 변경할 수 없음
- 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함
- 기본 값: 'auth.User'(auth 앱의 User모델)
- 프로젝트 중간에 AUTH_USER_MODEL 변경하기
  - 모델 관계에 영향을 미치기 때문에 훨 씬 더 어려운 작업이 필요
  - 즉, 중간 변경은 권장하지 않으므로 초기에 설정하는 것을 권장

#### Custom User 모델 정의하기

- 관리자 권한과 함께 완전한 기능을 갖춘 User 모델을 구현하는 기본 클래스인 AbstractUser를 상속받아 새로운 User 모델작성 

- 기존에 Djagno가 사용하는 User 모델이었던 auth 앱의 User 모델을 accounts 앱의 User 모델을 사용하도록 변경
- admin site에 Custom User 모델 등록 

- 프로젝트 중간에 진행한다면 데이터베이스를 초기화 한 후 마이글에ㅣ션 진행
- 초기화 방법
  - db.sqlite3 파일 삭제
  - migrations 파일 모두 삭제 (파일명에 숫자가 붙은 파일만 삭제 )



#### Custom user & Built-in auth forms

- 기존 User모델을 사용하기 때문에 커스텀 User 모델로 다시 작성하거나 확장해야 하는 forms

  - UserCreationForm
  - UserChangeForm

- 커스텀 User 모델이 AbstractUser의 하위 클래스인 경우 다음과 같은 방식으로 form을 확장

  ```python
  from django.contrib.auth.forms import UserCreationForm
  form myapp.models import CustomUser
  
  class CustomUserCreationForm(UserCreationForm) :
      
      class Meta(UserCreationForm.Meta) :
          model = CustomUser
          fields = UserCreationForm.Meta.fiels + ('coustom_field')
  ```

  

#### get_user_model()

- 현재 프로젝트에서 활성화 된 사용자 모델을 반환
  - User 모델을 커스터미이징 한 상황에서는 Custom User 모델을 반환
- 이 때문에 Django는 User 클래스를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 참조해야 한다고 강조 
