# object-oriented programming (OOP) 物件導向程式設計
# Class：紅豆模板、設計圖、無實體。
# object：紅豆湯、房子、實體可使用。

class Car:
    # 建構子：當車子被造出來時，必須傳入顏色和品牌
    def __init__(self, color, brand):
        self.color = color  # self.color 代表這台車自己的顏色
        self.brand = brand  # self.brand 代表這台車自己的品牌
    def drive(self):
        print(f"這台{self.color}的 {self.brand} 汽車開動了！")
# 🚗 真正創造實體物件（呼叫類別）
car1 = Car("紅色", "Toyota")  # 這時候 Python 會自動觸發 __init__
car2 = Car("黑色", "BMW")
# 呼叫物件的方法
car1.drive()  # 輸出：這台紅色的 Toyota 汽車開動了！
car2.drive()  # 輸出：這台黑色的 BMW 汽車開動了！

#是否要寫 __init__(self)，完全取決於您的類別需不需要在誕生的那一刻接收外部資料或執行特定初始化設定。

# Class 範例 定義一個類別MyClass；包含屬性(變數：int,char,list,str...)和方法(函式)
class DemoClass:
    # 屬性(變數)
    name = "小明"
    age = 18
    score = 92.5
    # 方法(函式)
    def say_hello(self):
        print(f"Hello, {self.name}，你今年 {self.age} 歲，成績是 {self.score} 分。")

# 創建 DemoClass 的實體物件
my_object = DemoClass()
# 呼叫物件的方法
my_object.say_hello()  # 輸出：Hello, 小明，你今年 18 歲，成績是 92.5 分。

class MyClass:
    def __init__(self):
      self.text = 'ABC'
    def clear(self):
      self.text = ''
  
obj1 = MyClass()
print(f"obj1.text: {obj1.text}")  # 輸出：obj1.text: ABC
obj1.text = 'XYZ'  # 修改 obj1 的 text 屬性
print(f"obj1.text: {obj1.text}")  # 輸出：obj1.text: XYZ
obj1.clear()  # 呼叫 clear 方法，將 obj1 的 text 屬性清空
print(f"obj1.text: {obj1.text}")  # 輸出：