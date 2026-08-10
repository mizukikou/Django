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
    #return render(request, 'hello3.html', locals())
    return render(request, 'hello3_2.html', locals())
    return render(request, 'dice1.html', locals())
  
  
def hello4(request, username1, username2):
    # print(username1)
    # print(username2)
    return HttpResponse("Hello "+ username1 + " "+username2)
  
def dice1(request):
    import random
    #return HttpResponse(f"Dice roll: {random.randint(1,6)}")
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    print("Dice roll: ", no1, no2, no3)
    return HttpResponse(render(request, 'dice1.html', {'no1': no1, 'no2': no2, 'no3': no3}))
  
def dice2(request):
    student = {'id': 1234,'name':'john','sex':'M'}
    fruits = ['apple','banana','orange']
    print(f"student: {student}, fruits: {fruits}")
    return render(request, 'dice2.html', {'student': student, 'fruits': fruits})
  
def dice3(request):
    person1 = {'name': 'Alice','phone': '123-456-7890', 'age': 25}
    person2 = {'name': 'Bob','phone': '987-654-3210', 'age': 30}
    #person2 = []
    person3 = {'name': 'Charlie','phone': '555-555-5555', 'age': 35}
    people = [person1, person2, person3]
    print(f"people: {people}")
    # people = []
    return render(request, 'dice3.html', {'people': people})
  
def get1(request):
    if request.method == 'GET':
        #name = request.GET['name']  ## 如果沒輸入(空值),就會出錯
        #city = request.GET['city']  ## 如果沒輸入(空值),就會出錯
        # basic-07.py範例
        name = request.GET.get('name', 'None')  ## 如果網址沒給 name，變數就會自動變成 "訪客"
        city = request.GET.get('city','Null')  ## 如果網址沒給 city，變數就會自動變成 "Null"
        print(f"Received GET request with name: {name}, city: {city}")
        return render(request, 'get1.html', {'name': name, 'city': city})
    #else:
        #return HttpResponse("This view only handles GET requests.")
        
def get2(request):
    try:
        name = request.GET['name']  ## 如果沒輸入(空值),就會出錯
        city = request.GET['city']  ## 如果沒輸入(空值),就會出錯
        status = True
        print(f" Received GET request with name: {name}, city: {city}")
        return render(request, 'get2.html', {'name': name, 'city': city, 'status': status})
    except:
        status = False
        print(status)
        return HttpResponse("An error occurred while processing the request.")