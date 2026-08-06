"""
Python 初中階教學 Demo
涵蓋：變數/型別、字串格式化、條件判斷、迴圈、串列、字典、函式、例外處理
"""

SEP = "=" * 50


# ──────────────────────────────────────────────────
# 第 1 節：變數宣告與資料型別
# ──────────────────────────────────────────────────
print(SEP)
print("【第 1 節】變數宣告與資料型別")
print(SEP)

name   = "小明"       # str
age    = 18           # int
score  = 92.5         # float
passed = True         # bool

print(f"姓名={name}  型別={type(name)}")
print(f"年齡={age}   型別={type(age)}")
print(f"成績={score} 型別={type(score)}")
print(f"及格={passed} 型別={type(passed)}")

# 動態型別：同一變數可重新賦值為不同型別
x = 10
print(f"\n原本 x={x}，型別={type(x)}")
x = "hello"
print(f"改成 x={x}，型別={type(x)}")


# ──────────────────────────────────────────────────
# 第 2 節：字串格式化三種寫法
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 2 節】字串格式化：%  /  format()  /  f-string")
print(SEP)

pi = 3.14159265

print("--- % 格式化 ---")
print("姓名=%s，成績=%.1f" % (name, score))
print("PI=%10.4f" % pi)           # 總寬 10（包含小數點與數字）、小數 4 位

print("\n--- format() ---")
print("姓名={}，成績={:.1f}".format(name, score))
print("PI={:10.4f}".format(pi))

print("\n--- f-string（Python 3.6+）---")
print(f"姓名={name}，成績={score:.1f}")
print(f"PI={pi:10.4f}")
print(f"PI={pi:.4}（4 位有效數字）")  # （總寬僅包含整數與小數）


# ──────────────────────────────────────────────────
# 第 3 節：條件判斷 if / elif / else
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 3 節】條件判斷 if / elif / else")
print(SEP)

def grade_label(s):
    if s >= 90:
        return "A（優秀）"
    elif s >= 80:
        return "B（良好）"
    elif s >= 70:
        return "C（普通）"
    elif s >= 60:
        return "D（待加強）"
    else:
        return "F（不及格）"

for test_score in [95, 82, 73, 61, 45]:
    print(f"成績 {test_score} → 等第 {grade_label(test_score)}")

# 三元運算式（條件表達式）
status = "及格" if score >= 60 else "不及格"
print(f"\n{name} {score} 分 → {status}")


# ──────────────────────────────────────────────────
# 第 4 節：for 迴圈
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 4 節】for 迴圈")
print(SEP)

print("--- range(1, 6) ---")
for i in range(1, 6):
    print(i, end="  ")
print()

print("\n--- 步長 range(0, 11, 2) ---")
for i in range(0, 11, 2):
    print(i, end="  ")
print()

print("\n--- 倒序 range(10, 0, -2) ---")
for i in range(10, 0, -2):
    print(i, end="  ")
print()

print("\n--- 遍歷串列 ---")
fruits = ["蘋果", "香蕉", "橘子", "芒果"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}. {fruit}")

print("\n--- 九九乘法表（3~5段）---")
for row in range(3, 6):
    for col in range(1, 10):
        print(f"{row}×{col}={row*col:2d}", end="  ")
    print()


# ──────────────────────────────────────────────────
# 第 5 節：while 迴圈 / break / continue
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 5 節】while 迴圈 / break / continue")
print(SEP)

print("--- 計算 1+2+…+10 ---")
total, n = 0, 1
while n <= 10:
    total += n
    n += 1
print(f"總和 = {total}")

print("\n--- break：找到第一個 3 的倍數就停 ---")
for i in range(1, 20):
    if i % 3 == 0:
        print(f"找到 {i}，停止迴圈")
        break

print("\n--- continue：跳過偶數，只印奇數 ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end="  ")
print()


# ──────────────────────────────────────────────────
# 第 6 節：串列 list
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 6 節】串列 list")
print(SEP)

scores = [85, 92, 78, 66, 90]
print(f"原始串列：{scores}")
print(f"長度={len(scores)}，最大={max(scores)}，最小={min(scores)}，總和={sum(scores)}")

scores.append(88)
print(f"\nappend(88)：{scores}")

scores.insert(2, 100)
print(f"insert(2, 100)：{scores}")

scores.remove(66)
print(f"remove(66)：{scores}")

popped = scores.pop()
print(f"pop()={popped}，剩下：{scores}")

print(f"\n切片 [1:4]：{scores[1:4]}")
print(f"反轉 [::-1]：{scores[::-1]}")

scores.sort()
print(f"排序後：{scores}")

print("\n--- List Comprehension ---")
squares = [x ** 2 for x in range(1, 8)]
print(f"1~7 的平方：{squares}")

evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"1~20 的偶數：{evens}")


# ──────────────────────────────────────────────────
# 第 7 節：字典 dict
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 7 節】字典 dict")
print(SEP)

