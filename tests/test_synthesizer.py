import unittest
from core.synthesizer import Synthesizer

class TestSynthesizer(unittest.TestCase):
    def setUp(self):
        instructions = "Extract information about policies and benefits."
        self.synthesizer = Synthesizer(instructions)

    def test_relevance_basic(self):
        html = "<html><body><p>This page contains information about employee benefits.</p></body></html>"
        content = self.synthesizer.parser.parse(html)
        relevance = self.synthesizer.is_relevant(content, "https://example.com")
        self.assertTrue(relevance, "The content should be considered relevant based on instructions")

    def test_non_relevant_content(self):
        html = "<html><body><p>Random unrelated content here.</p></body></html>"
        content = self.synthesizer.parser.parse(html)
        relevance = self.synthesizer.is_relevant(content, "https://example.com")
        self.assertFalse(relevance, "The content should be considered non-relevant based on instructions")

    def test_similarity_threshold(self):
        self.synthesizer.similarity_threshold = 0.5  # Set a lower threshold
        html = "<html><body><p>Partial match for policies and some benefits information.</p></body></html>"
        content = self.synthesizer.parser.parse(html)
        relevance = self.synthesizer.is_relevant(content, "https://example.com")
        self.assertTrue(relevance, "The content should pass with a lower threshold")

if __name__ == '__main__':
    unittest.main()
