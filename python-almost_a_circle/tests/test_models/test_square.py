#!/usr/bin/python3
"""Unit tests for 'Square' class methods """
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_exists(self):
        # Test cases for Square(1), Square(1, 2), Square(1, 2, 3), etc.
        square1 = Square(1)
        self.assertIsInstance(square1, Square)

        square2 = Square(1, 2)
        self.assertIsInstance(square2, Square)

        square3 = Square(1, 2, 3)
        self.assertIsInstance(square3, Square)

        # Add more test cases as needed

    def test_square_invalid_arguments(self):
        # Test cases for invalid arguments like Square("1"), Square(1, "2"), etc.
        with self.assertRaises(TypeError):
            invalid_square1 = Square("1")

        with self.assertRaises(TypeError):
            invalid_square2 = Square(1, "2")

        # Add more test cases as needed

    def test_str_method_exists(self):
        # Test __str__() method for Square
        square = Square(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 1")

    def test_to_dictionary_method_exists(self):
        # Test to_dictionary() method for Square
        square = Square(1, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_update_method_exists(self):
        # Test update() method for Square
        square = Square(1, 2, 3, 4)
        square.update(5, 6, 7, 8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_with_kwargs_exists(self):
        # Test update() method with kwargs for Square
        square = Square(1, 2, 3, 4)
        square.update(id=5, size=6, x=7, y=8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_create_method_exists(self):
        # Test create() method for Square
        square_dict = {'id': 5, 'size': 6, 'x': 7, 'y': 8}
        created_square = Square.create(**square_dict)
        self.assertIsInstance(created_square, Square)
        self.assertEqual(created_square.id, 5)
        self.assertEqual(created_square.size, 6)
        self.assertEqual(created_square.x, 7)
        self.assertEqual(created_square.y, 8)

    def test_save_to_file_method_exists(self):
        # Test save_to_file() method for Square
        square = Square(1, 2, 3, 4)
        Square.save_to_file([square])
        self.assertTrue(os.path.isfile("Square.json"))

    def test_load_from_file_method_exists(self):
        # Test load_from_file() method for Square
        square = Square(1, 2, 3, 4)
        Square.save_to_file([square])
        loaded_squares = Square.load_from_file()
        self.assertIsInstance(loaded_squares, list)
        self.assertEqual(len(loaded_squares), 1)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertEqual(loaded_squares[0].id, 4)

if __name__ == '__main__':
    unittest.main()