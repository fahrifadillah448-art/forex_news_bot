import requests
from config import TOPIC

def send_notification(title, message):
    response = requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": title,
            "Priority": "default"
        }
    )

    print("Notify Status:", response.status_code)
    print("Notify Response:", response.text)
