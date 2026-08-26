from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict

# Create your views here.
def homework4(request):
    return HttpResponse("Hello, this is homework4!")

def view_history_temperature(request):
    # 取得所有的溫度紀錄
    temperature_records = TemperatureRecord.objects.all()

    # 將每個紀錄轉換為字典
    records_list = [model_to_dict(record) for record in temperature_records]

    # 將紀錄傳遞給模板
    return render(request, 'view_history_temperature.html', {'records': records_list})
