from django.http import JsonResponse # 👈 記得在檔案最上方引入 JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from myapp.models import Student, Scorelist

def test(request):
    # datas = Student.objects.all() # 取得所有學生資料
    # data_list = []                 # 建立一個空清單來存放所有字典
    # for data in datas:
    # 將單筆學生資料轉成字典，並加入清單中
    # model_to_dict：Django 內建的工具函數，會把 data 裡面的欄位與數值自動剝離出來，打包成標準的 Python 字典。
    #     data_list.append(model_to_dict(data))
    # 注意：return 必須縮排在 for 迴圈外面！將整個清單傳給前端範本
    # return render(request, 'test.html', {'data': data_list})
  
     # datas = Student.objects.all()  # 取得所有學生資料
     # for data in datas:
     #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    ##########################
    # mysql:select cID, cName, cMail from myapp_student;
    # datas = Student.objects.values('cID', 'cName','cMail')  # 取得所有學生資料，並只取出指定欄位
    # for data in datas:
    #     print(data)  # 將每筆資料印在終端機上
    ###########################
    # .distinct() ➡️ 告訴資料庫：「重複的直接消去，我只要唯一值」
    # mysql:select DISTINCT cSEX FROM myapp_student;
    # datas = Student.objects.values('cSEX').distinct()  # 取得所有學生資料，並只取出指定欄位
    # for data in datas:
    #     print(data)  # 將每筆資料印在終端機上
    ###############################
    # mysql:select * from myapp_student where cID=3;
    # 使用 .get() 時，條件是須百分之百精準地在資料庫裡「只對應到一筆資料」，只要多一個或少一個，程式就會直接死機：
    # data = Student.objects.get(cID=3)  # 取得 cID=3 的學生資料
    # print(model_to_dict(data))  # 將資料轉成字典並印在終端機上
    ################################
    # mysql:select * from myapp_student where cSex='M';
    # datas = Student.objects.filter(cSex='M')  # 取得所有性別為 M 的學生資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    ###############################
    from django.db.models import Q
    # mysql:select * from myapp_student where cID>5 and cSex='M';
    # datas = Student.objects.filter(cID__gt=5, cSex='M')  # 取得所有 cID 大於 5 且性別為 M 的學生資料
    # 逗號在 filter() 裡只能當 AND 使用。如果您想查「學號大於 5 或者 性別是男性」（只要滿足一項就撈出來），必須使用 Q 物件搭配 |
    # datas = Student.objects.filter(Q(cID__gt=5) & Q(cSex='M'))  # 取得符合條件的資料
    # mysql:select * from myapp_student where cID=1 or cID>=9;
    # datas = Student.objects.filter(Q(cID=1) | Q(cID__gte=9))  # 取得符合條件的資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    ####################################################
    # mysql:select * from myapp_student where cID between 4 and 6;
    # datas = Student.objects.filter(cID__range=[4,6])  # 取得 cID 在 4 到 6 之間的學生資料
    # mysql:select * from myapp_student where cID>=4 and cID<=6;
    # datas = Student.objects.filter(cID__gte=4,cID__lte=6)  # 取得 cID 大於等於 4 且小於等於 6 的學生資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    # return HttpResponse("終端機已成功印出 cID 在 4 到 6 之間的學生資料！")
    #################################################
    # mysql:select * from myapp_student where cID in (1,3,5);
    # datas = Student.objects.filter(cID__in=[1,3,5])  # 取得 cID 在 1、3、5 的學生資料
    # for data in datas:
    #     print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    # return HttpResponse("終端機已成功印出 cID 在 1、3、5 的學生資料！")
    ###############################################
    # mysql:select * from myapp_student where cPhone like '0918%';
    # datas = Student.objects.filter(cPhone__istartswith='0918')
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
    # return HttpResponse("終端機已成功印出手機號碼以 0918 開頭的學生資料！")
    ##############################################        
    # mysql:select * from myapp_student where cAddr like '%建國%';
    # datas = Student.objects.filter(cAddr__icontains='建國')  # 取得住址包含「建國」的學生資料
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    # return HttpResponse("終端機已成功印出住址包含「建國」的學生資料！")
    ###############################################   
    # mysql:select * from myapp_student order by cBirthday desc;
    # datas = Student.objects.all().order_by('-cBirthday')  # 依出生日期排序 "-" 表示由大到小排序，"+" 表示由小到大排序
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    # return HttpResponse("終端機已成功印出依出生日期排序的學生資料！")
    # ###############################################   
    # mysql:select * from myapp_student order by cSex asc, cBirthday desc;
    # datas = Student.objects.all().order_by('cSex', '-cBirthday')  # 依性別排序，性別相同再依出生日期排序 "-" 表示由大到小排序，"+" 表示由小到大排序
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    # return HttpResponse("終端機已成功印出依性別及出生日期排序的學生資料！")
    ###############################################   
    # mysql:select * from myapp_student limit 2;
    #datas = Student.objects.all()[0:2]  # 取得前兩筆學生資料.顯示索引
    # mysql:select * from myapp_student limit 4,2;
    # datas = Student.objects.all()[4:6]  # 取得第 5 到第 6 筆學生資料.顯示切片
    # for data in datas:
    #         print(model_to_dict(data))  # 將每筆資料轉成字典並印在終端機上
            
    # return HttpResponse("終端機已成功印出第 5 到第 6 筆學生資料！")
    from django.db.models import Avg, Max, Sum, Count, Min
    # mysql:select avg(score), max(score), min(score), sum(score), count(score) from myapp_scorelist;
    # datas = Scorelist.objects.aggregate(Avg('score'), Max('score'), Min('score'), Sum('score'), Count('score'))  # 計算成績的平均值、最大值、最小值、總和、筆數
    # print(datas)  # 將計算結果印在終端機上
    
    # mysql:select avg(score), max(score), min(score), sum(score), count(score) from myapp_scorelist where course='國文';
    # datas = Scorelist.objects.filter(course='國文').aggregate(Avg('score'), Max('score'), Min('score'), Sum('score'), Count('score'))  # 計算國文成績的平均值、最大值、最小值、總和、筆數
    # print(datas)  # 將計算結果印在終端機上
    # return HttpResponse("終端機已成功印出國文成績的平均值、最大值、最小值、總和、筆數！")
    
    # mysql:select cID, count(cID) from myapp_student group by cID;
    # datas = Student.objects.aggregate(Count('cID'))  # 計算 cID 的筆數
    # print(datas)  # 將計算結果印在終端機上
    # return HttpResponse("終端機已成功印出 cID 的筆數！")
    
    # mysql:select cID, sum(score) from myapp_scorelist group by cID;
    #   datas = Scorelist.objects.values_list('cID').annotate(Sum('score'))
    #  # 計算每個學生的成績總和
    #   for data in datas:
    #       print(data)  # 將每筆資料印在終端機上
    #   return HttpResponse("終端機已成功印出每個學生的成績總和！")
    
    # mysql:select cID, sum(score) from myapp_scorelist where cID<=5 group by cID;
    #   datas = Scorelist.objects.filter(cID__lte=5).values_list('cID').annotate(Sum('score'))  # 計算 cID 小於等於 5 的學生的成績總和
    #   for data in datas:
    #       print(data)  # 將每筆資料印在終端機上
    #  # 💡 將 QuerySet 轉換成 Python 的 list，並用 JsonResponse 回傳
    #   # safe=False 是因為回傳的是 list（陣列）而不是 dict（字典）
    #   return JsonResponse(list(datas), safe=False, json_dumps_params={'ensure_ascii': False})
    
    # INSERT INTO myapp_student (cName, cSex, cBirthday, cEmail, cPhone, cAddr, cHeight, cWeight)
    # SELECT 'Bill3', 'M', '2000-01-01', 'bill3@example.com', '1234567890', '123 Main St', 180, 75
    # FROM DUAL
    # WHERE NOT EXISTS (
    #     SELECT 1 FROM myapp_student WHERE cName = 'Bill3'
    # );
    # students_exists = Student.objects.filter(cName='Bill3').exists()  # 檢查名為 'Bill1' 的學生是否存在
    # if not students_exists:
    #     add = Student(cName='Bill3', cSex='M', cBirthday='2000-01-01', cEmail='bill3@example.com', cPhone='1234567890', cAddr='123 Main St', cHeight=180, cWeight=75)
    #     add.save()  # 將新學生資料存入資料庫
    #     return HttpResponse("學生 'Bill3' 不存在，已新增！")
    # else:
    #     return HttpResponse("學生 'Bill3' 已存在！")
          
    # 第二種方式 使用 create() 方法直接新增資料
    # students_exists = Student.objects.filter(cName='Bill4').exists()  # 檢查名為 'Bill1' 的學生是否存在
    # if not students_exists:
    #     Student.objects.create(cName='Bill4', cSex='M', cBirthday='2000-01-01', cEmail='bill4@example.com', cPhone='1234567890', cAddr='123 Main St', cHeight=180, cWeight=75)
    #     return HttpResponse("學生 'Bill4' 不存在，已新增！")
    # else:
    #     return HttpResponse("學生 'Bill4' 已存在！")
    
    # 範例 update  myapp_student set  cheight=188, cWeight=88 WHERE cID=11;
    # try:
    #     student = Student.objects.get(cID=11)  # 嘗試取得 cID=11 的學生資料
    #     student.cHeight = 188  # 更新身高
    #     student.cWeight = 88   # 更新體重
    #     student.save()         # 儲存更新後的資料
    #     return HttpResponse("學生 cID=11 的身高與體重已成功更新！")
    # except Student.DoesNotExist:
    #     return HttpResponse("學生不存在，無法更新！")
    
    # 更新多筆資料的範例
    # mysql:UPDATE myapp_student SET cPhone='1234567890', cWeight=65, cAddr='123 Main St' WHERE cID>=11;
    # update_count = Student.objects.filter(cID__gte=11).update(cPhone='1234567890', cWeight=65, cAddr='123 Main St')  # 將 cID 大於等於 11 的學生的電話更新為 '1234567890'，體重更新為 65
    # return HttpResponse(f"已更新 {update_count} 筆學生資料！")
    
    # 刪除資料的範例
    # mysql:DELETE FROM myapp_student WHERE cID=12;
    Student_exists = Student.objects.filter(cID=12).exists()  # 檢查 cID=12 的學生是否存在
    if not Student_exists:
        return HttpResponse("學生 cID=12 不存在，無法刪除！")
    else:
        Student.objects.filter(cID=12).delete()  # 刪除 cID=12 的學生資料
        return HttpResponse("學生 cID=12 已成功刪除！")
    
