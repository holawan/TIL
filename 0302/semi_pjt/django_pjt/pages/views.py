from django.shortcuts import render
import random
# Create your views here.
def dinner(request):
    foods = ['짜파게티','불닭볶음면','김치찌개','뿌링클']
    people = ['철수','영희','맹구','짱구','훈이','수지']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'people' :people
    }
    return render(request,'dinner.html',context)