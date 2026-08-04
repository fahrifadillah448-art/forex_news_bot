from notify import send_notification
from economic_calendar import EconomicCalendar

calendar = EconomicCalendar()
events = calendar.get_events()

if not events:
    print("No events found")
    exit()

message = "📊 FOREX INTELLIGENCE\n"
message += "━━━━━━━━━━━━━━━━━━\n\n"

for event in events:

    message += (
        f"{event['country']}\n"
        f"📌 {event['title']}\n"
        f"🕒 {event['time']}\n"
        f"{event['impact']}\n\n"
        f"📈 Forecast : {event['forecast']}\n"
        f"📉 Previous : {event['previous']}\n"
        f"✅ Actual   : {event['actual']}\n"
        f"\n━━━━━━━━━━━━━━━━━━\n\n"
    )

send_notification(
    "📊 Forex Intelligence",
    message
)

print(message)
print("Economic Calendar Sent!")
