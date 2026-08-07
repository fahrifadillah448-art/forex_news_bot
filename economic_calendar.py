import requests
from datetime import datetime, timezone, timedelta
from config import TICKATLAS_API_KEY


class EconomicCalendar:

    def __init__(self):
        self.url = "https://tickatlas.com/v1/calendar"

    def get_events(self):

        headers = {
            "X-API-Key": TICKATLAS_API_KEY
        }

        params = {
            "currencies": "USD",
            "impact": "high",
            "next_hours": 168
        }

        response = requests.get(
            self.url,
            headers=headers,
            params=params,
            timeout=30
        )

        print("Status:", response.status_code)

        response.raise_for_status()

        data = response.json()

        # Debug struktur response
        if not isinstance(data, dict):
            print("ERROR: API response bukan dictionary")
            print(data)
            return []

        api_data = data.get("data", {})

        if not isinstance(api_data, dict):
            print("ERROR: data bukan dictionary")
            print(api_data)
            return []

        events = api_data.get("events", [])

        if not isinstance(events, list):
            print("ERROR: events bukan list")
            print(events)
            return []

        print("Total events:", len(events))

        results = []

        now = datetime.now(timezone.utc)

        jakarta = timezone(timedelta(hours=7))

        for item in events:

            # Pastikan item memang dictionary
            if not isinstance(item, dict):
                print("SKIP invalid item:", item)
                continue

            title = item.get("title")

            if not title:
                print("SKIP item tanpa title:", item)
                continue

            # Ambil waktu event
            raw_time = (
                item.get("datetime")
                or item.get("date")
                or item.get("time")
               
