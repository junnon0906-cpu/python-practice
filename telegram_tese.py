import requests

TOKEN = "8489882646:AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"
CHAT_ID = "8463335795"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "✅ 校園網路測試成功！"
}

response = requests.post(
    url,
    json=payload,
    timeout=10,
    verify=False   # 🔴 關鍵：關掉 SSL 驗證
)

print("HTTP:", response.status_code)
print(response.text)
