import requests

url = "https://www.forexfactory.com/calendar"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)

print(response.status_code)
print(response.text[:500])
