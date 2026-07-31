#list內有多個dictionary,如何找出特定的key value
items = [{"name":"John","score":6734,"dept":"sales"},
         {"name":"Mary","score":1234,"dept":"HR"},
         {"name":"Peter","score":5678,"dept":"IT"}]
print(items)
print(items[1]["name"]) #Mary
print(items[1]["score"]) #1234
print(items[1]["dept"]) #HR
print(f'{items[1]["name"]} {items[1]["score"]} {items[1]["dept"]}')
for data in items:
    print(data)
    print(f'姓名：{data["name"]}, 分數：{data["score"]}, 部門：{data["dept"]}')
    
print(*range(1, 5))


