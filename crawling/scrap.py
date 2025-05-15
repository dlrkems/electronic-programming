import requests
from bs4 import BeautifulSoup

def scrap_test():
    print("scrap")

def get_current_price(code='005930'):
    """네이버 금융에서 주식의 현재가를 가져오는 함수"""
    url = f"https://finance.naver.com/item/main.naver?code={code}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price_tag = soup.select_one('p.no_today span.blind')
    if price_tag:
        return price_tag.text
    else:
        return "가격 정보 없음"
