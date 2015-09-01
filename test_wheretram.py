import unittest

from etransport.app.libs.where_tram import where_tram


class TestDecode(unittest.TestCase):
    def setUp(self):
        self.responce = where_tram('3416')

    def test_responcetype(self):
        self.assertTrue(isinstance(self.responce, list))

if __name__ == '__main__':
    unittest.main()
