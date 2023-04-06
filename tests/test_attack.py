"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.battle_actions import attack
from unittest.mock import patch
import io


class TestAttack(TestCase):
    def test_attack_return_no_guard(self):
        test_player = {"level": 1, "atk": 2}
        test_enemy = {"hp": 3}
        actual = attack(test_player, test_enemy)
        expected = 0
        self.assertEqual(actual, expected)

    def test_attack_enemy_health_correct(self):
        test_player = {"level": 2, "atk": 4}
        test_enemy = {"hp": 10}
        attack(test_player, test_enemy)
        actual = test_enemy["hp"]
        expected = 2
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_print_output(self, mock_output):
        test_player = {"level": 3, "atk": 6}
        test_enemy = {"hp": 20}
        attack(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You have dealt 18 damage!\n'
        self.assertEqual(actual, expected)

    def test_attack_go_to_the_gym_enemy_health(self):
        test_player = {"level": 1, "atk": 0}
        test_enemy = {"hp": 3}
        attack(test_player, test_enemy)
        actual = test_enemy["hp"]
        expected = 3
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_go_to_the_gym_print(self, mock_output):
        test_player = {"level": 1, "atk": 0}
        test_enemy = {"hp": 16}
        attack(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You have dealt 0 damage!\n'
        self.assertEqual(actual, expected)

    def test_attack_why_are_you_healing_them(self):
        test_player = {"level": 4, "atk": -3}
        test_enemy = {"hp": 3}
        attack(test_player, test_enemy)
        actual = test_enemy["hp"]
        expected = 15
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_why_are_you_healing_them_print(self, mock_output):
        test_player = {"level": 4, "atk": -3}
        test_enemy = {"hp": 3}
        attack(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You have dealt -12 damage!\n'
        self.assertEqual(actual, expected)

    def test_attack_how_is_your_level_negative(self):
        test_player = {"level": -2, "atk": 3}
        test_enemy = {"hp": 4}
        attack(test_player, test_enemy)
        actual = test_enemy["hp"]
        expected = 10
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_how_is_your_level_negative_print(self, mock_output):
        test_player = {"level": -2, "atk": 3}
        test_enemy = {"hp": 5}
        attack(test_player, test_enemy)
        actual = mock_output.getvalue()
        expected = 'You have dealt -6 damage!\n'
        self.assertEqual(actual, expected)
