from notify import send_notification
from economic_calendar import EconomicCalendar

calendar = EconomicCalendar()
events = calendar.get_events()

if not events:
    print("No events found")
    exit()

message = "📅 Forex Intelligence\n\n"

for event in events:

    message += (
        f"{event['country']} {event['title']}\n"
        f"🕒 {event['time']}\n"
        f"🔥 Impact : {event['impact']}\n"
        f"📊 Forecast : {event['forecast']}\n"
        f"📉 Previous : {event['previous']}\n\n"
    )

send_notification(
    "High Impact Events",
    message
)

print(message)
print("Economic Calendar Sent!")
