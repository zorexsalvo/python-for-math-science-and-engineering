from bs4 import BeautifulSoup
from IPython import embed


def generate_html():
    return '''
        <html>
            <head></head>
            <body>
                <div id="target" data='1234'>Some Content</div>
                <div>A</div>
                <div>B</div>
                <div>C</div>
            </body>
        </html>
    '''


def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')
    div_elements = soup.find_all('div')

    for target in div_elements:
        print(target.get_text())


if __name__ == '__main__':
    main()
