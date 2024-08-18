import unittest
 
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')
    def test_multiple_words(self):
        text = 'this is a test'
        result = cap.cap_text(text)
        self.assertEqual(result,'This Is A Test')


if __name__ == '__main__':
    unittest.main()