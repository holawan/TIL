from django.shortcuts import render
import random
# Create your views here.
def dinner(request,foods,num):
    context = {
        'foods' : foods,
        'num' : num,
    }
    return render(request,'dinner.html',context)