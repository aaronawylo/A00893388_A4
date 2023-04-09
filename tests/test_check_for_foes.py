"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from unittest.mock import patch

from utilities.miscellaneous import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.randint', return_value=1)
    def test_check_for_foes_pseudo_one(self, _):
        self.assertEqual(True, check_for_foes())

    @patch('random.randint', return_value=2)
    def test_check_for_foes_pseudo_two(self, _):
        self.assertEqual(False, check_for_foes())

    @patch('random.randint', return_value=3)
    def test_check_for_foes_pseudo_three(self, _):
        self.assertEqual(False, check_for_foes())

    @patch('random.randint', return_value=4)
    def test_check_for_foes_pseudo_four(self, _):
        self.assertEqual(False, check_for_foes())
