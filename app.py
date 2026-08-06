from notify import send_notification
from economic_calendar import EconomicCalendar
from database.supabase_client import event_exists, save_event

calendar = EconomicCalendar()
events = calendar.get_events()

if not events:
    print("No events found")
    exit()

message = "📅 Forex Intelligence\n\n"

new_events = []

for event in events:

    if event_exists(event["event_id"]):
        print(f"Skip: {event['title']}")
        continue

    new_events.append(event)

    message += (
        f"{event['country']} {event['title']}\n"
        f"🕒 {event['time']}\n"
        f"🔥 Impact : {event['impact']}\n"
        f"📊 Forecast : {event['forecast']}\n"
        f"📉 Previous : {event['previous']}\n\n"
    )

if not new_events:
    print("No new events")
    exit()

send_notification("High Impact Events", message)

for event in new_events:
    save_event(event)

print(f"Notification sent ({len(new_events)} new events)")
