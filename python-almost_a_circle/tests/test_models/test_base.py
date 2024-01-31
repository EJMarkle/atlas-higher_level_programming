#!/usr/bin/python3
"""Unit tests for 'Base' class methods'"""
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1, 'name': 'test'}]), '[{"id": 1, "name": "test"}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string('[{"id": 1, "name": "test"}]'), [{'id': 1, 'name': 'test'}])

    def tearDown(self):
        try:
            os.remove('Base.json')
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
    