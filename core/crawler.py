import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging
import ssl
import certifi

logger = logging.getLogger(__name__)

class Crawler:
    def __init__(self, max_depth=2, max_pages=100):
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.visited = set()
        self.pages = []
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())

    async def fetch(self, session, url):
        try:
            async with session.get(url, ssl=None, timeout=10) as response:
                if response.status == 200 and 'text/html' in response.headers.get('Content-Type', ''):
                    text = await response.text()
                    return text
                else:
                    print(f"Skipped non-HTML content at {url}")
        except aiohttp.ClientConnectorCertificateError as e:
            print(f"SSL certificate error when fetching {url}: {e}")
            return ''
        except aiohttp.ClientConnectorSSLError as e:
            print(f"SSL error when fetching {url}: {e}")
            return ''
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            return ''
        return ''

    async def crawl(self, start_url):
        async with aiohttp.ClientSession() as session:
            await self._crawl(session, start_url, depth=0)
        return self.pages

    async def _crawl(self, session, url, depth):
        if depth > self.max_depth or len(self.visited) >= self.max_pages:
            return
        if url in self.visited:
            return
        self.visited.add(url)
        print(f"Crawling: {url}")

        html = await self.fetch(session, url)
        if not html:
            return

        self.pages.append({'url': url, 'html': html})
        soup = BeautifulSoup(html, 'html.parser')
        tasks = []
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            if urlparse(next_url).netloc != urlparse(url).netloc:
                continue  # Skip external links
            tasks.append(self._crawl(session, next_url, depth + 1))
        await asyncio.gather(*tasks)
