import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_kospi():
    url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    kospi = soup.select_one('#now_value').text
    return kospi

def write_to_file(kospi):
    with open('test.txt', 'a') as f:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{now}: {kospi}\n')

def main():
    kospi = get_kospi()
    write_to_file(kospi)

main()
