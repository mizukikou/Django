from django.db import models

class UserProfile(models.Model):
    """
    對應資料庫中 'myapp_userprofile' 資料表的 Django 模型 (Model)。
    欄位設定皆依據 MySQL Workbench 的資料型態與約束條件 (Constraint) 進行對應。
    """
    
    # id 欄位：對應 BIGINT。
    # primary_key=True 代表設定為主鍵 (PK)，內建會自動遞增 (AI)。
    id = models.BigAutoField(primary_key=True)
    
    # username 欄位：對應 VARCHAR(100)。
    # 圖片中勾選了 NN (Not Null)，故不加 null=True，代表此欄位為必填。
    username = models.CharField(max_length=100)
    
    # usersex 欄位：對應 VARCHAR(10)。
    # 圖片中勾選了 NN (Not Null)，代表此欄位為必填。
    usersex = models.CharField(max_length=10)
    
    # userschool 欄位：對應 VARCHAR(20)。
    # 圖片中勾選了 NN (Not Null)，代表此欄位為必填。
    userschool = models.CharField(max_length=20)
    
    # userinterest 欄位：依需求使用 LONGTEXT (TextField) 類型。
    # 圖片中未勾選 NN，表示允許空值；故設定 null=True (資料庫允許 NULL) 與 blank=True (表單允許留白)。
    userinterest = models.TextField(null=True, blank=True)
    
    # userthought 欄位：依需求使用 LONGTEXT (TextField) 類型。
    # 圖片中未勾選 NN，預設值為 NULL；故設定 null=True 與 blank=True。
    userthought = models.TextField(null=True, blank=True)

    class Meta:
        # 預設 Django 會自動將資料表命名為 '應用程式名稱_userprofile'。
        # 為了精準對應圖片中的 Table Name，在此明確指定資料表名稱為 'myapp_userprofile'。
        db_table = 'myapp_userprofile'

    def __str__(self):
        """
        定義物件的字串表達形式。
        當在 Django Admin 後台、終端機 (Shell) 或印出物件時，會直接顯示該使用者的姓名，便於閱讀與管理。
        """
        return self.username
