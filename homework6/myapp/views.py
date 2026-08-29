from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict
from django.db.models import Q  # 💡 補上這一行
      
def homework6(request):
    # return HttpResponse("Hello, this is homework6 view.")
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

        # 🎯 新增：將資料存入資料庫內
        # 💡 注意：因為多選框 userinterest 是陣列型態（如 ['閱讀', '打球']），
        # 存入資料庫前，我們用逗號將它們串接成字串，以便符合大多數 Model 欄位設定。
        interest_str = ",".join(userinterest)
        
        # 假設您的 Model 名稱為 UserProfile（請依您的實際名稱為準）
        # 建立新物件並直接存入資料庫
        UserProfile.objects.create(
            username=username,
            usersex=usersex,
            userschool=userschool,
            userinterest=interest_str,  # 或是直接傳入陣列，取決於您的欄位型態
            userthought=userthought
        )
        
        # 3. 將所有資料打包成字典，傳送給回應頁面 hw6_response.html
        context = {
            'username': username,
            'usersex': usersex,
            'userschool': userschool,
            'userinterest': userinterest,  # 這是勾選活動的陣列
            'userthought': userthought
        }
        return render(request, 'hw6_response.html', context)
        
    else:
        # GET 請求：顯示原本的表單頁面
        return render(request, 'homework6.html')

# 用來處理「查看所有資料」的視圖
def show_all(request):
    try:
        users = UserProfile.objects.all()
        # 💡 因為資料庫取出的興趣是字串（例如 "閱讀,打球"），為了能在前端用 for 迴圈印出點點項目，
        # 我們在撈出資料時，順手把每個人的興趣轉回陣列（List）
        for user in users:
            if user.userinterest:
                user.userinterest = user.userinterest.split(',')
            else:
                user.userinterest = []
    except NameError:
        users = []
        
    context = {
        'users': users
    }
    return render(request, 'show_all.html', context)
