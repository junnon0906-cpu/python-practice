import requests

TOKEN = "AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"
CHAT_ID = "8463335795"

message = "⚠️ 測試成功！這是我的課表提醒 Bot"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, json=payload)  # 改成 json=payload

print("已送出通知")
print(response.status_code, response.text)  # 這行可以看回傳
