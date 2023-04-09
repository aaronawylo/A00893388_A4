"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.battle_actions import enemy_attack
from unittest.mock import patch
import io


class TestEnemyAttack(TestCase):
    def test_enemy_attack_damage_dealt(self):
        test_player = {"Current HP": 12}
        test_enemy = {"name": "Slime", "atk": 2}
        enemy_attack(test_player, test_enemy, 1)
        actual = test_player["Current HP"]
        expected = 11
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_damage_dealt_print(self, mock_output):
        test_player = {"Current HP": 12}
        test_enemy = {"name": "Slime", "atk": 2}
        enemy_attack(test_player, test_enemy, 1)
        actual = mock_output.getvalue()
        expected = 'Slime has dealt 1 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_enemy_attack_training_dummy(self):
        test_player = {"Current HP": 10}
        test_enemy = {"name": "Dummy", "atk": 0}
        enemy_attack(test_player, test_enemy, 0)
        actual = test_player["Current HP"]
        expected = 10
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_training_dummy_print(self, mock_output):
        test_player = {"Current HP": 10}
        test_enemy = {"name": "Dummy", "atk": 0}
        enemy_attack(test_player, test_enemy, 0)
        actual = mock_output.getvalue()
        expected = 'Dummy has dealt 0 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_enemy_attack_death_comes(self):
        test_player = {"Current HP": 5}
        test_enemy = {"name": "Reaper", "atk": 5}
        enemy_attack(test_player, test_enemy, 0)
        actual = test_player["Current HP"]
        expected = 0
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_death_comes_print(self, mock_output):
        test_player = {"Current HP": 5}
        test_enemy = {"name": "Reaper", "atk": 5}
        enemy_attack(test_player, test_enemy, 0)
        actual = mock_output.getvalue()
        expected = 'Reaper has dealt 5 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_enemy_attack_that_looked_like_it_hurt(self):
        test_player = {"Current HP": 2}
        test_enemy = {"name": "Thanos", "atk": 20}
        enemy_attack(test_player, test_enemy, 0)
        actual = test_player["Current HP"]
        expected = -18
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_that_looked_like_it_hurt_print(self, mock_output):
        test_player = {"Current HP": 2}
        test_enemy = {"name": "Thanos", "atk": 20}
        enemy_attack(test_player, test_enemy, 0)
        actual = mock_output.getvalue()
        expected = 'Thanos has dealt 20 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_enemy_attack_blocking_does_not_heal(self):
        test_player = {"Current HP": 30}
        test_enemy = {"name": "Bunny", "atk": 0}
        enemy_attack(test_player, test_enemy, 5)
        actual = test_player["Current HP"]
        expected = 30
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_blocking_does_not_heal_print(self, mock_output):
        test_player = {"Current HP": 30}
        test_enemy = {"name": "Bunny", "atk": 0}
        enemy_attack(test_player, test_enemy, 5)
        actual = mock_output.getvalue()
        expected = 'Bunny has dealt 0 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_enemy_attack_enemies_cannot_heal_you(self):
        test_player = {"Current HP": 20}
        test_enemy = {"name": "Friend", "atk": -5}
        enemy_attack(test_player, test_enemy, 5)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_enemies_cannot_heal_you_print(self, mock_output):
        test_player = {"Current HP": 20}
        test_enemy = {"name": "Friend", "atk": -5}
        enemy_attack(test_player, test_enemy, 5)
        actual = mock_output.getvalue()
        expected = 'Friend has dealt 0 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_enemy_attack_current_hp_not_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Got nothing": 20}
            test_enemy = {"name": "Slime", "atk": 5}
            enemy_attack(test_player, test_enemy, 1)

    def test_defend_atk_not_in_enemy(self):
        with self.assertRaises(KeyError):
            test_player = {"Current HP": 20}
            test_enemy = {"name": "Slime", "Whoops": 5}
            enemy_attack(test_player, test_enemy, 1)

    def test_defend_name_not_in_enemy(self):
        with self.assertRaises(KeyError):
            test_player = {"Current HP": 20}
            test_enemy = {"Hi Chris": "Slime", "atk": 5}
            enemy_attack(test_player, test_enemy, 1)

    def test_defend_no_number_in_current_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Current HP": "20"}
            test_enemy = {"name": "Slime", "atk": 5}
            enemy_attack(test_player, test_enemy, 1)

    def test_defend_no_number_in_atk(self):
        with self.assertRaises(TypeError):
            test_player = {"Current HP": 20}
            test_enemy = {"name": "Slime", "atk": "5"}
            enemy_attack(test_player, test_enemy, 1)
