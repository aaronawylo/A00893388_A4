"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from utilities.miscellaneous import menu_print
from unittest.mock import patch
import io


class TestMenuPrint(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print_one_pair(self, mock_output):
        test_menu = {"Test": "Case"}
        menu_print(test_menu)
        actual = mock_output.getvalue()
        expected = "Test: Case\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print_two_pairs(self, mock_output):
        test_menu = {"This": "Is", "A": "Menu"}
        menu_print(test_menu)
        actual = mock_output.getvalue()
        expected = "This: Is\nA: Menu\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print_works_with_integers(self, mock_output):
        test_menu = {1: 2, 3: 4}
        menu_print(test_menu)
        actual = mock_output.getvalue()
        expected = "1: 2\n3: 4\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print_works_with_floats(self, mock_output):
        test_menu = {1.1: 2.2, 3.3: 4.4}
        menu_print(test_menu)
        actual = mock_output.getvalue()
        expected = "1.1: 2.2\n3.3: 4.4\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print_works_with_booleans(self, mock_output):
        test_menu = {True: True, False: False}
        menu_print(test_menu)
        actual = mock_output.getvalue()
        expected = "True: True\nFalse: False\n"
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print_works_with_none(self, mock_output):
        test_menu = {None: None}
        menu_print(test_menu)
        actual = mock_output.getvalue()
        expected = "None: None\n"
        self.assertEqual(actual, expected)
