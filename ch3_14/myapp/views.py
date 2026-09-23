from django.shortcuts import render, redirect
from django.http import HttpResponse  # 導入 HttpResponse，以便不透過 HTML 範本直接回傳網頁內容
from django.contrib import messages
import datetime                       # 導入日期時間模組，用來計算 Cookie 的過期時間

# Create your views here.

# ==============================================================================
# 案例一：基礎的 Cookie 寫入 (Create)
# ==============================================================================
def set_cookie(request, key, value):
    # 建立一個基礎的網頁回應物件
    response = HttpResponse("<h1>Response 成功！(不使用 HTML 檔案)</h1>")
    
    # 【核心操作】直接將網址傳進來的 key 和 value 寫入使用者的瀏覽器 Cookie
    # 因為沒有設定時間，此為工作階段 Cookie (關閉瀏覽器後即消失)
    response.set_cookie(key, value)   # 這邊的.set_cookie(...)是內建方法，會將 key 和 value 寫入瀏覽器 Cookie
    
    return response

# ==============================================================================
# 案例二：讀取特定的 Cookie (Read)
# ==============================================================================
def get_cookie(request, key):
    # 【核心操作】檢查 request.COOKIES 字典中，是否存在使用者指定的鍵 (key)
    if key in request.COOKIES:
        value = request.COOKIES[key] # 讀取該鍵對應的值
        return HttpResponse(f"<h1>Cookie 值: {value}</h1>")
    else:
        return HttpResponse("<h1>Cookie 不存在</h1>")
      
# ==============================================================================
# 案例三：列出所有的 Cookies (List All)
# ==============================================================================
def get_all_cookies(request):
    # 檢查目前瀏覽器中是否有任何 Cookie 資料
    if request.COOKIES != None:
        strcookies = ""
        # 迴圈歷遍 COOKIES 字典中的每一個鍵值對，並組合成 HTML 字串
        for key1, value1 in request.COOKIES.items():
            strcookies = strcookies + key1 + ":" + value1 + "<br>"
        return HttpResponse(f"<h1>所有 Cookie: <br>{strcookies}</h1>")
    else:
        return HttpResponse('Cookie 不存在!')	
      
# ==============================================================================
# 案例四：設定帶有存活時間的 Cookie ( max_age 參數 )
# ==============================================================================
def set_cookie2(request, key, value, max_age=None):
    response = HttpResponse("<h1>Response 成功！(不使用 HTML 檔案)</h1>")
    
    # 【核心操作】使用 max_age 參數指定 Cookie 的存活「秒數」
    # max_age=3600 代表這個 Cookie 在瀏覽器中只能活 3600 秒 (即 1 小時)
    response.set_cookie(key, value, max_age=3600)
    return response

# ==============================================================================
# 案例五：刪除指定的 Cookie (Delete)
# ==============================================================================
def delete_cookie(request, key):
  # 檢查該 Cookie 是否存在，存在才能刪除
  if key in request.COOKIES:
      response = HttpResponse("<h1>Cookie 已刪除</h1>" + key)
      
      # 【核心操作】通知瀏覽器立刻抹除這個 key 的 Cookie 資料
      response.delete_cookie(key)
      return response
  else:
      return HttpResponse("<h1>Cookie 不存在</h1>" + key)
    
# ==============================================================================
# 案例六：進階綜合應用 —— 每日造訪計數器 ( expires 參數應用 )
# ==============================================================================
def index(request):
    # 1. 【讀取與邏輯計算】檢查瀏覽器有沒有 counter 這個計數器 Cookie
    if "counter" in request.COOKIES:
        counter = int(request.COOKIES["counter"]) # 取出舊的次數並轉成整數
        counter += 1                              # 次數加 1
    else:
        counter = 1                               # 第一次造訪，次數設為 1
        
    # 2. 渲染前端 index.html 範本，並把計數器的值帶給網頁顯示
    response = render(request, "index.html", {"counter": counter})
    
    # 3. 【進階時間計算】設定 counter 變數的到期時間為「今天的午夜 24:00 (明天的 00:00:00)」
    # 步驟 A: 取得現在的日期時間，並加上 1 天 (代表明天)
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1) 
    
    # 步驟 B: 將明天的時、分、秒強制強制改為 0時 0分 0秒 (即明天的凌晨零點)
    tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0) 
    
    # 步驟 C: 將時間物件轉換為 HTTP 規範標準的格林威治時間 (GMT) 字串格式
    # 格式範例: "Wed, 23-Sep-2026 00:00:00 GMT"
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
    
    # 4. 【寫入與限制時間】將最新的計數值寫回 Cookie，並透過 expires 參數指定它在午夜失效
    #expires=： 是 Django set_cookie 函式數，用來接收一個「特定的格林威治時間（GMT）字串」。
    response.set_cookie("counter", counter, expires=expires) 
    
    #max_age 使用的是「相對時間（秒數）」，而 expires 使用的是「絕對時間（特定日期時間點）」
    
    return response

