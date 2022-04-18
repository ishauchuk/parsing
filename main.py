import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='beautiful-soup-documentation').find('h1').text
    return h1


def main():
    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
