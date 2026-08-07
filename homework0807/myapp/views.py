from django.shortcuts import render
from django.http import HttpResponse

import random
from django.shortcuts import render

# 移除 username 參數
def lotto2(request):
    
    # 產生 5 組大樂透號碼
    lotto_groups = []
    for _ in range(6):
        numbers = sorted(random.sample(range(1, 50), 6))
        lotto_groups.append(numbers)

    return render(request, 'lotto2.html', locals())

