from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayhello(request):
    return HttpResponse("<h1>Hello, World! 002</h1>")

def hello1(request, username):
    print(username)
    return HttpResponse(f"<h1>Hello {username}!</h1>")