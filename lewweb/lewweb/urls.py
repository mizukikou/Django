"""
URL configuration for lewweb project.
"""
from django.contrib import admin
from django.urls import path, include

# 💡 引入 Django 核心設定與靜態檔案路由工具
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # 連結至您 myapp 內部的 urls.py
]

# 🛠️ 【強效防錯】在開發環境（DEBUG = True）下，強制讓 Django 伺服器幫我們把 static 資料夾掛載到網址列
if settings.DEBUG:
    # 這裡會動態將 settings.py 裡的 STATIC_URL 與 STATICFILES_DIRS 綁定進路由中
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
