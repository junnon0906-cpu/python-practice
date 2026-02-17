import requests

# ✅ 你的 Bot Token
TOKEN = "AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"

# ✅ 你的 Telegram 帳號 CHAT_ID（就是你 /start 過的那個）
CHAT_ID = 8463335795

# 測試訊息
message = "⚠️ 測試課表提醒：這是一條測試通知！"

# Telegram API URL
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# 使用 json= 參數發送，並加上 timeout 和 SSL 驗證
data = {
    "chat_id": CHAT_ID,
    "text": message
}

try:
    response = requests.post(url, json=data, timeout=10, verify=True)
    if response.status_code == 200:
        print("✅ 訊息已送出到 Telegram！")
    else:
        print("❌ 發送失敗，回傳：", response.text)
except requests.exceptions.RequestException as e:
    print("❌ 發送過程出錯：", e)
