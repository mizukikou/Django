from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict

# Create your views here.
def search_list(request):
    # 💡 判斷前端發送的 HTTP GET 請求中，網址列是否帶有名為 'cname' 的參數（例如：?cname=小明）
    if 'cname' in request.GET:
        # 讀取並取出網址參數中 'cname' 欄位實際輸入的搜尋關鍵字字串
        cname = request.GET['cname']
        
        # 💡 查詢資料庫：使用 filter 篩選符合條件的資料
        # cname__icontains 代表進行「不區分大小寫」的關鍵字模糊搜尋（相當於 SQL 的 LIKE '%關鍵字%'）
        datas = Students.objects.filter(cname__icontains=cname)
        
        # 💡 檢查機制：如果資料庫中完全找不到任何一筆符合該關鍵字的學生紀錄
        if not datas.exists():
            # 直接中斷並在網頁上回傳「找不到資料」的純文字訊息
            return HttpResponse("No data found.")
            
        # 💡 若有找到資料，則呼叫 render 函數渲染網頁
        # 將篩選出來的學生清單（datas）打包放進字典中，傳遞給前端網頁範本 "serach_list.html"
        return render(request, "serach_list.html", {"datas": datas})
        
    # 💡 區塊路由：若網址列沒有帶任何 'cname' 參數，代表使用者要瀏覽完整的學生列表
    else:
        # 💡 查詢資料庫：使用 all() 撈取 Students 資料表內「所有」學生的完整紀錄
        datas = Students.objects.all()
        
        # 💡 檢查機制：如果目前資料庫是完全清空、沒有半筆學生資料的狀態
        if not datas.exists():
            # 直接中斷並在網頁上回傳「找不到資料」的純文字訊息
            return HttpResponse("No data found.")
            
        # 💡 若有資料，同樣呼叫 render 函數，將全部學生的清單傳遞給前端網頁範本進行列表展示
        return render(request, "serach_list.html", {"datas": datas})

    # datas = Students.objects.all()
    # for data in datas:
    #     print(type(data))
    #     print(model_to_dict(data))
        
    # return HttpResponse("Hello, world. You're at the search_list index.")
    # return HttpResponse(", ".join([f"{data.cname} ({data.cid})" for data in datas]))  
    # return render(request, "serach_list.html", {"datas": datas})
    
    datas = Students.objects.all()
    if not datas.exists():
        return HttpResponse("No data found.")
    return render(request, "serach_list.html", {"datas": datas})
  
def search_name(request):
    #  return HttpResponse("Hello, world. You're at the search_name index.")
    return render(request, "serach_name.html")

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")