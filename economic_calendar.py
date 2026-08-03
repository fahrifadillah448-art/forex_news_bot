from provider import EconomicProvider

class EconomicCalendar(EconomicProvider):

    def get_events(self):
        return [
            {
                "country": "🇺🇸",
                "title": "Provider Ready",
                "time": "--",
                "forecast": "--",
                "previous": "--",
                "impact": "🔥"
            }
        ]
