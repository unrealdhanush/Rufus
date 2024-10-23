import asyncio
import unittest
import json
from core.client import RufusClient
from dotenv import load_dotenv
import os

class TestRufusIntegration(unittest.TestCase):
    def setUp(self):
        load_dotenv()  # Load environment variables
        api_key = 'testkey' or os.getenv('RUFUS_API_KEY')
        self.client = RufusClient(api_key=api_key)

    def test_full_integration(self):
        asyncio.run(self.run_full_integration())

    async def run_full_integration(self):
        instructions = "Extract information on government policies and services."
        documents = await self.client.scrape(
            "https://sfgov.org",
            instructions=instructions,
            max_depth=2,
            max_pages=100
        )
        self.assertGreater(len(documents), 0, "Rufus should return some documents")
        self.assertIn('url', documents[0], "Each document should contain a URL")
        self.assertIn('content', documents[0], "Each document should contain extracted content")

        # Test output format
        with open('tests/test_output.json', 'w') as f:
            json.dump(documents, f, indent=2)

        with open('tests/test_output.json', 'r') as f:
            data = json.load(f)
            self.assertIsInstance(data, list, "Output should be a list of documents")
            self.assertGreater(len(data), 0, "JSON file should contain documents")

    def test_run_async(self):
        self.test_full_integration()
        
if __name__ == '__main__':
    unittest.main()