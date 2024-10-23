from .parser import Parser
from sentence_transformers import SentenceTransformer, util

class Synthesizer:
    def __init__(self, instructions, model_name='stsb-roberta-large', similarity_threshold=0.8):
        self.instructions = instructions
        self.model = SentenceTransformer(model_name)
        self.similarity_threshold = similarity_threshold
        self.instruction_embedding = self.model.encode(
            instructions, convert_to_tensor=True, normalize_embeddings=True)
        self.parser = Parser()

    def is_relevant(self, content):
        content_embedding = self.model.encode(content, convert_to_tensor=True, normalize_embeddings=True)
        similarity_score = util.pytorch_cos_sim(self.instruction_embedding, content_embedding)[0][0].item()
        print(f"Similarity Score: {similarity_score}")
        return similarity_score >= self.similarity_threshold

    def synthesize(self, pages):
        documents = []
        contents = []
        valid_pages = []
        for page in pages:
            content = self.parser.parse(page['html'])
            if content:
                contents.append(content)
                valid_pages.append(page)

        if not contents:
            return documents

        content_embeddings = self.model.encode(
            contents, batch_size=8, convert_to_tensor=True, normalize_embeddings=True)
        similarities = util.pytorch_cos_sim(self.instruction_embedding, content_embeddings)[0]

        for idx, similarity_score in enumerate(similarities):
            score = similarity_score.item()
            url = valid_pages[idx]['url']
            print(f"URL: {url} | Similarity Score: {score}")
            if score >= self.similarity_threshold:
                documents.append({
                    'url': url,
                    'content': contents[idx],
                    'instructions': self.instructions
                })

        return documents
