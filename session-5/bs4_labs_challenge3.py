from bs4 import BeautifulSoup
from IPython import embed


def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <a href="/a.html"></a>
                <a href="/b.html"></a>
                <a href="/c.html"></a>
                <a href="/d.html"></a>
            </body>
        
        </html>
    """


def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')
    anchor_elements = soup.find_all('a')

    for element in anchor_elements:
        print(element['href'])


if __name__ == '__main__':
    main()
