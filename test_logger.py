from database.supabase_client import supabase

response = supabase.table("bot_logs").select("*").limit(1).execute()

print("SUPABASE TEST")
print(response.data)
