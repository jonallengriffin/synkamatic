#!/usr/bin/env python

"""
unit tests
"""

import os
import sys
import unittest

# globals
here = os.path.dirname(os.path.abspath(__file__))

class SynkamaticUnitTest(unittest.TestCase):

    def test_synkamatic(self):
        pass

    def test_pullrequest(self):
        """test github pull requests"""


if __name__ == '__main__':
    unittest.main()

