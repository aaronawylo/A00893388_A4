"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from unittest.mock import patch


from Movement.movement import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_input_one(self, _):
        actual = get_user_choice()
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_input_two(self, _):
        actual = get_user_choice()
        expected = 2
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_input_three(self, _):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_input_four(self, _):
        actual = get_user_choice()
        expected = 4
        self.assertEqual(actual, expected)
