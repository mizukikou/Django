# for in
# string
print("........1........")
for letter in "python":
    print(f"current letter:{letter}")

#list
print("........2........")
fruits = ["banana","apple","mango"]
for f in fruits:
    print(f"current fruit:{f}")

#dictionary
print("........3........")
dict_data = {"banana":20,"apple":50,"mango":30}
#取key，透過key，再產生value
for name in dict_data:
    print(f"{name}數量為{dict_data[name]}")

#利用items()，取得key and value
for name, num in dict_data.items():
    print(f"{name}數量為{num}")

########################################
print("........4........")
# list內有多個dictionary
items = [{"name":"bill","score":30},
         {"name":"mary","score":60},
         {"name":"harry","score":80}
        ]
print(items)
print("........5........")
for data in items:
    # print(data)
    print(f"姓名={data["name"]},分數={data["score"]}")

