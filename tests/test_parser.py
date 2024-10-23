import unittest
from core.parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_basic_html(self):
        html = "<html><body><p>Hello, World!</p></body></html>"
        text = self.parser.parse(html)
        self.assertEqual(text, "hello world")

    def test_parse_with_scripts(self):
        html = "<html><body><script>console.log('test');</script><p>Content here</p></body></html>"
        text = self.parser.parse(html)
        self.assertEqual(text, "content")

    def test_parse_with_main_content(self):
        html = "<html><body><main><p>Main content</p></main><p>Other content</p></body></html>"
        text = self.parser.parse(html)
        self.assertEqual(text, "main content")

    def test_parse_without_main(self):
        html = "<html><body><div class='content'><p>Content in div</p></div></body></html>"
        text = self.parser.parse(html)
        self.assertEqual(text, "content div")

if __name__ == '__main__':
    unittest.main()
