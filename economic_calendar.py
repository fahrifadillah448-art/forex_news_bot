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

        print("API response type:", type(data))

        if not isinstance(data, dict):
            print("ERROR: response API bukan dictionary")
            print(data)
            return []

        # Ambil data utama
        api_data = data.get("data", {})

        if not isinstance(api_data, dict):
            print("ERROR: data bukan dictionary")
            print(api_data)
            return []

        # Ambil events
        events = api_data.get("events", [])

        if not isinstance(events, list):
            print("ERROR: events bukan list")
            print(events)
            return []

        print("Total events:", len(events))

        results = []

        now = datetime.now(timezone.utc)

        for item in events:

            # Pastikan item berbentuk dictionary
            if not isinstance(item, dict):
                print("SKIP item invalid:", item)
                continue

            title = item.get("title")

            if not title:
                print("SKIP event tanpa title")
                continue

            raw_time = item.get("datetime")

            if raw_time is None:
                raw_time = item.get("date")

            if raw_time is None:
                raw_time = item.get("time")

            if raw_time is None:
                raw_time = item.get("event_time")

            if raw_time is None:
                print("SKIP event tanpa waktu:", title)
                continue

            try:

                event_time = datetime.fromisoformat(
                    str(raw_time).replace("Z", "+00:00")
                )

                if event_time.tzinfo is None:
                    event_time = event_time.replace(
                        tzinfo=timezone.utc
                    )

                event_time = event_time.astimezone(
                    timezone.utc
                )

            except Exception as e:

                print(
                    "SKIP waktu tidak valid:",
                    title,
                    raw_time,
                    e
                )

                continue

            minutes_left = (
                event_time - now
            ).total_seconds() / 60

            print(
                "EVENT:",
                title,
                "| UTC:",
                event_time,
                "| Minutes left:",
                round(minutes_left, 2)
            )

            # Hanya event 0-60 menit dari sekarang
            if minutes_left < 0:
                continue

            if minutes_left > 60:
                continue

            event_id = item.get("id")

            if event_id is None:
                event_id = item.get("event_id")

            if event_id is None:
                event_id = (
                    title
                    + "_"
                    + event_time.isoformat()
                )

            country = item.get("country")

            if country is None:
                country = item.get("currency")

            if country is None:
                country = "USD"

            impact = item.get("impact")

            if impact is None:
                impact = "High"

            forecast = item.get("forecast")

            if forecast is None:
                forecast = "-"

            previous = item.get("previous")

            if previous is None:
                previous = "-"

            actual = item.get("actual")

            if actual is None:
                actual = "-"

            jakarta = timezone(
                timedelta(hours=7)
            )

            jakarta_time = event_time.astimezone(
                jakarta
            )

            results.append({
                "event_id": str(event_id),
                "country": str(country),
                "title": str(title),
                "time": jakarta_time.strftime(
                    "%Y-%m-%d %H:%M WIB"
                ),
                "forecast": str(forecast),
                "previous": str(previous),
                "actual": str(actual),
                "impact": str(impact),
                "minutes_left": round(
                    minutes_left,
                    2
                )
            })

        print(
            "Events setelah filter:",
            len(results)
        )

        return results
