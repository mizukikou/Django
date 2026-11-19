choice = int(input("要轉換(1)公尺->英呎  (2)公斤->英鎊:"))
if choice in [1,2]:
    number = float(input("請輸入欲轉換的數字:"))
    if choice == 1:
        result = number * 3.2  #3.2808
        print(f"{number:.6f}公尺 = {result:.6f}英呎")
    elif choice == 2:
        result = number * 2.2  #2.2046
        print(f"{number:.6f}公斤 = {result:.6f}英鎊")
else:
    print("無此選項")

length = int(input("請輸入身高(cm):"))
weight = int(input("請輸入體重(kg):"))
bmi = weight / (length/100)**2
print(f"BMI 值為{bmi:.2f}。屬",end='')
if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("正常範圍")
elif bmi < 27:
    print("稍重")
elif bmi < 30:
    print("輕度肥胖")
elif bmi < 35:
    print("中度肥胖")
else:
    print("重度肥胖")





length_u = int(input("請輸入上底長度:"))
length_l = int(input("請輸入下底長度:"))
height = int(input("請輸入高度:"))
area = (length_u + length_l) * height / 2
print(f"梯形面積:  {area:.2f}")