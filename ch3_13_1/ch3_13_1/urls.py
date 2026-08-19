from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name='test'),  # 👈 修正：在 'test' 後方加上斜線 '/'
]
