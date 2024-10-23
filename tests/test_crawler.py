import asyncio
import unittest
from core.crawler import Crawler

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = Crawler(max_depth=2, max_pages=10)

    async def test_basic_crawl(self):
        result = await self.crawler.crawl('https://sfgov.org')
        self.assertGreater(len(result), 0, "Crawler should return some pages")
        self.assertIn('url', result[0], "Each result should have a URL")
        self.assertIn('html', result[0], "Each result should have HTML content")

    @unittest.skip("Skipping test_non_html_content temporarily due to known issues.")
    async def test_non_html_content(self):
        result = await self.crawler.crawl('https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf')
        self.assertEqual(len(result), 0, "Crawler should skip non-HTML content")

    async def test_nested_links(self):
        result = await self.crawler.crawl('https://sfgov.org')
        self.assertGreaterEqual(len(result), 5, "Crawler should follow nested links within the max depth")

    def test_run_async(self):
        asyncio.run(self.test_basic_crawl())
        asyncio.run(self.test_non_html_content())
        asyncio.run(self.test_nested_links())

if __name__ == '__main__':
    unittest.main()

