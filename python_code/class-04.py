class SmallMath:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"
          
s = SmallMath(10, 5)
print(s.add())        # Output: 15
print(s.subtract())   # Output: 5
print(s.multiply())   # Output: 50
print(s.divide())     # Output: 2.0
