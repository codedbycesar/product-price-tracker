import requests
from bs4 import BeautifulSoup

url = ""
headers = headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" }

try:
    response = requests.get(url, headers)
    soup = response.text

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
