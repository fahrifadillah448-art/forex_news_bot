from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def event_exists(event_id):

    response = (
        supabase
        .table("sent_events")
        .select("event_id")
        .eq("event_id", event_id)
        .limit(1)
        .execute()
    )

    return len(response.data) > 0


def save_event(event):

    result = (
        supabase
        .table("sent_events")
        .insert({
            "event_id": event["event_id"],
            "title": event["title"],
            "event_time": convert_to_timestamp(
                event["time"]
            )
        })
        .execute()
    )

    return result


def convert_to_timestamp(time_string):

    # Input:
    # 2026-08-07 19:30 WIB
    #
    # Output:
    # 2026-08-07T19:30:00+07:00

    clean_time = time_string.replace(
        " WIB",
        ""
    )

    return clean_time.replace(
        " ",
        "T"
    ) + "+07:00"
