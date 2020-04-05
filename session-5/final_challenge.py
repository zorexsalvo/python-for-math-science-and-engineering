import random
import requests

from bs4 import BeautifulSoup
from bs4.element import Tag
from IPython import embed
from time import sleep
from functools import wraps

BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'


def get_random_number():
    return random.randint(1, 2)


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


class Scrapy(object):
    def __init__(self, url, *args, **kwargs):
        self.url = url

    def extract_html_content(self):
        print(f'Downloading HTML content of {self.url}')
        response = requests.get(self.url)
        self.html_doc = response.text

    @delay(seconds=get_random_number())
    def extract_list_from_html_content(self):
        soup = BeautifulSoup(self.html_doc, 'html.parser')
        configuration_list = soup.find_all('ul')
        return configuration_list

    def perform(self):
        self.extract_html_content()
        config_list = self.extract_list_from_html_content()

        for item in config_list[0].contents:
            if isinstance(item, Tag):
                print(item.get_text().strip().replace('\n',
                                                      '').replace('\t', ''))


def main():
    target_url = BASE_URL + '/group3/target.html'

    scrapy = Scrapy(target_url)
    scrapy.perform()


if __name__ == '__main__':
    main()
