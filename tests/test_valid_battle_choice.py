"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.normal_fight import valid_battle_choice
from unittest.mock import patch
import io


class TestValidBattleChoice(TestCase):
    def test_valid_battle_choice(self):
        test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
        actual = valid_battle_choice(test_menu, "1")
        expected = True
        self.assertEqual(actual, expected)

    def test_valid_battle_choice_not_in_menu_boolean(self):
        test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
        actual = valid_battle_choice(test_menu, "4")
        expected = False
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_battle_choice_not_in_menu_print(self, mock_output):
        test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
        valid_battle_choice(test_menu, "4")
        actual = mock_output.getvalue()
        expected = "That is not a valid numeric choice, please select from the following:\n"
        self.assertEqual(actual, expected)

    def test_valid_battle_choice_not_valid_choice_boolean(self):
        test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
        actual = valid_battle_choice(test_menu, "Still can't read instructions")
        expected = False
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_battle_choice_not_valid_choice_print(self, mock_output):
        test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
        valid_battle_choice(test_menu, "Still can't read instructions")
        actual = mock_output.getvalue()
        expected = "That is not a valid numeric choice, please select from the following:\n"
        self.assertEqual(actual, expected)
