from django.shortcuts import render
from django.http import HttpResponse

import random
from django.shortcuts import render

# 移除 username 參數
def lotto1(request):
    
    numbers = random.sample(range(1, 6), 5)  # 生成 5 個不重複的隨機數字
    print(numbers)
    return render(request, 'lotto1.html', locals())
  


