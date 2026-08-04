import requests
from datetime import datetime
from zoneinfo import ZoneInfo

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
                "next_hours": 168
            },
            timeout=20
        )

        print("Status:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return []

        data = response.json()

        print("Total events:", data["data"]["count"])

        events = []

        for item in data["data"]["events"]:

            # UTC -> WIB
            utc_time = datetime.fromisoformat(
                item["datetime"].replace("Z", "+00:00")
            )

            wib_time = utc_time.astimezone(
                ZoneInfo("Asia/Jakarta")
            )

            formatted_time = wib_time.strftime("%d %B %Y | %H:%M WIB")

            # Impact
            impact = item.get("impact", "").lower()

            if impact == "high":
                impact = "🔥🔥🔥 High"
            elif impact == "medium":
                impact = "🔥🔥 Medium"
            elif impact == "low":
                impact = "🔥 Low"
            else:
                impact = "-"

            events.append({
    "id": f"{item.get('currency')}_{item.get('event')}_{item.get('datetime')}",
    "country": f"🇺🇸 {item.get('currency', 'USD')}",
    "title": item.get("event", "Unknown Event"),
    "time": formatted_time,
    "forecast": item.get("forecast") or "-",
    "previous": item.get("previous") or "-",
    "actual": item.get("actual") or "-",
    "impact": impact
})
        return events
