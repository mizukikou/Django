from django.db import models

# 1. 學生模型 (一對多、一對一的主表)
class Student(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=20, blank=False)
    cSex = models.CharField(max_length=1, blank=False, default='F')
    cBirthday = models.DateField(null=True, blank=True)
    cEmail = models.CharField(max_length=100, blank=False)
    cPhone = models.CharField(max_length=50, blank=False)
    cAddr = models.CharField(max_length=255, blank=False)
    cHeight = models.IntegerField(blank=True, null=True) 
    cWeight = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'myapp_student'  # 👈 對應 Workbench 匯入有資料的單數資料表

# 2. 成績模型 (與 Student 為一對多關聯)
class Scorelist(models.Model):
    id = models.AutoField(primary_key=True)
    
    # 👈 關鍵修改：將外鍵 ForeignKey 改為一般的 IntegerField
    # 👈 變數名稱完美設定為 cID，db_column 設定為你的 MySQL 實體欄位 'cID_id'
    cID = models.IntegerField(null=True, db_column='cID_id') 
    
    course = models.CharField(max_length=20, blank=False)
    score = models.IntegerField(blank=False)
    
    class Meta:
        db_table = 'myapp_scorelist'


# 3. 權限密碼模型 (與 Student 為一對一關聯)
class Permissions(models.Model):
    id = models.AutoField(primary_key=True)
    # 将 db_column 改为 'cID_id'
    student = models.OneToOneField('Student', on_delete=models.CASCADE, null=True, db_column='cID_id')
    passwd = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=2, blank=False) # 0管理者 #1一般使用者

    class Meta:
        db_table = 'myapp_permissions'

# 4. 書籍模型 (與 Author 為多對多關聯)
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=32, blank=False)
    authors = models.ManyToManyField(to='Author')

    class Meta:
        db_table = 'myapp_book'

# 5. 作者模型
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    aID = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=32, blank=False)

    class Meta:
        db_table = 'myapp_author'
