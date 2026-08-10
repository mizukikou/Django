from django.shortcuts import render
from django.http import HttpResponse

import random
from django.shortcuts import render

# 移除 username 參數
def lotto2(request):
    
    # 產生 6 組大樂透號碼
    lotto_groups = []   # 在使用「列表（List）」的 append() 方法之前，必須先告訴程式「這是一個空的列表」。
    for _ in range(6):  #不需要在迴圈內部用到計數器的值時，用_來代替變數名稱。
        numbers = sorted(random.sample(range(1, 43), 6))
        # 將每個個位數轉成補0的字串
        #formatted_numbers = [f"{num:02d}" for num in numbers]
        #lotto_groups.append(formatted_numbers)
        lotto_groups.append(numbers)
    print(lotto_groups)
    return render(request, 'lotto2.html', locals())
  


