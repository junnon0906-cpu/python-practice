import requests

TOKEN = "8489882646:AAHCleOidktsYOfZ7xxkbiqN8BIaCt2ew7w"
CHAT_ID = "8463335795"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "📚 課表提醒測試：如果你看到這行，代表一切正常"
}

r = requests.post(url, json=payload, timeout=10)
print(r.json())
