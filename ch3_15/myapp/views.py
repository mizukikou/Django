from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
  
def useradd(request):
    if request.method == 'POST':
        # 處理表單提交邏輯
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        
        print("username:", username, "password:", password, "repassword:", repassword, "phone:", phone, "email:", email, "birthday:", birthday)

        # 這裡可以加入表單驗證邏輯，例如檢查密碼是否一致、檢查必填欄位等
        if password != repassword:
            messages.error(request, "密碼與確認密碼不一致")
            return render(request, 'useradd.html')

        # 如果驗證通過，可以將資料存入資料庫
        # 這裡假設有一個 User 模型
        User = get_user_model()
        # 檢查帳號是否已存在
        if User.objects.filter(username=username).exists():
            messages.error(request, "帳號已存在")
            return render(request, 'useradd.html')

        # 檢查帳密是否一致
        if password != repassword:
            messages.error(request, "密碼與確認密碼不一致")
            return render(request, 'useradd.html')
          
        # 如果帳號不存在，則創建新用戶
        user = User.objects.create_user(
          username=username, 
          password=password, 
          tel=phone, 
          email=email, 
          cBirthday=birthday
        )
        user.is_active = True
        user.save()
        messages.success(request, "用戶創建成功")
        return redirect('userlogin')
        

    else:
        return render(request, 'useradd.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "帳號或密碼錯誤")
            return render(request, 'userlogin.html')

    else:
        return render(request, 'userlogin.html')


def userlogout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/userlogin/')
def page1(request):
    return render(request, 'page1.html')