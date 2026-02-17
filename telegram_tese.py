import requests

TOKEN = "AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"
CHAT_ID = "8463335795"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "⚠️ 測試成功！這是我的課表提醒 Bot"
}

try:
    response = requests.post(
        url,
        json=payload,      # 🔴 關鍵：用 json=
        timeout=10,        # 🔴 防止卡住
        verify=True        # 🔴 強制 SSL 驗證
    )

    print("HTTP 狀態碼:", response.status_code)
    print("Telegram 回傳:", response.text)

except Exception as e:
    print("發生錯誤：", e)
