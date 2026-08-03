from notify import send_notification

title = "Forex Intelligence Bot"

message = """
🚨 HIGH IMPACT TEST

🇺🇸 US CPI

🕗 20:30 WIB

Forecast : 2.8%
Previous : 2.7%

━━━━━━━━━━━━━━

Bot berhasil mengirim format profesional.
"""

send_notification(title, message)

print("Done")