# ============================
# Create your views here.
# ==============================================================================
# 案例一：基礎的 Session 寫入 (Create)
# ==============================================================================
def set_session(request, key=None, value=None):
    # 【核心操作】直接將資料存入伺服器端的 Session 中
    # Django 會在資料庫中存下這筆資料，並只把一個隨機加密的 session_id 透過 Cookie 發給瀏覽器
    request.session[key] = value
    return HttpResponse('Session 儲存完畢!')
    
# ==============================================================================
# 案例二：讀取特定的 Session (Read)
# ==============================================================================
def get_session(request, key=None):
    # 【核心操作】檢查伺服器的 Session 字典中，是否存在使用者指定的鍵 (key)
    if key in request.session:
        # 取出該鍵對應的值並回傳
        return HttpResponse(f"{key}:{request.session[key]}")
    else:
        return HttpResponse('Session 不存在!')

# ==============================================================================
# 案例三：列出所有的 Sessions (List All)
# ==============================================================================
def get_allsessions(request):
    # 檢查目前使用者的 Session 裡面有沒有任何鍵值對 (.items() 是否有資料)
    if request.session.items() != None:
        strsessions = ""
        # 迴圈歷遍所有 Session 資料並組合成 HTML 字串
        for key1, value1 in request.session.items():
            strsessions += f"'{key1}':'{value1}'<br>"
        return HttpResponse(f"All Sessions:<br>{strsessions}")
    else:
        return HttpResponse('Session 不存在!')	

# ==============================================================================
# 案例四：實務應用 —— 防止重複投票 (檢驗狀態)
# ==============================================================================
def vote(request):
    # 【核心操作】檢查 Session 中有沒有 "vote" 這個標記
    if not "vote" in request.session:
        # 如果沒有，代表他是第一次來，幫他蓋上「已投票」的印章 (設為 True)
        request.session["vote"] = True
        msg = "您第一次投票!"		
    else:		
        # 如果有，代表伺服器記得他投過了，直接拒絕重複投票
        msg = "您已投過票!"	

    return HttpResponse(msg)	

# ==============================================================================
# 案例五：設定帶有存活時間的 Session ( set_expiry 參數 )
# ==============================================================================
def set_session2(request, key=None, value=None):
    # 嚴謹度檢查：判斷 key 是否為空值
    if key is None:
        return HttpResponse("Key 不可為空")

    # 將資料存入 Session
    request.session[key] = value

    # 【核心操作】使用 set_expiry() 設定整個 Session 的過期秒數
    # 傳入 10 代表 10 秒後，伺服器上的這筆 Session 紀錄與瀏覽器的 Session Cookie 會同步失效
    request.session.set_expiry(10)

    return HttpResponse("Session 儲存完畢!")

# ==============================================================================
# 案例六：清除指定的 Session 資料 (Delete)
# ==============================================================================
def delete_session(request, key=None):
    # 檢查該 Session 鍵是否存在
    if key in request.session:
        response = HttpResponse('Delete Session: ' + key)	
        
        # 【核心操作】使用 Python 的 del 關鍵字，將該條 Session 資料從字典與資料庫中抹除
        del request.session[key]
        return response
    else:
        return HttpResponse('No Session:' + key)

# ==============================================================================
# 案例七：使用者登入 (Login)
# ==============================================================================
def login(request):
    if request.session.get('user'):
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == '12345':
            # 假設使用者成功登入，將使用者資訊存入 Session
            request.session['user'] = 'example_user'
            messages.success(request, '登入成功!')
            messages.info(request, '歡迎回來!')
            # 登入成功後導向 dashboard，避免重新整頁時重複提交表單
            return redirect('dashboard')
        else:
            messages.error(request, '帳號或密碼錯誤!')
            status = 'error'
            return render(request, 'login.html', locals())
    else:
        messages.info(request, '請使用 POST 方法登入!')
        status = 'info'
        return render(request, 'login.html',locals())

# ==============================================================================
# 案例七之一：登入後的主頁 (Dashboard)
# ==============================================================================
def dashboard(request):
    if not request.session.get('user'):
        messages.error(request, '請先登入!')
        return redirect('login')
    return render(request, 'dashboard.html', {'user': request.session.get('user')})

# ==============================================================================
# 案例八：使用者登出 (Logout)
# ==============================================================================
def logout(request):
    # 清除使用者的 Session 資料
    if 'user' in request.session:
        del request.session['user']
    messages.info(request, '使用者已登出!')
    return redirect('login')
