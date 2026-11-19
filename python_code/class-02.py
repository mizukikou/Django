class A():
    # 🌟 這裡叫「在函式外面、類別裡面」
    # 它不屬於任何 def 區塊。這裡定義的變數 x 叫做「類別變數」。
    # 或「靜態變數（Static Variable）」。它是屬於「類別本身」的，而不是屬於「物件」，
    # 所有的實例（物件）共同分享同一個記憶體空間
    x = [] 

    # 🌟 這裡用 def 宣告的才叫做「函式（方法）」
    def __init__(self):
        # 這裡叫「在函式裡面」，# 💡 這樣寫，每次 new 出新物件時，Python 都會開闢一塊全新的獨立列表
        self.y = [] # 這裡定義的 y 叫做「實例變數（各管各的）」

# 🌟 這裡叫「實例化（物件建立）」
# a1、a2 是「物件」，不是函式！
a1 = A() 
a2 = A() 
a1.x.append(1)
a2.x.append(2)
print(a1.x)  # Output: [1, 2]
print(a2.x)  # Output: [1, 2]

a1.y.append(1)
a2.y.append(2)
print(a1.y)  # Output: [1]
print(a2.y)  # Output: [2]

