import unittest
from core.synthesizer import Synthesizer

class TestSynthesizer(unittest.TestCase):
    def setUp(self):
        instructions = "Extract information about policies and benefits."
        self.synthesizer = Synthesizer(instructions)

    def test_relevance_basic(self):
        content = "This article discusses financial data, policies and benefits"
        relevance = self.synthesizer.is_relevant(content)
        self.assertTrue(relevance, "The content should be considered relevant based on instructions")

    def test_non_relevant_content(self):
        content = "This article is about cooking recipes."
        relevance = self.synthesizer.is_relevant(content)
        self.assertFalse(relevance, "The content should be considered non-relevant based on instructions")

    def test_similarity_threshold(self):
        self.synthesizer.similarity_threshold = 0.1  # Set a lower threshold
        content = "Somewhat related financial information."
        relevance = self.synthesizer.is_relevant(content)
        self.assertTrue(relevance, "The content should pass with a lower threshold")

if __name__ == '__main__':
    unittest.main()
