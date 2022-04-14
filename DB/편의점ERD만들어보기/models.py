from django.db import models
from django.conf import settings

# Create your models here.
class ConvenienceStore(models.Model):
    # 지점 이름
    name = models.CharField(max_length=20)
    # 지점번호
    phone_num = models.CharField(max_length=20)
    # 지점위치
    location = models.TextField()
    # 직영점여부
    directly_manage = models.BooleanField()

class MainCategory(models.Model) :
    #메인 카테고리 이름
    category_main_name= models.CharField()
    #진열 위치
    display_position = models.IntegerField()

class SubCategory(models.Model) :
    #하위 카테고리 이름
    category_sub_name= models.CharField()
    #상위 카테고리 PK
    main = models.ForeignKey(MainCategory,on_delete=models.CASCADE)

class Product(models.Model):
    # FK
    convenience = models.ForeignKey(ConvenienceStore, on_delete=models.CASCADE)
    #카테고리 대분류
    category = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    # 상품가격
    product_price = models.IntegerField()
    # 유통기한
    life = models.DateTimeField()
    # 재고
    quantity = models.IntegerField()
    # 이벤트 상품여부
    event = models.BooleanField