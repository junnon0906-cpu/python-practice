import requests
import datetime

# ---------- 設定 ----------
TOKEN = "8489882646:AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"        # 換成你 Bot 的 Token
CHAT_ID = 8463335795       # 你的 chat_id

# 課表設定
# 格式: "星期": [("課程名稱", "開始時間", "結束時間")]
SCHEDULE = {
    "Monday": [("數位邏輯", "08:30", "10:00"), ("程式設計", "10:30", "12:00")],
    "Tuesday": [("資料結構", "08:30", "10:00")],
    "Wednesday": [("人工智慧", "09:00", "10:30")],
    # 可依你的課表自己填
}

# ---------- 判斷今天課程 ----------
today = datetime.datetime.now().strftime("%A")  # 例如 Monday
courses_today = SCHEDULE.get(today, [])

if courses_today:
    msg_lines = [f"⚠️ 今天的課程提醒 ({today}):"]
    for course, start, end in courses_today:
        msg_lines.append(f"{start}~{end} → {course}")
    message = "\n".join(msg_lines)
else:
    message = f"今天 ({today}) 沒有課程喔～"

# ---------- 發送訊息 ----------
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": message
}

try:
    response = requests.post(url, json=data, timeout=10)  # json= 更穩定
    print(response.text)
except requests.exceptions.RequestException as e:
    print("發送失敗:", e)
