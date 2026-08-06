from notify import send_notification
from economic_calendar import EconomicCalendar
from database.supabase_client import event_exists, save_event
from database.logger import log_info, log_error

try:

    log_info("Bot started")

    calendar = EconomicCalendar()
    events = calendar.get_events()

    log_info(f"Found {len(events)} events")

    if not events:
        log_info("No events found")
        exit()

    message = "📅 Forex Intelligence\n\n"

    new_events = []

    for event in events:

        if event_exists(event["event_id"]):
            log_info(f"Skip: {event['title']}")
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
        log_info("No new events")
        print("No new events")
        exit()

    send_notification("High Impact Events", message)

    log_info("Notification sent")

    for event in new_events:
        save_event(event)

    log_info(f"Saved {len(new_events)} events")

    print("Done")

except Exception as e:

    log_error(str(e))

    raise
