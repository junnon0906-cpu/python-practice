import requests
import time
from datetime import datetime

# ==== Telegram 設定 ====
TOKEN = "AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"  # 你的 Bot Token
CHAT_ID = "8463335795"                          # 你的 Telegram ID

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=data, timeout=10, verify=True)
        if response.status_code == 200:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 已送出通知：{text}")
        else:
            print(f"送訊息失敗，狀態碼：{response.status_code}")
    except Exception as e:
        print(f"發送失敗：{e}")

# ==== 課表設定 ====
# 範例格式：("星期幾", "HH:MM", "課程名稱")
schedule = [
    ("Mon", "08:30", "程式設計"),
    ("Mon", "13:30", "資料結構"),
    ("Tue", "10:00", "電腦網路"),
    ("Wed", "14:00", "人工智慧"),
]

# ==== 主程式 ====
if __name__ == "__main__":
    print("課表提醒程式啟動...")
    already_sent = set()  # 記錄今天已提醒的課

    while True:
        now = datetime.now()
        weekday = now.strftime("%a")  # Mon, Tue, ...
        current_time = now.strftime("%H:%M")

        for day, class_time, class_name in schedule:
            key = f"{weekday}_{class_time}_{class_name}"
            # 如果今天是上課日，且時間到了，且還沒提醒過
            if weekday == day and current_time == class_time and key not in already_sent:
                send_message(f"⚠️ 上課提醒：{class_name} 現在開始！")
                already_sent.add(key)

        # 每 30 秒檢查一次
        time.sleep(30)
