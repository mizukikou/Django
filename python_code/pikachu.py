class Pikachu:
    def __init__(self, level):
        # 💡 依照你的要求：剛抓到時，強制初始化為空字串（空白名稱）
        self.nickname = ""  
        self.level = level
        self.hp = level * 10

    def thunderbolt(self):
        # 防呆機制：如果名字還是空的，就稱呼牠為「皮卡丘」，否則用牠的暱稱
        display_name = self.nickname if self.nickname else "皮卡丘"
        damage = self.level * 2
        print(f"⚡ {display_name} 使用了『十萬伏特』！造成了 {damage} 點傷害！")

    def print_status(self):
        display_name = self.nickname if self.nickname else "（尚未取名）"
        print(f"📊 【{display_name}】 等級: {self.level} | 目前血量: {self.hp}\n")


# ==================== 🎮 遊戲實際執行畫面 ====================

print("🎉 恭喜你！成功捕捉到一隻皮卡丘！")
# 1. 🌟 實體化時只需要指定等級，名字一開始強制為 ""
p1 = Pikachu(level=5)
p1.print_status()  # 顯示：📊 【（尚未取名）】 等級: 5

# 2. 畫面跳出對話框詢問使用者
ans = input("❓ 要幫這隻寶可夢取個新名字嗎？(y/n): ").strip().lower()

if ans == 'y':
    # 3. 使用者想取名，跳出輸入框讓使用者輸入
    new_name = input("✍️ 請輸入新名字: ").strip()
    
    if new_name: # 確保使用者沒有交白卷
        p1.nickname = new_name
        print(f"✨ 命名成功！牠的新名字決定是【{p1.nickname}】了！")
    else:
        print("⚠️ 由於輸入為空，將維持空白名稱。")
else:
    print("👌 好的，目前先不幫牠取名字。")

print("-" * 40)
# 4. 再次查看最終狀態與戰鬥測試
p1.print_status()
p1.thunderbolt()
