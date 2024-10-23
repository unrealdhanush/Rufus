import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup, Comment

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

class Parser:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Remove unwanted elements
        for element in soup(['script', 'style', 'header', 'footer', 'nav', 'aside', 'form', 'noscript']):
            element.decompose()

        # Remove comments
        for comment in soup.findAll(string=lambda string: isinstance(string, Comment)):
            comment.extract()

        # Extract main content
        main_content = soup.find('main')
        if main_content:
            text = main_content.get_text(separator=' ', strip=True)
        else:
            body_content = soup.find('body')
            if body_content:
                text = body_content.get_text(separator=' ', strip=True)
            else:
                text = soup.get_text(separator=' ', strip=True)

        # Preprocess text
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        processed_text = ' '.join(tokens)

        return processed_text.strip()
