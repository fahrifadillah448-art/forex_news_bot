import requests
from config import TICKATLAS_API_KEY
from provider import EconomicProvider

class EconomicCalendar(EconomicProvider):

    def get_events(self):

        url = "https://tickatlas.com/v1/calendar"

        headers = {
            "X-API-Key": TICKATLAS_API_KEY
        }

        params = {
            "currencies": "USD",
            "impact": "high",
            "next_hours": 24
        }

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=20
        )

        if response.status_code != 200:
            print(response.status_code)
            print(response.text)
            return []

        data = response.json()

        events = []

        for item in data["data"]["events"]:

            events.append({
                "country": "🇺🇸",
                "title": item["event"],
                "time": item["datetime"],
                "forecast": item.get("forecast", "-"),
                "previous": item.get("previous", "-"),
                "impact": "🔥"
            })

        return events
