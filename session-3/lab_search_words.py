import argparse

parser = argparse.ArgumentParser(
    description='Search for the words including partial word')
parser.add_argument('snippet',
                    help='partial (or complete) string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

matches = []

print([word for word in words if snippet in word.lower()])
