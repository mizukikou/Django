from django.shortcuts import render
from django.http import HttpResponse


def sayhello(request):
    return HttpResponse("<b>Hello World 40!!!!!</b>")

def hello1(request,username):
    print(username)
    return HttpResponse(f"<b>Hello {username}!!!!!</b>")

from datetime import datetime  
def hello2(request,username):
    print(username)
    now = datetime.now()  # get current date and time
    current_time = now.strftime("%H:%M:%S")  # format time as HH
    print("Current Time =", current_time)
    # return HttpResponse(f"<b>Hello {username}!!!!!</b>")
    return render(request, 'hello2.html', locals())
  
def hello3(request,username):
    print(username)
    now = datetime.now()  # get current date and time
    current_time = now.strftime("%H:%M:%S")  # format time as HH
    print("Current Time =", current_time)
    # return HttpResponse(f"<b>Hello {username}!!!!!</b>")
    return render(request, 'hello3.html', locals())