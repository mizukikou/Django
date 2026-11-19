score = int(input("請輸入成績:"))
if (score>=90): #>=90
    print("Level A")
elif(score>=80): #89~80
    print("Level B")
elif(score>=70): #79~70
    print("Level C")
elif(score>=60): #69~60
    print("Level D")
else: #<60
    print("Level E")