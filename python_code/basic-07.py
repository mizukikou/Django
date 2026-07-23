print('___________ 建立__________')
dict_data = {"name":'John',"code":6734,'dept':"sales"}
#無順序性,它不認得「第 0 個位置」是什麼。您不能寫 dict_data[0]（這會報錯 KeyError）。您必須透過指定的「鍵（Key）」來查值
print(dict_data)

print('___________ 再新增__________')
dict_data['one'] = "This is new one"
print(dict_data)

dict_data2 = {}
dict_data2['one']='one'
dict_data2[1]='two'
print(dict_data2)

print('___________ 修改__________')
print(dict_data)
dict_data["code"] = 8888
print(dict_data)

print('___________ 取值_____________')
print(dict_data['code'],end="\t")
print(dict_data['dept'],end="\t")
print(dict_data['name'],end="\t")

print('___________刪除_____________')
print(dict_data)
del dict_data['dept']
print(dict_data)

print('___________走訪_____________')
for key in dict_data:
    print(key,dict_data[key])
    print(f"{key}=>{dict_data[key]}")
print('___________________________')
#利用items()取得 key & value
for k,v in dict_data.items():
#利用k()取得 key
    print(k)
#利用v()取得 value
    print(v)
    print(f"{k}=>{v}")
    
print('___________________________')
# print(dict_data['sample]) # 抛出 KeyError: 'sample'
#方法一 : try excpet
try:
    print(dict_data['sample'])
except KeyError:
    print("找不到 sample 這個 key！") # 👈 這裡必須縮排（按 Tab 鍵），不能留空
#方法二 ：透過get()方法
print(dict_data.get('code'))
print(dict_data.get('dept'))
print(dict_data.get('name'))
print(dict_data.get('sample')) # 如果找不到，則回傳 None
print(dict_data.get('sample', 'default')) # 如果找不到，則回傳 default


    
print('___________________________')    
key = "name"
print(f"嗨，{key}")  
# 輸出：嗨，name
print("嗨，{key}")  
# 輸出：嗨，{key}  (大括號完全失去功能，被當成一般文字印出)
