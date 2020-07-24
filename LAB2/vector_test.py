import unittest
from vector import Vector
from vector import Errors


class TestVector(unittest.TestCase):

    def test_correct_add(self):
        a = Vector(-5, 10, 7)
        b=Vector(2, 4, 2)
        self.assertTrue(a+b==Vector(-3, 14, 9))

    def test_correct_sub(self):
        a = Vector(-5, 10, 7)
        b = Vector(2, 4, 2)
        self.assertTrue(a - b == Vector(-7, 6, 5))

    def test_incorrect_add(self):
        a = Vector(-5, 10, 7)
        b = Vector(2, 4)
        with self.assertRaises(Errors):
            a + b

    def test_correct_prod(self):
        a = Vector(-5, 10, 7)
        b = Vector(2, 4, 2)
        self.assertTrue(a * b == 44)

    def test_incorrect_prod(self):
        a = Vector(-5, 10, 7)
        b = Vector(2, 4)
        with self.assertRaises(Errors):
            a * b

    def test_correct_const_prod(self):
        a = Vector(-5, 10, 7)
        a *= 2
        self.assertTrue(a == Vector(-10, 20, 14))

    def test_correct_const_division(self):
        a = Vector(-5, 10, 7)
        a /= 2
        self.assertTrue(a == Vector(-2.5, 5, 3.5))

    def test_incorrect_const_division(self):
        a = Vector(-5, 10, 7)
        with self.assertRaises(Errors):
            a/=0

    def test_abs(self):
        a = Vector(-5, 10, 7)
        self.assertTrue(abs(a) == 13.19090595827292)

    def test_correct_eq(self):
        a = Vector(-5, 10, 7)
        b = Vector(-5, 10, 7)
        self.assertTrue(a == b)

    def test_incorrect_eq(self):
        a = Vector(-5, 10, 7)
        b = Vector(-5, 10, 7, 11)
        with self.assertRaises(Errors):
            self.assertTrue(a == b)

    def test_correct_getitem(self):
        a = Vector(-5, 10, 7)
        self.assertTrue(a[1] == 10)

    def test_incorrect_getitem(self):
        a = Vector(-5, 10, 7)
        with self.assertRaises(Errors):
            self.assertTrue(a[5])


if __name__ == '__main__':
    unittest.main()
