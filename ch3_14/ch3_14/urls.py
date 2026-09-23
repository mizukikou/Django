# -------------------------------------------------------------
# 模組導入 (Imports)
# -------------------------------------------------------------
# 導入 Django 內建的後台管理系統模組
from django.contrib import admin
# 導入 用於定義網址路徑的 path 函式
from django.urls import path
# 導入 您自己編寫的應用程式 (myapp) 中的檢視邏輯 (views.py)
from myapp import views

# -------------------------------------------------------------
# 網址路由配置 (URL Patterns)
# -------------------------------------------------------------
# 這裡定義了網站的「網址地圖」，當使用者在瀏覽器輸入特定網址時，
# Django 就會依照這個列表，將請求分派給 views.py 中對應的函式處理。
urlpatterns = [
    # 1. 預設的 Django 後台管理系統網址 (通常透過 http://IP:Port/admin/ 進入)
    path('admin/', admin.site.urls),

    # 2. 【寫入 Cookie (方法一)】
    # 動態接收網址中的 key 和 value 參數，並呼叫 views.set_cookie 寫入瀏覽器。
    # 例如輸入: /set_cookie/name/bill/ -> 會在瀏覽器存入 name = bill
    path('set_cookie/<str:key>/<str:value>/', views.set_cookie, name='set_cookie'), 

    # 3. 【讀取單一 Cookie】
    # 動態接收網址中的 key 參數，去瀏覽器搜尋對應的值並顯示在網頁上。
    # 例如輸入: /get_cookie/name/ -> 網頁會顯示該 Cookie 的值
    path('get_cookie/<str:key>/', views.get_cookie, name='get_cookie'),

    # 4. 【讀取全部 Cookies】
    # 靜態網址。不需要傳入參數，直接把目前瀏覽器中儲存的所有 Cookies 一併列出來。
    path('get_all_cookies/', views.get_all_cookies, name='get_all_cookies'),

    # 5. 【寫入 Cookie (方法二)】
    # 教學對照組。通常用來展示不同的 Cookie 設定參數（例如：加上過期時間 max_age 或安全屬性 httponly）。
    path('set_cookie2/<str:key>/<str:value>/', views.set_cookie2, name='set_cookie2'),

    # 6. 【刪除指定 Cookie】
    # 動態接收網址中的 key 參數，通知瀏覽器將該名稱的 Cookie 抹除。
    # 例如輸入: /delete_cookie/name/ -> 瀏覽器中的 name 欄位就會被刪除
    path('delete_cookie/<str:key>/', views.delete_cookie, name='delete_cookie'),
    
    path('index/', views.index, name='index'),
    path('set_session/<str:key>/<str:value>/', views.set_session, name='set_session'),
    path('get_session/<str:key>/', views.get_session, name='get_session'),
    path('delete_session/<str:key>/', views.delete_session, name='delete_session'),
    path('vote/', views.vote, name='vote'),
    path('set_session2/<str:key>/<str:value>/', views.set_session2, name='set_session2'),
    path('get_allsessions/', views.get_allsessions, name='get_allsessions'),
    
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),

]
