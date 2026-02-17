import requests

TOKEN = "8489882646:AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"
CHAT_ID = "8463335795"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "✅ SSL + JSON 測試成功（如果你看到這行就對了）"
}

try:
    r = requests.post(
        url,
        json=payload,      # ✅ 一定要用 json=
        timeout=10,        # ✅ 防止卡死
        verify=True        # ✅ 強制 SSL 驗證
    )
    print(r.status_code)
    print(r.text)

except requests.exceptions.RequestException as e:
    print("❌ 發送失敗：", e)
