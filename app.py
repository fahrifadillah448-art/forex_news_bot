import requests

response = requests.post(
    "https://ntfy.sh/forex_pai_2026",
    data="TEST DARI GITHUB ACTIONS"
)

print(response.status_code)
print(response.text)
