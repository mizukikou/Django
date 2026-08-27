from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import TemperatureRecord  # 1. 修改為您的 Model 名稱

def homework4(request):
    return HttpResponse("Hello, this is homework4!")

def view_history_temperature(request):
    # 2. 這裡的主鍵是 id，所以要改成依 '-id' 降冪排序
    temperature_records = TemperatureRecord.objects.all().order_by('-myid')
    return render(request, 'view_history_temperature.html', {'records': temperature_records})
