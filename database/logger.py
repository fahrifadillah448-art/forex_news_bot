from database.supabase_client import supabase


def log_info(message):
    supabase.table("bot_logs").insert({
        "level": "INFO",
        "message": message
    }).execute()


def log_error(message):
    supabase.table("bot_logs").insert({
        "level": "ERROR",
        "message": message
    }).execute()
