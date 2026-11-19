class Emp:
  def __init__(self):
      self.Salary = 0
  def set_salary(self, Salary):
      if(Salary > 40000):
          self.Salary = 40000
      else:
          self.Salary = Salary
  def ShowSalary(self):
		  print(str(self.Salary))
          
class Manager(Emp):
  def __init__(self):
      super().__init__()
      self.bonus = 0
  def set_salary(self, Salary):
      if(Salary > 60000):
          self.Salary = 60000
      else:
          self.Salary = Salary
          
  def ShowSalary(self):
      print(f"Salary: {self.Salary+self.bonus}")
      
Jonn = Emp()
Jonn.set_salary(50000) # Output: Salary: 40000
Jonn.ShowSalary()  # Output: Salary: 40000

Jonn.Salary = 100
Jonn.ShowSalary()  # Output: Salary: 100

Mike = Manager()
Mike.bonus = 15000
Mike.set_salary(90000)
Mike.ShowSalary()  # Output: Salary:105000

      