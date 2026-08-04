import requests
from config import TICKATLAS_API_KEY
from provider import EconomicProvider


class EconomicCalendar(EconomicProvider):

    def get_events(self):

        response = requests.get(
            "https://tickatlas.com/v1/calendar",
            headers={
                "X-API-Key": TICKATLAS_API_KEY
            },
            params={
                "currencies": "USD",
                "impact": "high",
                "next_hours": 24
            },
            timeout=20
        )

        print("Status:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return []

        data = response.json()

        events = []

        for item in data["data"]["events"]:
            events.append({
                "country": "🇺🇸",
                "title": item.get("event", "Unknown"),
                "time": item.get("datetime", "--"),
                "forecast": item.get("forecast", "-"),
                "previous": item.get("previous", "-"),
                "impact": item.get("impact", "-")
            })

        return events
