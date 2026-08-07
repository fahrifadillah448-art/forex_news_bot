import requests

from config import TOPIC


def send_notification(title, message):

    url = f"https://ntfy.sh/{TOPIC}"

    try:

        response = requests.post(
            url,
            data=message.encode("utf-8"),
            headers={
                "Title": title,
                "Priority": "default"
            },
            timeout=20
        )

        print("Notify Status:", response.status_code)
        print("Notify Response:", response.text)

        # HTTP selain 2xx dianggap gagal
        response.raise_for_status()

        print("Notification sent successfully")

        return True

    except requests.exceptions.RequestException as e:

        print("Notification failed:", str(e))

        raise
