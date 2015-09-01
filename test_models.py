import unittest

from etransport.app.models.coord import Coord


class TestCoord(unittest.TestCase):
    def setUp(self):
        self.num = '1'
        self.coord = [44, 55]
        self.type = 'bus'
        self.testunit = Coord(self.num, self.coord, self.type)

    def test_constructor(self):
        self.assertTrue(isinstance(self.testunit, Coord))

    def test_getter(self):
        self.assertEqual(self.testunit.num, self.num)
        self.assertEqual(self.testunit.coord, self.coord)
        self.assertEqual(self.testunit.type, self.type)

if __name__ == '__main__':
    unittest.main()
