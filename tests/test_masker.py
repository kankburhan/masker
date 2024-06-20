import unittest
from masker import Masker

class TestMasker(unittest.TestCase):

    def setUp(self):
        self.masker = Masker()

    def test_start_keep_char_greater_than_word_length(self):
        word = 'hello'
        keep_char = 10
        expected_result = 'hello'
        result = self.masker.start(word, keep_char)
        self.assertEqual(result, expected_result)

    def test_start_keep_char_less_than_word_length(self):
        word = 'hello'
        keep_char = 2
        expected_result = '***lo'
        result = self.masker.start(word, keep_char)
        self.assertEqual(result, expected_result)

    def test_end_keep_char_greater_than_word_length(self):
        word = 'hello'
        keep_char = 10
        expected_result = 'hello'
        result = self.masker.end(word, keep_char)
        self.assertEqual(result, expected_result)

    def test_end_keep_char_less_than_word_length(self):
        word = 'hello'
        keep_char = 2
        expected_result = 'he***'
        result = self.masker.end(word, keep_char)
        self.assertEqual(result, expected_result)

    def test_mid_start_and_end_keep_char_greater_than_word_length(self):
        word = 'hello'
        start_keep_char = 10
        end_keep_char = 10
        expected_result = 'hello'
        result = self.masker.mid(word, start_keep_char, end_keep_char)
        self.assertEqual(result, expected_result)

    def test_mid_start_and_end_keep_char_less_than_word_length(self):
        word = 'hello'
        start_keep_char = 1
        end_keep_char = 1
        expected_result = 'h***o'
        result = self.masker.mid(word, start_keep_char, end_keep_char)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()