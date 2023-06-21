#!/usr/bin/python3
# test_square.py
"""
This module contains unit tests for the Square class.
Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""

import sys
import io
import unittest
from models.square import Square
from models.base import Base


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4)._Square__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquareSize(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_display_size_x_y(self):
        s = Square(4, 2, 3, 22)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("\n\n  ####\n  ####\n  ####\n", capture.getvalue())

    def test_display_changed_attributes(self):
        s = Square(3, 1, 1, 7)
        s.size = 5
        s.x = 2
        s.y = 2
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("\n\n  #####\n  #####\n  #####\n  #####\n  #####\n", capture.getvalue())

    def test_display_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing the update method with *args of the Square class."""

    def test_no_args(self):
        s = Square(5, 5, 5, 5)
        s.update()
        self.assertEqual("[Square] (5) 5/5 - 5", str(s))

    def test_one_arg(self):
        s = Square(5, 5, 5, 5)
        s.update(10)
        self.assertEqual("[Square] (10) 5/5 - 5", str(s))

    def test_two_args(self):
        s = Square(5, 5, 5, 5)
        s.update(10, 2)
        self.assertEqual("[Square] (10) 5/5 - 2", str(s))

    def test_three_args(self):
        s = Square(5, 5, 5, 5)
        s.update(10, 2, 3)
        self.assertEqual("[Square] (10) 3/5 - 2", str(s))

    def test_four_args(self):
        s = Square(5, 5, 5, 5)
        s.update(10, 2, 3, 4)
        self.assertEqual("[Square] (10) 3/4 - 2", str(s))

    def test_more_than_four_args(self):
        s = Square(5, 5, 5, 5)
        s.update(10, 2, 3, 4, 5)
        self.assertEqual("[Square] (10) 3/4 - 2", str(s))

    def test_negative_size(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(10, -2)
        self.assertEqual("[Square] (10) 5/5 - 5", str(s))

    def test_zero_size(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(10, 0)
        self.assertEqual("[Square] (10) 5/5 - 5", str(s))

    def test_negative_x(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(10, 2, -3)
        self.assertEqual("[Square] (10) 5/5 - 5", str(s))

    def test_negative_y(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(10, 2, 3, -4)
        self.assertEqual("[Square] (10) 5/5 - 5", str(s))


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing the update method with **kwargs of the Square class."""

    def test_no_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update()
        self.assertEqual("[Square] (5) 5/5 - 5", str(s))

    def test_one_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(id=10)
        self.assertEqual("[Square] (10) 5/5 - 5", str(s))

    def test_two_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(id=10, size=2)
        self.assertEqual("[Square] (10) 5/5 - 2", str(s))

    def test_three_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(id=10, size=2, x=3)
        self.assertEqual("[Square] (10) 3/5 - 2", str(s))

    def test_four_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(id=10, size=2, x=3, y=4)
        self.assertEqual("[Square] (10) 3/4 - 2", str(s))

    def test_invalid_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(id=10, width=2, height=3)
        self.assertEqual("[Square] (10) 5/5 - 5", str(s))


if __name__ == '__main__':
    unittest.main()
