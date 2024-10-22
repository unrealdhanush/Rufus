from bs4 import BeautifulSoup

class Parser:
    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Remove scripts and styles
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        # Get text
        text = soup.get_text(separator=' ', strip=True)
        return text
