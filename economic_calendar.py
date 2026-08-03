import requests
import os
from datetime import datetime

API_KEY = os.getenv("FMP_API_KEY")

def get_events():
    today = datetime.utcnow().strftime("%Y-%m-%d")

    url = (
        f"https://financialmodelingprep.com/stable/economic-calendar"
        f"?from={today}&to={today}&apikey={API_KEY}"
    )

    response = requests.get(url, timeout=20)
    data = response.json()

    events = []

    for item in data:
        if item.get("country") == "US":
            events.append({
                "country": "🇺🇸",
                "title": item.get("event", "Unknown"),
                "time": item.get("date", ""),
                "forecast": item.get("estimate", "-"),
                "previous": item.get("previous", "-"),
                "impact": "🔥"
            })

    return events
