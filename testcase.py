import unittest
import breakoutroom

key = list(breakoutroom.json_data.keys())[0]

class TestStringMethods(unittest.TestCase):

    def test_key(self):
        self.assertEqual(key,"ip")

if __name__ == '__main__':
    unittest.main()
