#!/usr/bin/python3
"""
contains tests fir Base class
"""


import os
import unittest
from models import rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """tests the base class"""
    def test_args(self):
        """tests if there are too many args"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_no_args(self):
        """tests if there are no args"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique(self):
        self.assertEqual(2, Base(2).id)

    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)
