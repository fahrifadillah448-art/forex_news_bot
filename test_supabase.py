from database.supabase_client import supabase

response = supabase.table("sent_events").select("*").execute()

print(response.data)
