import math

print("........1........")
name = "王大明"
print("Hello, " + name + "!")
score = 80 #int
score2 = 80.0 #float
print(type(name)) 
print(type(score))
print(type(score2))

print(name+"的成績為"+str(score))

print("........2.......")
print(name,score)
print(name,score,sep="&",end="***")
print("Hello")
print(name,score,sep="-",end="\n")
print("Hello")

print("........3.......")
# 參數格式化
# %s=>str
# %d=>int
# %f=>float
# %c=>char
print("%s的成績為%d" % (name, score))
print("PI=%10.3f" % (math.pi)) #總長度10,小數為3 [.]也算一個
print("PI=%6.0f" % (math.pi))

print("........4.......")
# 參數格式化: format
print("{}的成績為{}" .format(name, score))
print("PI={}".format(math.pi)) #總長度10,小數為3 [.]也算一個
print("PI={:8.4f}".format(math.pi)) #總長度10,小數為3 [.]也算一個
print("PI={:6.0f}".format(math.pi)) 

print("........4.......")
# f-string:python 3.6之後才能用
print(f"{name}的成績為{score}")
print(f"PI={math.pi}")
print(f"PI={math.pi:6.6f}")
print(f"PI={math.pi:4.0f}")
print(f"PI={math.pi:.3}")  #保留共3位有效數字
print(f"PI={math.pi:.3f}") #保留小數後3
x=10
y=20
print(f"x*y={x*y}")
print(f"x*y={x*y}", end="\t")
print(f"x*y={x*y}", end="\t")
print(f"x*y={x*y}", end="\t")
#print("\n程式執行完畢！")
#input("請按 Enter 鍵關閉視窗...")


