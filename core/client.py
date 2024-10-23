import os
from dotenv import load_dotenv
from .crawler import Crawler
from .synthesizer import Synthesizer

load_dotenv()

class RufusClient:
    def __init__(self, api_key=None):
        self.api_key = 'temp_key' or os.getenv('RUFUS_API_KEY')
        if not self.api_key:
            raise ValueError("API key is required")

    async def scrape(self, url, instructions, max_depth=2, max_pages=100):
        crawler = Crawler(max_depth=max_depth, max_pages=max_pages)
        pages = await crawler.crawl(url)
        print(f"Crawled {len(pages)} pages.")
        synthesizer = Synthesizer(instructions, similarity_threshold=0.2)
        documents = synthesizer.synthesize(pages)
        print(f"Synthesized {len(documents)} documents.")
        return documents
