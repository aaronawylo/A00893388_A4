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

    def test_attack_no_level_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"forgot I can get stronger": 2, "atk": 3}
            test_enemy = {"hp": 5}
            attack(test_player, test_enemy)

    def test_attack_no_attack_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"level": 2, "I have a wet noodle": 3}
            test_enemy = {"hp": 5}
            attack(test_player, test_enemy)

    def test_attack_no_hp_in_enemy(self):
        with self.assertRaises(KeyError):
            test_player = {"level": 2, "atk": 3}
            test_enemy = {"Just Shadow Boxing": 5}
            attack(test_player, test_enemy)

    def test_attack_no_number_in_level(self):
        with self.assertRaises(TypeError):
            test_player = {"level": "oops", "atk": 3}
            test_enemy = {"hp": 5}
            attack(test_player, test_enemy)

    def test_attack_no_number_in_atk(self):
        with self.assertRaises(TypeError):
            test_player = {"level": 2, "atk": "my bad"}
            test_enemy = {"hp": 5}
            attack(test_player, test_enemy)

    def test_attack_no_number_in_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"level": 2, "atk": 3}
            test_enemy = {"hp": "I'm a moron"}
            attack(test_player, test_enemy)
