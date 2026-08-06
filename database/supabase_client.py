from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def event_exists(event_id):
    response = (
        supabase.table("sent_events")
        .select("id")
        .eq("event_id", event_id)
        .execute()
    )

    return len(response.data) > 0


def save_event(event):
    supabase.table("sent_events").insert({
        "event_id": event["event_id"],
        "title": event["title"],
        "event_time": event["time"]
    }).execute()
