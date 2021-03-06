import random
import requests

from bs4 import BeautifulSoup
from IPython import embed
from time import sleep
from functools import wraps

BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'

PAGES = [
    'group1/1.html', 'group1/2.html', 'group1/3.html', 'group1/4.html',
    'group1/5.html'
]


def get_random_number():
    return random.randint(1, 5)


def delay(seconds):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f'[START: delay]')
            print(f'Sleeping for {seconds} second(s)')

            sleep(seconds)
            output = function(*args, **kwargs)
            print(f'[END: delay]')
            return output

        return wrapper

    return inner_function


def debug_input_and_output(function):
    output = None

    def wrapper(*args, **kwargs):
        print(f'[START: {function.__name__}]')

        output = function(*args, **kwargs)

        print(f'[END: {function.__name__}]')
        return output

    return wrapper


class Scrapy(object):
    def __init__(self, url, *args, **kwargs):
        self.url = url

    @debug_input_and_output
    def extract_html_content(self):
        print(f'Downloading HTML content of {self.url}')
        response = requests.get(self.url)
        print(response.text)
        self.html_doc = response.text
        return response.text

    @delay(seconds=get_random_number())
    def extract_target_value_from_page(self):
        soup = BeautifulSoup(self.html_doc, 'html.parser')
        div = soup.find(id='target')
        return div.get_text()

    def perform(self):
        self.extract_html_content()
        print(self.extract_target_value_from_page())


def main():
    for page in PAGES:
        target_url = BASE_URL + '/' + page
        scrapy = Scrapy(target_url)
        scrapy.perform()


if __name__ == '__main__':
    main()
