import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 建立資料
df = pd.DataFrame({
    "坪數":[10,20,30,40,50],
    "房價":[300,500,700,900,1100]
})

# 建立 X、y
X = df[["坪數"]]
y = df["房價"]
print(X)
print(y)

# 建立模型
model = LinearRegression()

# 訓練
model.fit(X, y)

print("截距:", model.intercept_)
print("斜率:", model.coef_[0])

# 畫圖
# 顯示繁體中文
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.scatter(X, y)
plt.plot(X, model.predict(X), color="red")
plt.xlabel("坪數")
plt.ylabel("房價")
plt.title("線性回歸")
plt.show()

new_data = pd.DataFrame({
    "坪數": [35]
})

price = model.predict(new_data)

print("35坪預測房價：", price[0])
