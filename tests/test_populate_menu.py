"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from utilities.miscellaneous import populate_menu


class TestPopulateMenu(TestCase):

    def test_populate_menu_list_strings(self):
        test_menu = ["First", "Second", "Third"]
        actual = populate_menu(test_menu)
        expected = {1: 'First', 2: 'Second', 3: 'Third'}
        self.assertEqual(actual, expected)

    def test_populate_menu_list_integers(self):
        test_menu = [1, 2, 3]
        actual = populate_menu(test_menu)
        expected = {1: 1, 2: 2, 3: 3}
        self.assertEqual(actual, expected)

    def test_populate_menu_list_floats(self):
        test_menu = [1.1, 2.2, 3.3]
        actual = populate_menu(test_menu)
        expected = {1: 1.1, 2: 2.2, 3: 3.3}
        self.assertEqual(actual, expected)

    def test_populate_menu_list_booleans(self):
        test_menu = [True, False, True]
        actual = populate_menu(test_menu)
        expected = {1: True, 2: False, 3: True}
        self.assertEqual(actual, expected)

    def test_populate_menu_list_none_type(self):
        test_menu = [None, None, None]
        actual = populate_menu(test_menu)
        expected = {1: None, 2: None, 3: None}
        self.assertEqual(actual, expected)

    def test_populate_menu_empty_list(self):
        test_menu = []
        actual = populate_menu(test_menu)
        expected = {}
        self.assertEqual(actual, expected)

    def test_populate_menu_is_one_item_still_a_list(self):
        test_menu = ["Shopping"]
        actual = populate_menu(test_menu)
        expected = {1: "Shopping"}
        self.assertEqual(actual, expected)

    def test_populate_menu_guess_im_writing_lines_at_this_point(self):
        test_menu = ["Alright", "So", "Here", "Is", "The", "Story", "Of", "How", "I", "Met", "Your", "Mother"]
        actual = populate_menu(test_menu)
        expected = {1: "Alright", 2: "So", 3: "Here", 4: "Is", 5: "The", 6: "Story", 7: "Of", 8: "How", 9: "I",
                    10: "Met", 11: "Your", 12: "Mother"}
        self.assertEqual(actual, expected)
