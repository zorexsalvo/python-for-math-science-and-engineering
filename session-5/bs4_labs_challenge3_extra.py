from bs4 import BeautifulSoup
from IPython import embed
import re


def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <a href="/a.html"></a>
                <a href="/b.html"></a>
                <a href="/c.html"></a>
                <a href="/d.html"></a>
            
                <script>
                    var hello = "yoh";
                    alert(hello);
                </script>
            </body>
        
        </html>
    """


def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')
    pattern = re.compile(r'\w+ \w+ = "(.*?)";', re.MULTILINE)

    script = soup.find('script', text=pattern)
    print(pattern.search(script.text).group(1))


if __name__ == '__main__':
    main()
