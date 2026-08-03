import requests
from bs4 import BeautifulSoup

url = "https://www.forexfactory.com/calendar"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

print(soup.title.text)
