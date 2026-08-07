import requests
from datetime import datetime, timezone
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

        # Ambil list event
        if isinstance(data, dict):
            events_data = data.get("data", [])
        else:
            events_data = data

        print("Total events:", len(events_data))

        events = []

        now = datetime.now(timezone.utc)

        for item in events_data:

            title = (
                item.get("title")
                or item.get("event")
                or item.get("name")
                or "Unknown Event"
            )

            event_time_raw = (
                item.get("event_time")
                or item.get("datetime")
                or item.get("date")
                or item.get("time")
            )

            if not event_time_raw:
                print("SKIP:", title, "| Tidak ada waktu")
                continue

            try:

                event_time = datetime.fromisoformat(
                    event_time_raw.replace("Z", "+00:00")
                )

                if event_time.tzinfo is None:
                    event_time = event_time.replace(
                        tzinfo=timezone.utc
                    )

                event_time = event_time.astimezone(timezone.utc)

            except Exception as e:

                print(
                    "SKIP:",
                    title,
                    "| Format waktu error:",
                    event_time_raw
                )

                continue

            minutes_left = (
                event_time - now
            ).total_seconds() / 60

            print(
                f"EVENT: {title} | "
                f"UTC: {event_time} | "
                f"Minutes left: {minutes_left:.2f}"
            )

            # Event yang sudah lewat
            if minutes_left < 0:
                print("SKIP: Event sudah lewat")
                continue

            # Hanya ambil event dalam 3 jam ke depan
            if minutes_left > 180:
                print("SKIP: Event masih terlalu jauh")
                continue

            event_id = (
                str(item.get("event_id"))
                if item.get("event_id")
                else f"{title}_{event_time.isoformat()}"
            )

            country = (
                item.get("country")
                or item.get("currency")
                or "USD"
            )

            impact = (
                item.get("impact")
                or "high"
            )

            forecast = (
                item.get("forecast")
                if item.get("forecast") is not None
                else "-"
            )

            previous = (
                item.get("previous")
                if item.get("previous") is not None
                else "-"
            )

            events.append({
                "event_id": event_id,
                "country": country,
                "title": title,
                "time": event_time.strftime(
                    "%Y-%m-%d %H:%M UTC"
                ),
                "impact": impact,
                "forecast": forecast,
                "previous": previous
            })

        print("Selected events:", len(events))

        return events
