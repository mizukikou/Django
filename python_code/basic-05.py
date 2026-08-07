print("__________________1________________________")
list_data = ['abcd', 786, 2.23, 'John', 70.2, 786]
print(list_data)
#取得元素
print(list_data[0])
print(list_data[2])
print(list_data[1:3])
print(list_data[2:])

#update
print("__________________2________________________")
list_data[2] = 'new number'
print(list_data)

#delete 
print("__________________3________________________")
print(list_data)
del list_data[2]
print(list_data)

#append
print("__________________4________________________")
print(list_data)
list_data.append('ccc')
print(list_data)

# 💡 使用 insert(索引值, 要插入的內容)
print("__________________5________________________")
print(list_data)
list_data.insert(2, 'xxx')
print(list_data)

#走訪
print("__________________6________________________")
for element in list_data:
  print(element, end="\t")

