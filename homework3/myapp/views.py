from django.shortcuts import render
from django.http import HttpResponse
      
def homework3(request):
    if request.method == 'POST':
        # 1. 取得多選框的所有選項（注意：名稱必須與 HTML 的 name="userinterest" 完全一致）
        userinterest = request.POST.getlist('userinterest')  
        
        # 2. 順便取得其他欄位的輸入資料
        username = request.POST.get('username')       # 姓名
        usersex = request.POST.get('usersex')         # 性別
        userschool = request.POST.get('userschool')   # 學歷
        userthought = request.POST.get('userthought') # 臉書看法
        
        # 在終端機印出測試
        print("勾選的活動：", userinterest)
        print(f"姓名: {username}, 性別: {usersex}, 學歷: {userschool}")
        
        # 3. 將所有資料打包成字典，傳送給回應頁面 hw3_response.html
        context = {
            'username': username,
            'usersex': usersex,
            'userschool': userschool,
            'userinterest': userinterest,  # 這是勾選活動的陣列
            'userthought': userthought
        }
        return render(request, 'hw3_response.html', context)
        
    else:
        # GET 請求：顯示原本的表單頁面
        return render(request, 'homework3.html')
