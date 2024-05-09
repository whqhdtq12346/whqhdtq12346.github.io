import requests
from bs4 import BeautifulSoup

def get_kospi():
    url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    kospi = soup.select_one("#now_value").text
    return kospi

print(get_kospi())
