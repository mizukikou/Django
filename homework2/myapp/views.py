from django.shortcuts import render
from django.http import HttpResponse

def homework2(request, username):
    print(username)
    # locals() 會將這裡的 username 變數自動打包送給 HTML 網頁
    return render(request, 'show.html', locals())
