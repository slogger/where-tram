import unittest

from etransport.app.libs.google_geo_decode import decode


class TestDecode(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(decode('_p~iF~ps|U'), [(38.5, -120.2)])

if __name__ == '__main__':
    unittest.main()
