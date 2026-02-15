import datetime

# 課表（之後可以自己改）
import datetime

schedule = {
    "Monday": [
        ("09:10", "數學"),
        ("13:10", "程式設計")
    ],
    "Tuesday": [
        ("10:10", "英文"),
        ("14:10", "資料結構")
    ],
    "Wednesday": [
        ("08:10", "體育")
    ]
}

now = datetime.datetime.now()
today = now.strftime("%A")
current_time = now.strftime("%H:%M")

print("今天是：", today)
print("現在時間：", current_time)

def to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

now_min = to_minutes(current_time)

if today in schedule:
    print("今天的課：")
    for time, course in schedule[today]:
        class_min = to_minutes(time)
        diff = class_min - now_min

        print(f"{time} {course}")

        if 0 <= diff <= 30:
            print(f"⚠️  提醒：{course} 還有 {diff} 分鐘要上課！")
else:
    print("今天沒有課 🎉")