student = {
    "name":   "小明",
    "age":    18,
    "scores": {"國文": 85, "數學": 92, "英文": 78},
}

print(f"姓名：{student['name']}")
print(f"年齡：{student.get('age', 'N/A')}")
print(f"數學：{student['scores']['數學']}")

student["email"] = "ming@example.com"   # 新增鍵
student["age"]   = 19                    # 修改值
print(f"\n更新後：{student}")

print("\n--- 遍歷字典 ---")
for key, value in student.items():
    print(f"  {key}: {value}")

print(f"\n所有鍵：{list(student.keys())}")
print(f"'email' 存在？{'email' in student}")

# Dict Comprehension
squares_dict = {n: n ** 2 for n in range(1, 6)}
print(f"\n平方字典：{squares_dict}")


# ──────────────────────────────────────────────────
# 第 8 節：Tuple 與 Set
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 8 節】Tuple 與 Set")
print(SEP)

print("--- Tuple（不可變序列）---")
point = (3, 7)
x_coord, y_coord = point           # 解包
print(f"座標：{point}，x={x_coord}，y={y_coord}")

rgb = (255, 128, 0)
print(f"RGB：{rgb}，紅色分量={rgb[0]}")

print("\n--- Set（不重複集合）---")
tags = {"Python", "AI", "Python", "資料科學", "AI"}
print(f"集合（自動去重）：{tags}")

tags.add("機器學習")
tags.discard("AI")
print(f"add / discard 後：{tags}")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"聯集 a|b：{a | b}")
print(f"交集 a&b：{a & b}")
print(f"差集 a-b：{a - b}")


# ──────────────────────────────────────────────────
# 第 9 節：函式 def / 預設參數 / 任意參數
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 9 節】函式")
print(SEP)

print("--- 基本函式 ---")
def greet(person, greeting="你好"):
    return f"{greeting}，{person}！"

print(greet("小明"))
print(greet("老師", greeting="早安"))

print("\n--- 多個回傳值 ---")
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 9, 5, 7])
print(f"最小={lo}，最大={hi}")

print("\n--- *args（不定數量位置參數）---")
def total(*nums):
    return sum(nums)

print(f"total(1,2,3)={total(1, 2, 3)}")
print(f"total(10,20,30,40)={total(10, 20, 30, 40)}")

print("\n--- **kwargs（不定數量關鍵字參數）---")
def show_info(**info):
    for k, v in info.items():
        print(f"  {k}: {v}")

show_info(name="小明", age=18, city="台北")


# ──────────────────────────────────────────────────
# 第 10 節：Lambda / map / filter
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 10 節】Lambda 與高階函式 map / filter")
print(SEP)

square = lambda x: x ** 2
print(f"lambda 平方：square(5) = {square(5)}")

nums = [1, 2, 3, 4, 5, 6, 7, 8]

squared = list(map(lambda x: x ** 2, nums))
print(f"\nmap 平方：{squared}")

evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"filter 偶數：{evens}")

# sorted 搭配 key
words = ["banana", "apple", "cherry", "date"]
sorted_by_len = sorted(words, key=lambda w: len(w))
print(f"\n依長度排序：{sorted_by_len}")

students = [
    {"name": "小明", "score": 82},
    {"name": "小華", "score": 95},
    {"name": "小美", "score": 78},
]
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("\n依成績高低排序：")
for s in sorted_students:
    print(f"  {s['name']}：{s['score']}")


# ──────────────────────────────────────────────────
# 第 11 節：例外處理 try / except / else / finally
# ──────────────────────────────────────────────────
print(f"\n{SEP}")
print("【第 11 節】例外處理 try / except / else / finally")
print(SEP)

print("--- 捕捉除以零 ---")
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  錯誤：除數不可為零！")
        return None
    else:
        print(f"  {a} / {b} = {result}")
        return result
    finally:
        print("  （finally 一定執行）")

safe_divide(10, 2)
print()
safe_divide(10, 0)

print("\n--- 捕捉多種例外 ---")
def parse_int(s):
    try:
        return int(s)
    except ValueError:
        print(f"  ValueError：'{s}' 無法轉為整數")
    except TypeError:
        print(f"  TypeError：型別不對，收到 {type(s)}")

parse_int("123")
parse_int("abc")
parse_int(None)

print("\n--- 主動 raise 例外 ---")
def set_age(a):
    if not isinstance(a, int):
        raise TypeError("年齡必須為整數")
    if a < 0 or a > 150:
        raise ValueError(f"年齡 {a} 超出合理範圍")
    return a

for val in [25, -1, 200, "old"]:
    try:
        print(f"  set_age({val!r}) → {set_age(val)}")
    except (ValueError, TypeError) as e:
        print(f"  set_age({val!r}) → 例外：{e}")


print(f"\n{SEP}")
print("教學 Demo 結束，Python 加油！")
print(SEP)
