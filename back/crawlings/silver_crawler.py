# silver_crawler.py
import requests
from bs4 import BeautifulSoup

def get_silver_price():
    url = "https://finance.naver.com/marketindex/?tabSel=silver"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    silver_price = soup.select_one(".value").text.strip()
    return silver_price

if __name__ == "__main__":
    price = get_silver_price()
    print(f"현재 은 시세: {price} 원/그램")
