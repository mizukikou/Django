from django.db import models

# Create your models here.
class Students(models.Model):
    cID = models.AutoField(primary_key=True) 
    cName = models.CharField(max_length=20,blank=False) #blank=False表示欄位是不能為空(必填)
    cSex = models.CharField(max_length=1, blank=False, default='F')
    cBirthday = models.DateField(blank=False) 
    #cCreated = models.DateField(auto_now_add=True) #設定加入當下的生成時間
    #cUpdated = models.DateField(auto_now=True) #設定自動更新生成時間
    cMail = models.EmailField(max_length=100, blank=False)
    cPhone = models.CharField(max_length=50, blank=False)
    cAddr = models.CharField(max_length=255, blank=False)
    cHeight = models.IntegerField(blank=True)
    cWeight = models.IntegerField(blank=True)