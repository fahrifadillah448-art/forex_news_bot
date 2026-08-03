import requests

TOPIC = "forex_pai_2026"

message = """
🤖 Forex Intelligence Bot

✅ Python berhasil dijalankan
✅ GitHub Actions berhasil
✅ Siap untuk mengambil data ekonomi
"""

requests.post(
    f"https://ntfy.sh/{TOPIC}",
    data=message.encode("utf-8"),
    headers={
        "Title": "Forex Intelligence",
        "Priority": "default"
    }
)

print("Notification sent!")
