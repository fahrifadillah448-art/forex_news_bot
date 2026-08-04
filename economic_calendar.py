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
        print("Response text:")
        print(response.text)

        return []
