from .parser import Parser
from sentence_transformers import SentenceTransformer, util

class Synthesizer:
    def __init__(self, instructions, model_name='all-MiniLM-L6-v2', similarity_threshold=0.5):
        self.instructions = instructions
        self.parser = Parser()
        self.model = SentenceTransformer(model_name)
        self.instruction_embedding = self.model.encode(instructions, convert_to_tensor=True)
        self.similarity_threshold = similarity_threshold

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
        content_embedding = self.model.encode(content, convert_to_tensor=True)
        similarity = util.cos_sim(self.instruction_embedding, content_embedding)
        similarity_score = similarity.item()
        return similarity_score >= self.similarity_threshold
