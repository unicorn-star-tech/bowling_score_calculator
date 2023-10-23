import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))


from application.bowling_model import BowlingGameLogic


class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = BowlingGameLogic()

    def throw_many(self, n, pins):
        for i in range(n):
            self.g.throw(pins)

    def test_gutter_game(self):
        self.throw_many(20, 0)
        self.assertEqual(0, self.g.score())

    def test_all_ones(self):
        self.throw_many(20, 1)
        self.assertEqual(20, self.g.score())

    def test_one_spare(self):
        self.throw_spare()
        self.g.throw(3)
        self.throw_many(17, 0)
        self.assertEqual(16, self.g.score())

    def test_one_strike(self):
        self.throw_strike()
        self.g.throw(3)
        self.g.throw(4)
        self.throw_many(16, 0)
        self.assertEqual(24, self.g.score())

    def test_perfect_game(self):
        self.throw_many(12, 10)
        self.assertEqual(300, self.g.score())

    def throw_strike(self):
        self.g.throw(10)

    def throw_spare(self):
        self.g.throw(5)
        self.g.throw(5)


if __name__ == '__main__':
    unittest.main()
