from django.db import models


class Students(models.Model):
    # 💡 自增值主鍵（Primary Key）：在 MySQL 資料庫中會自動遞增數值（1, 2, 3...）
    cid = models.AutoField(primary_key=True)
    
    # 💡 字串欄位（CharField）： blank=False 代表在後台或表單中此欄位為必填項目
    cname = models.CharField(max_length=20, blank=False)
    
    # 💡 性別欄位：預設值（default）設定為 'F' (代表女生)
    csex =  models.CharField(max_length=1, blank=False, default='F')
    
    # 【參數知識補充】：
    # 1. auto_now_add=True：只有在「第一次建立資料」時會自動填入目前時間，未來修改資料時，這個時間永遠不會改變（適合用在：建立時間 create_at）。
    # 2. auto_now=True：每次只要這筆資料有被修改並「重新儲存(save)」，欄位就會自動更新為當下的最新時間（適合用在：最後修改時間 update_at）。
    
    # 💡 日期欄位：null=True 代表資料庫允許為空值（NULL），blank=True 代表前端表單填寫時可以留白
    cbirthday = models.DateField(null=True, blank=True)
    
    # 💡 電子信箱欄位：限制最大長度為 100 個字元
    cemail = models.CharField(max_length=100, blank=False)
    
    # 💡 電話號碼欄位：限制最大長度為 50 個字元
    cphone = models.CharField(max_length=50, blank=False)
    
    # 💡 地址欄位：限制最大長度為 255 個字元
    caddr = models.CharField(max_length=255, blank=False)

    # 💡 物件字串表達方法：定義當我們在終端機 print(student_object) 或在 Django 後台查看時，該物件要顯示成什麼格式
    def __str__(self):
        # 修正：將原先大寫的 self.cName 修改為你實際宣告的小寫 self.cname
        return f"{self.cname} ({self.cid})"
