class TaipeiBank:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def print_balance(self):
    print(f"{self.name} has a balance of {self.balance}")
    
t = TaipeiBank("John Doe", 1000) #實體化時必須要指定值，否則 Python 在執行時會直接報錯並中斷。
t.print_balance()