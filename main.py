import requests
from bs4 import BeautifulSoup
import datetime

def get_kospi():
    url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    kospi = soup.select_one("#now_value").text
    return kospi

kospi = get_kospi()
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
record = f"{current_date} : {kospi}"

with open("test.txt", "a") as file:
    file.write(record + "\n")
