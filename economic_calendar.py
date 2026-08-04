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

        now = datetime.now(ZoneInfo("UTC"))

        for item in data["data"]["events"]:

            utc_time = datetime.fromisoformat(
                item["datetime"].replace("Z", "+00:00")
            )

            minutes_left = (
                utc_time - now
            ).total_seconds() / 60

            # hanya kirim jika 20-30 menit sebelum berita
            if minutes_left > 30:
                continue

            if minutes_left < 20:
                continue

            wib_time = utc_time.astimezone(
                ZoneInfo("Asia/Jakarta")
            )

            formatted_time = wib_time.strftime(
                "%d %B %Y | %H:%M WIB"
            )

            impact = item.get("impact", "").lower()

            if impact == "high":
                impact = "🔥🔥🔥 High Impact"
            elif impact == "medium":
                impact = "🔥🔥 Medium Impact"
            else:
                impact = "🔥 Low Impact"

            events.append({
                "country": f"🇺🇸 {item.get('currency','USD')}",
                "title": item.get("event","Unknown Event"),
                "time": formatted_time,
                "forecast": item.get("forecast") or "-",
                "previous": item.get("previous") or "-",
                "actual": item.get("actual") or "-",
                "impact": impact,
                "minutes_left": int(minutes_left)
            })

        return events
