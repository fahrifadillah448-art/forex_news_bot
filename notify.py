import requests

TOPIC = "forex_pai_2026"

def send_notification(title, message):
    requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": title,
            "Priority": "default"
        }
    )
