import unittest
from Ball import Pos

class TestPosClass(unittest.TestCase):
    def test_eq(self):
        # TODO: setUp tearDown?
        original_point = Pos()
        unit_point = Pos(1, 1)
        self.assertEqual(original_point == original_point, True)
        self.assertEqual(original_point == unit_point, False)

    def test_add(self):
        original_point = Pos()
        unit_point = Pos(1, 1)
        self.assertEqual(original_point + unit_point, unit_point)

    def test_sub(self):
        original_point = Pos()
        unit_point = Pos(1, 1)
        self.assertEqual(unit_point - unit_point,  original_point)

    def test_mul(self):
        original_point = Pos()
        unit_point = Pos(1, 1)
        tt_point = Pos(3, 3)
        self.assertEqual(unit_point * 3,  tt_point)
        self.assertEqual(3 * unit_point,  tt_point)
        self.assertEqual(-3 * unit_point,  -tt_point)


class TestBallClass(unittest.TestCase):
    pass
class TestSpaceClass(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()