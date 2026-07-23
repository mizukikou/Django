print("__________________1________________________")
# 建立tuple
tuple_data = ('abcd', 786, 2.23, 'John', 70.2, 786)
print(tuple_data)
#取得元素
print(tuple_data[0])
print(tuple_data[2])
print(tuple_data[1:3])
print(tuple_data[2:])

# tuple_data[2] = 'new number'  #Typeerror
# 常數
for element in tuple_data:
  print(element, end="\t")