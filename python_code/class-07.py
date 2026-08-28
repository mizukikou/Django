class Animal:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying!")


class Bird(Animal):
    # Bird 繼承 Animal，因此可以直接使用 Animal 的屬性和方法。
    def __init__(self, name, color):
        # super() 呼叫父類別的初始化方法，設定共用的 name 屬性。
        super().__init__(name)
        self.color = color

    def fly(self):
        # 覆寫父類別的 fly()，在飛行訊息中加入鳥的顏色。
        print(f"{self.color} {self.name} is flying!")

    def sing(self):
        print(f"{self.color} {self.name} is singing!")


class Eagle(Animal):
    # Eagle 沒有重新定義 fly()，所以會直接使用 Animal 的 fly()。
    pass


bird = Bird("Bird", "yellow")
eagle = Eagle("Eagle")

bird.fly()   # Bird 覆寫後的方法，會顯示顏色
bird.sing()  # Bird 自己新增的方法，也會使用顏色
eagle.fly()  # Eagle 繼承 Animal 的方法