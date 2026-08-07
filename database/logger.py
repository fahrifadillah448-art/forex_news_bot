from database.supabase_client import supabase


def log_info(message):
    response = supabase.table("bot_logs").insert({
        "level": "INFO",
        "message": message
    }).execute()

    return response.data


def log_error(message):
    response = supabase.table("bot_logs").insert({
        "level": "ERROR",
        "message": message
    }).execute()

    return response.data
