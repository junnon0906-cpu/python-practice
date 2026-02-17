import requests

TOKEN = "AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"
CHAT_ID = "8463335795"

message = "⚠️ 測試成功！這是我的課表提醒 Bot"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

try:
    response = requests.post(
        url,
        json=payload,     # ✅ 重點 1：用 json=
        timeout=10,       # ✅ 重點 2：加 timeout
        verify=True       # ✅ 重點 3：強制 SSL 驗證
    )

    print("已送出通知")
    print("狀態碼:", response.status_code)
    print("回傳內容:", response.text)

except Exception as e:
    print("發送失敗:", e)
