"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.fight import potion_check
from unittest.mock import patch
import io


class TestPotionCheck(TestCase):

    def test_potion_check_without_key(self):
        with self.assertRaises(KeyError):
            test_player = {"Why didn't I make a better character?": "I should be better next time."}
            potion_check(test_player, '3')

    def test_character_potion_check_positive_potions_no_drinking(self):
        test_player = {"potions": 1}
        actual = potion_check(test_player, '3')
        expected = True
        self.assertEqual(actual, expected)

    def test_character_potion_check_no_more_potions_not_thirsty_boolean(self):
        test_player = {"potions": 2}
        actual = potion_check(test_player, '3')
        expected = True
        self.assertEqual(actual, expected)

    def test_character_potion_check_positive_potions_use_potion(self):
        test_player = {"potions": 3}
        actual = potion_check(test_player, '3')
        expected = True
        self.assertEqual(actual, expected)

    def test_character_potion_check_no_more_potions_use_potion_boolean(self):
        test_player = {"potions": 0}
        actual = potion_check(test_player, '3')
        expected = False
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_potion_check_no_more_potions_print_check(self, mock_output):
        test_player = {"potions": 0}
        potion_check(test_player, '3')
        actual = mock_output.getvalue()
        expected = "You're out of potions! Do something else!\n"
        self.assertEqual(actual, expected)

