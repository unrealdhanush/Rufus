import os
from .crawler import Crawler
from .synthesizer import Synthesizer

class RufusClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('RUFUS_API_KEY')
        if not self.api_key:
            raise ValueError("API key is required")
        # Additional authentication setup if needed

    async def scrape(self, url, instructions, max_depth=2, max_pages=100):
        crawler = Crawler(max_depth=max_depth, max_pages=max_pages)
        pages = await crawler.crawl(url)
        synthesizer = Synthesizer(instructions)
        documents = synthesizer.synthesize(pages)
        return documents
