import argparse
import csv
import logging
import os
import requests

DATA_SOURCE = os.getenv(
    'DATA_SOURCE',
    'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'
)


def setup():
    """
    Downloads the 'products.csv'.
    """
    f = open('products.csv', 'wb')

    with f:
        response = requests.get(DATA_SOURCE)

        if response.status_code == 200:
            f.write(response.content)
            logging.info('OK!')

        else:
            logging.error(response.content)


def clean_products(reader):
    """
    Removes all products that don't have category.
    """
    for row in reader:
        if row[25]:
            yield row


def main(target=None):
    with open('products.csv', newline='') as file:
        reader = csv.reader(file)
        cleaned_products = clean_products(reader)

        if target:
            with open(target, 'w') as file:
                writer = csv.writer(file)
                for row in cleaned_products:
                    writer.writerow(row)
        else:
            for row in cleaned_products:
                print(', '.join(row))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', help='filename of the output file')
    parser.add_argument('--log-level',
                        '-log',
                        default='INFO',
                        help='set log verbosity')

    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)
    log = logging.getLogger(__name__)

    try:
        data_file = open('products.csv', 'r')
    except FileNotFoundError as err:
        logging.error(f'{err}: Fetching data...')
        setup()

    main(args.output)
