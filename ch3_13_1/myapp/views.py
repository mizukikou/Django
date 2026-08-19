from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from myapp.models import Student

def test(request):
    # datas = Student.objects.all() # 取得所有學生資料
    # data_list = []                 # 建立一個空清單來存放所有字典
    # for data in datas:
        # 將單筆學生資料轉成字典，並加入清單中
    #     data_list.append(model_to_dict(data))
    # 注意：return 必須縮排在 for 迴圈外面！將整個清單傳給前端範本
    # return render(request, 'test.html', {'data': data_list})
  
     # datas = Student.objects.all()  # 取得所有學生資料
     # for data in datas:
     #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    ##########################
    # datas = Student.objects.values('cID', 'cName','cMail')  # 取得所有學生資料，並只取出指定欄位
    # for data in datas:
    #     print(data)  # 將每筆資料印在終端機上
    ###########################
    # datas = Student.objects.values('cSEX').distinct()  # 取得所有學生資料，並只取出指定欄位
    # for data in datas:
    #     print(data)  # 將每筆資料印在終端機上
    ###############################
    # data = Student.objects.get(cID=3)  # 取得 cID=3 的學生資料
    # print(model_to_dict(data))  # 將資料轉成字典並印在終端機上
    ################################
    # datas = Student.objects.filter(cSex='M')  # 取得所有性別為 M 的學生資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    ###############################
    from django.db.models import Q
    # datas = Student.objects.filter(Q(cID__gt=5) & Q(cSex='M'))  # 取得符合條件的資料
    #逗號在 filter() 裡只能當 AND 使用。如果您想查「學號大於 5 或者 性別是男性」（只要滿足一項就撈出來），必須使用 Q 物件搭配 |
    # datas = Student.objects.filter(Q(cID=1) | Q(cID__gte=9))  # 取得所有性別為 M 或 F 的學生資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    ####################################################
    #datas = Student.objects.filter(cID__range=[4,6])  # 取得 cID 在 4 到 6 之間的學生資料
    # datas = Student.objects.filter(cID__gte=4,cID__lte=6)  # 取得 cID 大於等於 4 且小於等於 6 的學生資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    # return HttpResponse("終端機已成功印出 cID 在 4 到 6 之間的學生資料！")
    #################################################
    # datas = Student.objects.filter(cID__in=[1,3,5])  # 取得 cID 在 1、3、5 的學生資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    # return HttpResponse("終端機已成功印出 cID 在 1、3、5 的學生資料！")
    ###############################################
    # datas = Student.objects.filter(cPhone__istartswith='0918')
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    # return HttpResponse("終端機已成功印出手機號碼以 0918 開頭的學生資料！")
    ##############################################        
    # datas = Student.objects.filter(cAddr__icontains='建國')  # 取得住址包含「建國」的學生資料
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    # return HttpResponse("終端機已成功印出住址包含「建國」的學生資料！")
    ###############################################   
    # datas = Student.objects.all().order_by('-cBirthday')  # 依出生日期排序學生資料 "-" 表示由大到小排序，"+" 表示由小到大排序
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    # return HttpResponse("終端機已成功印出依出生日期排序的學生資料！")
    # ###############################################   
    # datas = Student.objects.all().order_by('cSex', '-cBirthday')  # 依性別排序，性別相同再依出生日期排序 "-" 表示由大到小排序，"+" 表示由小到大排序
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    # return HttpResponse("終端機已成功印出依性別及出生日期排序的學生資料！")
    ###############################################   
    #datas = Student.objects.all()[0:2]  # 取得前兩筆學生資料.顯示索引
    datas = Student.objects.all()[4:6]  # 取得第 5 到第 6 筆學生資料.顯示切片
    for data in datas:
            print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    return HttpResponse("終端機已成功印出第 5 到第 6 筆學生資料！")
# Create your views here.
