from django.shortcuts import render, redirect
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
    # ORM
    resultlist = Students.objects.all()
    for result in resultlist:
        print(model_to_dict(result))
    data_count = resultlist.count()
    print(f"資料總筆數：{data_count}")
    return render(request, "index.html", locals())
  
def post(request):
    # return HttpResponse("Hello, world. You're at the post index.")
    if request.method == "POST":
        # 讀取前端表單送來的資料
        cname = request.POST.get("cname")
        cid = request.POST.get("cid")
        csex = request.POST.get("csex")
        cemail = request.POST.get("cemail")
        cphone = request.POST.get("cphone")
        cbirthday = request.POST.get("cbirthday")
        caddr = request.POST.get("caddr")

        print(f"已新增學生資料：cname={cname}, cid={cid}, csex={csex}, cemail={cemail}, cphone={cphone}, cbirthday={cbirthday}, caddr={caddr}")
        # 將讀取到的資料寫入資料庫
        add = Students(cname=cname, cid=cid, csex=csex, cemail=cemail, cphone=cphone, cbirthday=cbirthday, caddr=caddr)
        add.save()
        return redirect("/index/") # 新增資料後，導向到首頁
    else:
        return render(request, "post.html", locals())
      
def edit(request, cid):
    # 讀取指定 cid 的學生資料
    student = Students.objects.get(cid=cid)
    print(model_to_dict(student))
    if request.method == "POST":
        # 讀取前端表單送來的資料
        student.cname = request.POST.get("cname")
        student.csex = request.POST.get("csex")
        student.cemail = request.POST.get("cemail")
        student.cphone = request.POST.get("cphone")
        student.cbirthday = request.POST.get("cbirthday")
        student.caddr = request.POST.get("caddr")

        print(f"已更新學生資料：cname={student.cname}, cid={student.cid}, csex={student.csex}, cemail={student.cemail}, cphone={student.cphone}, cbirthday={student.cbirthday}, caddr={student.caddr}")
        
        # 將更新後的資料寫入資料庫
        student.save()
        return redirect("/index/") # 更新資料後，導向到首頁
    else:
        return render(request, "edit.html", {"student": student})
      
def delete(request, cid):
    if request.method == "POST":
        # 讀取指定 cid 的學生資料
        student = Students.objects.get(cid=cid)
        print(model_to_dict(student))
        
        # 刪除該筆學生資料
        student.delete()
        print(f"已刪除學生資料：cname={student.cname}, cid={student.cid}")
        
        return redirect("/index/") # 刪除資料後，導向到首頁
    else:
        # 讀取指定 cid 的學生資料
        student = Students.objects.get(cid=cid)
        print(model_to_dict(student))
        return render(request, "delete.html", {"student": student})
  