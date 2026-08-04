from notify import send_notification
from economic_calendar import EconomicCalendar
from sent_events import already_sent, mark_sent

calendar = EconomicCalendar()
events = calendar.get_events()

if not events:
    print("No events found")
    exit()

new_events = []

for event in events:

    if already_sent(event["id"]):
        print(f"Skip: {event['title']}")
        continue

    new_events.append(event)
    mark_sent(event["id"])

if not new_events:
    print("No new events")
    exit()

message = "📊 FOREX INTELLIGENCE\n"
message += "━━━━━━━━━━━━━━━━━━\n\n"

for event in new_events:

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
