# Django URLs and Views and Models



### Views

```python
from django.shortcuts import render,redirect
from shortener.models import Users
# Create your views here.

def index(request) :
    #user중 이름이 admin인 것을 필터해서 그중 첫번째 것을 가져와라
    #없으면 none
    user = Users.objects.filter(username="admin").first()
    # user = Users.objects.get(username='admin')
    #email이 있으면 email에 email을 입력하고 아니면 anonymous User로 선언해라 
    email = user.email if user else "Anonymous User!"

    print(email)
    print(request.user.is_authenticated)
    #로그인이 되어있는지 확인 
    if request.user.is_authenticated is False :
        email = "Anonymous User!"

        print(email)
    return render(request,"base.html",{"welcome_msg" : f"Hello {email}!"})


def redirect_test(request):
    print("Go Redirect")
    #여기로 들어오면 index로 redirect하라 
    return redirect("index")
```



### Models 

```python
from django.db import models

# Create your models here.

from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser

class PayPlan(models.Model) :
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

#AbstractUser 상속받기 
class Users(AbstractUser) :
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING,null=True)

#장고 내부 USER 모델에과 onetoeone 관계만들어서 detail 관리하기 
class UserDetail(models.Model) :
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan,on_delete=models.DO_NOTHING)
```

### URLS 

```python
from django.contrib import admin
from django.urls import path
from shortener.views import index,redirect_test
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("redirect", redirect_test),
]
```



