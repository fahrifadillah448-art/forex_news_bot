from notify import send_notification
from economic_calendar import EconomicCalendar
from database.supabase_client import event_exists, save_event
from database.logger import log_info, log_error

import hashlib


def generate_event_id(event):
    """
    Membuat ID unik dan stabil untuk setiap economic event.
    ID dibuat dari kombinasi:
    country + title + time
    """

    raw = (
        f"{event.get('country', '')}|"
        f"{event.get('title', '')}|"
        f"{event.get('time', '')}"
    )

    return hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()


try:

    # =========================
    # BOT START
    # =========================

    log_info("Bot started")

    calendar = EconomicCalendar()

    events = calendar.get_events()

    log_info(f"Found {len(events)} events")

    if not events:
        log_info("No events found")
        print("No events found")
        exit()


    # =========================
    # PREPARE MESSAGE
    # =========================

    message = "📅 Forex Intelligence\n\n"

    new_events = []


    # =========================
    # CHECK DUPLICATE EVENTS
    # =========================

    for event in events:

        # Generate event ID if provider
        # does not supply one
        if not event.get("event_id"):

            event["event_id"] = generate_event_id(event)

        event_id = event["event_id"]

        if event_exists(event_id):

            log_info(
                f"Skip duplicate: {event['title']}"
            )

            continue

        new_events.append(event)

        message += (
            f"{event['country']} "
            f"{event['title']}\n"
            f"🕒 {event['time']}\n"
            f"🔥 Impact : {event['impact']}\n"
            f"📊 Forecast : {event['forecast']}\n"
            f"📉 Previous : {event['previous']}\n\n"
        )


    # =========================
    # NO NEW EVENTS
    # =========================

    if not new_events:

        log_info("No new events")

        print("No new events")

        exit()


    # =========================
    # SEND NOTIFICATION
    # =========================

    log_info(
        f"Sending notification for "
        f"{len(new_events)} events"
    )

    send_notification(
        "High Impact Events",
        message
    )

    log_info("Notification sent successfully")


    # =========================
    # SAVE EVENTS
    # =========================

    for event in new_events:

        save_event(event)

        log_info(
            f"Saved event: {event['title']}"
        )


    log_info(
        f"Saved {len(new_events)} events"
    )

    print("Done")


# =========================
# GLOBAL ERROR HANDLER
# =========================

except Exception as e:

    error_message = (
        f"{type(e).__name__}: {str(e)}"
    )

    log_error(error_message)

    print(
        f"BOT ERROR: {error_message}"
    )

    raise
