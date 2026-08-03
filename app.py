from notify import send_notification
from calendar import get_events

events = get_events()

message = "📅 Forex Intelligence Bot\n\n"

for event in events:
    message += (
        f"{event['country']} {event['title']}\n"
        f"🕒 {event['time']}\n"
        f"Impact : {event['impact']}\n"
        f"Forecast : {event['forecast']}\n"
        f"Previous : {event['previous']}\n\n"
    )

send_notification("Agenda Ekonomi", message)

print("Economic Calendar Sent!")
