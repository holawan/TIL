## 장고 배포시 secretkey 비공개

### 시크릿 키 (SECRET_KEY)

- 장고 프로젝트를 생성하면, 메인 프로젝트에 settings.py가 자동으로 생성된다.

- 또한, 이 파일안에는 임의의 SECRET_KEY가 입력되어 있는데, 이 값은 데이터를 보호하는 역할을 하며, 이를 안전하게 유지해야한다고 한다.
- 그 이유는 키가 공개되어 있을 경우, 해당 키를 이용해서 서버를 조작할 수 있기 때문이다.

https://docs.djangoproject.com/ko/4.0/topics/signing/#protecting-the-secret-key



- 나는 아직 배포를 해보지 않고, Django 프로젝트를 github에 올려본적은 있는데, 그럴때마다 경고 메일이 온다.

![alret](00_Django_Secretkey.assets/alret.PNG)

해당 경고는 Django 프로젝트의 Secret Key가 공개되어있기 때문에 github 저장소가 보안에 취약하다고 알려주는 것이다.

**따라서, 지금부터 이를 어떻게 비공개 처리 하는지 알아보겠다.**

##### 참고 URL :https://django-environ.readthedocs.io/en/latest/



### Secret_key 비공개처리 

#### SECRET_KEY는 Django 프로젝트 settings.py 파일에 있다.

![sk](00_Django_Secretkey.assets/sk.PNG)

#### 이를 비공개 처리해주기 위해 .env 파일을 settings.py와 같은 위치에 생성한다.

![env](00_Django_Secretkey.assets/env.PNG)

- .env 파일 내부에 해당 코드를 작성한다.

```
DEBUG=on
SECRET_KEY=나의 시크릿 키 넣어주기 
DATABASE_URL=psql://urser:un-githubbedpassword@127.0.0.1:8458/database
SQLITE_URL=sqlite:///my-local-sqlite.db 
CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213 
REDIS_URL=rediscache://127.0.0.1:6379/1?
client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
```

- 이 때 SECRET_KEY는 띄어쓰기 등을 하지 않고, 그대로 넣어주어야 한다.
  - 연습용 프로젝트의 SECRET_KEY 첨부 

```
SECRET_KEY=django-insecure-*u@$^b=+(@t8^&f+kxyatvdgpgkwsw6h_gora_-d5#)y6xp=b1'
```

#### 그리고 settings.py에 해당 코드를 추가한다.

```python
import os,environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# reading .env file
environ.Env.read_env()
```

- BASE_DIR에 대한 설정은 원래 settings.py에 있기 때문에 원래 있는 코드를 지우고 작성해도 되고, 위 아래 있는 코드만 따로 복사 붙여넣기 해도 된다.

#### settings.py에서 SECRET_KEY를 변경한다

```python
SECRET_KEY = env('SECRET_KEY')
```

#### git ignore에 .env 추가

![gitignore](00_Django_Secretkey.assets/gitignore.PNG)

- env 파일이 git에 업로드 되지 않으므로 성공적으로 완료될 것이다.

#### 끝



### 추가

- 해당 과정은 따로 정리를 해두고, 프로젝트를 만들 때 즉시 적용하는 것이 좋다고 생각한다.

- 이미 프로젝트가 git에 업로드 되어있다면 과거 settings.py의 로그를 보고 secret_key를 공격자가 파악할 수 있을 것이다. 

  
