from database.supabase_client import supabase


def log_info(message):
    try:
        response = (
            supabase
            .table("bot_logs")
            .insert({
                "level": "INFO",
                "message": message
            })
            .execute()
        )

        return response.data

    except Exception as e:
        print(f"LOGGER ERROR: {e}")
        return None


def log_error(message):
    try:
        response = (
            supabase
            .table("bot_logs")
            .insert({
                "level": "ERROR",
                "message": message
            })
            .execute()
        )

        return response.data

    except Exception as e:
        print(f"LOGGER ERROR: {e}")
        return None
