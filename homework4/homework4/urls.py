"""
URL configuration for homework4 project.
"""

from django.contrib import admin
from django.urls import path
from myapp import views # 👈 確保引入了你的 views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # 💡 修正重點：網址叫 homework4/，後方對應的函數名稱也完美對齊 views.homework4
    path("homework4/", views.homework4, name="homework4"),
    path('view_history_temperature/', views.view_history_temperature)
]
