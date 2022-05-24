#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """ Defines unit testing for max_integer function """

    def test_max_int(self):
        self.assertAlmostEqual(max_integer([2, 4, 3, 1]), 4)
        self.assertAlmostEqual(max_integer([2, 3, 3, 1]), 3)
        self.assertAlmostEqual(max_integer([2, -4, 3, 1]), 3)
        self.assertAlmostEqual(max_integer([-2, -4, -3, -1]), -1)
        self.assertAlmostEqual(max_integer([-2, 0]), 0)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([3.5, 2, 1]), 3.5)

    def test_errors(self):
        self.assertAlmostEqual(max_integer("hello"), "o")
        self.assertAlmostEqual(max_integer(["hello"]), "hello")
        self.assertRaises(TypeError, max_integer, [2, "hello"])
