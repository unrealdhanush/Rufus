from .parser import Parser

class Synthesizer:
    def __init__(self, instructions):
        self.instructions = instructions.lower()
        self.parser = Parser()

    def synthesize(self, pages):
        documents = []
        for page in pages:
            content = self.parser.parse(page['html'])
            if self.is_relevant(content):
                documents.append({
                    'url': page['url'],
                    'content': content,
                    'instructions': self.instructions
                })
        return documents

    def is_relevant(self, content):
        # Simple keyword matching for relevance; can be replaced with NLP models
        keywords = self.instructions.split()
        return any(keyword in content.lower() for keyword in keywords)
