#!/usr/bin/python3
"""Unit tests for 'Rectangle' class methods"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 1/2 - 4/5")

    def test_display_without_x_y(self):
        r = Rectangle(2, 3)
        r.display()

    def test_display_without_y(self):
        r = Rectangle(2, 3, 1)
        r.display()

    def test_display_exists(self):
        r = Rectangle(2, 3, 1, 2)
        r.display()

    def test_to_dictionary(self):
        r = Rectangle(4, 5, 1, 2, 7)
        expected_dict = {'id': 7, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_update(self):
        r = Rectangle(4, 5, 1, 2, 7)
        r.update(8)
        self.assertEqual(r.id, 8)

        r.update(8, 9)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)

        r.update(8, 9, 10)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 10)

        r.update(8, 9, 10, 11)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 11)

        r.update(8, 9, 10, 11, 12)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 11)
        self.assertEqual(r.y, 12)

        with self.assertRaises(ValueError):
            r.update(8, 9, -10, 11, 12)

        with self.assertRaises(ValueError):
            r.update(8, 9, 10, -11, 12)

    def test_update_with_kwargs(self):
        r = Rectangle(4, 5, 1, 2, 7)
        r.update(id=8)
        self.assertEqual(r.id, 8)

        r.update(id=8, width=9)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)

        r.update(id=8, width=9, height=10)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 10)

        r.update(id=8, width=9, height=10, x=11)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 11)

        r.update(id=8, width=9, height=10, x=11, y=12)

if __name__ == '__main__':
    unittest.main()
