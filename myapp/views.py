from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#時間函數
from datetime import datetime

#隨機變數
import random

def hello(request):
    #return HttpResponse("Hello World")
    return render(request, 'hello.html')

def hello1(request, username):
    now = datetime.now()
    #                                    傳遞的資料
    return render(request, 'hello1.html', locals())

#全域變數
times = 0

def hello2(request, username):
    global times #使用全域變數
    times = times+1
    local_times = times #全域轉區域
    now = datetime.now()
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dict = {"dice1": dice1, "dice2": dice2, "dice3": dice3}
    score = random.randint(0, 100)
    #                                    傳遞的資料(只能傳遞區域變數)
    return render(request, 'hello2.html', locals())
    #locals()字典內容:
    #{"username": username, "now": datetime.now(), "dice1": random.randint(1, 6), "dice2": random.randint(1, 6), "dice3": random.randint(1, 6), "dict": {"dice1": dice1, "dice2": dice2, "dice3": dice3}, 以此類推}

def students(request):
    std1 = {"name": "aaa", "sid": "001", "age": 20}
    std2 = {"name": "bbb", "sid": "002", "age": 21}
    std3 = {"name": "ccc", "sid": "003", "age": 19}
    stds = [std1, std2, std3]
    return render(request, 'std.html', locals())