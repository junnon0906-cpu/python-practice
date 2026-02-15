import datetime

# 課表（之後可以自己改）
schedule = {
    "Monday": [
        ("09:00", "數學"),
        ("13:00", "程式設計")
    ],
    "Tuesday": [
        ("10:00", "英文"),
        ("14:00", "資料結構")
    ]
}

now = datetime.datetime.now()
today = now.strftime("%A")
current_time = now.strftime("%H:%M")

print("今天是：", today)
print("現在時間：", current_time)

if today in schedule:
    print("今天的課：")
    for time, course in schedule[today]:
        print(time, course)
else:
    print("今天沒有課 🎉")
