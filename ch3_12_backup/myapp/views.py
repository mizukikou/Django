from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict
from django.db.models import Q  # 💡 補上這一行


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
    # 1. 預設先抓取所有資料（如果沒有搜尋，就用這個）
    resultlist = Students.objects.all()
    search_query = "" # 對應前端網頁需要的變數名稱（HTML 裡是 {{ search_query }}）

    # 2. 檢查是否有收到搜尋要求
    if 'site_search' in request.GET:
        site_search = request.GET['site_search'].strip()
        
        # 🌟 關鍵修正：必須把抓到的關鍵字同步存入 search_query 變數中！
        # 這樣前端 HTML 的 value="{{ search_query }}" 和分頁連結才能順利讀到它
        search_query = site_search 
        
        print(f"使用者輸入的搜尋關鍵字：{site_search}")
        keyworks = site_search.split()  # 將使用者輸入的字串以空白切割成多個關鍵字
        print(f"切割後的關鍵字列表：{keyworks}")
        
        query = Q()  # 建立一個空的 Q 物件，用來累加多個搜尋條件
        for keyword in keyworks:
            query |= Q(cname__icontains=keyword) | Q(cid__icontains=keyword) | Q(cemail__icontains=keyword) | Q(cphone__icontains=keyword) | Q(caddr__icontains=keyword)
       
        resultlist = Students.objects.filter(query).order_by('-cid')  # 使用累加的 Q 物件進行資料庫查詢    
    else:
        print("沒有收到搜尋要求，顯示全部資料。")    
        resultlist = Students.objects.all().order_by('-cid')  # 如果沒有搜尋要求，則抓取所有資料並依照學號倒序排列

    data_count = resultlist.count()
    print(f"資料總筆數：{data_count}")
    
    # 分頁顯示，每頁顯示3筆資料
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    paginator = Paginator(resultlist, 3)  # 每頁顯示3筆資料
    page_number = request.GET.get('page') # 讀取網址列的 page 參數，決定要顯示哪一頁的資料, 如 ?page=2
    try:
        resultlist = paginator.page(page_number)
    except PageNotAnInteger:    # 如果 page 參數不是整數，則顯示第一頁
        resultlist = paginator.page(1)
    except EmptyPage:           # 如果 page 參數超過總頁數，則顯示最後一頁
        resultlist = paginator.page(paginator.num_pages)
    
    # 🌟 雙重保險：為了防止前端 HTML 有些地方寫 {{ site_search }}，有些寫 {{ search_query }}
    # 我們讓兩個變數的內容完全一模一樣，這樣前端不論用哪一個名字都能 100% 正常動工！
    site_search = search_query
    
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
  