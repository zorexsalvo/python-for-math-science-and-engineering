import random
import requests

from IPython import embed
from time import sleep
from bs4 import BeautifulSoup

BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'

PAGES = [
    'group1/1.html', 'group1/2.html', 'group1/3.html', 'group1/4.html',
    'group1/5.html'
]


def delay(seconds):
    print(f'Sleeping for {seconds} second(s)')
    sleep(seconds)


def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text


def extract_target_value_from_page(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    div = soup.find(id='target')
    return div.get_text()


def get_random_number():
    return random.randint(1, 5)


def main():
    for page in PAGES:
        delay(get_random_number())
        html_doc = extract_html_content(BASE_URL + '/' + page)
        print(extract_target_value_from_page(html_doc))


if __name__ == '__main__':
    main()
