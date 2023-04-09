"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.hades import ult_move
from unittest.mock import patch
import io


class TestEnemyAttack(TestCase):
    def test_ult_move_damage_dealt(self):
        test_player = {"Current HP": 100}
        test_enemy = {"name": "Hades", "atk": 5}
        ult_move(test_player, test_enemy, 0)
        actual = test_player["Current HP"]
        expected = 50
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ult_move_damage_dealt_print(self, mock_output):
        test_player = {"Current HP": 12}
        test_enemy = {"name": "Hades", "atk": 5}
        ult_move(test_player, test_enemy, 0)
        actual = mock_output.getvalue()
        expected = 'Hades unleashes all of his built-up energy!\nYou took 50 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_ult_move_training_dummy(self):
        test_player = {"Current HP": 10}
        test_enemy = {"name": "Dummy", "atk": 0}
        ult_move(test_player, test_enemy, 0)
        actual = test_player["Current HP"]
        expected = 10
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ult_move_training_dummy_print(self, mock_output):
        test_player = {"Current HP": 10}
        test_enemy = {"name": "Dummy", "atk": 0}
        ult_move(test_player, test_enemy, 0)
        actual = mock_output.getvalue()
        expected = 'Dummy unleashes all of his built-up energy!\nYou took 0 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_ult_move_death_comes(self):
        test_player = {"Current HP": 60}
        test_enemy = {"name": "Reaper", "atk": 6}
        ult_move(test_player, test_enemy, 0)
        actual = test_player["Current HP"]
        expected = 0
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ult_move_death_comes_print(self, mock_output):
        test_player = {"Current HP": 60}
        test_enemy = {"name": "Reaper", "atk": 6}
        ult_move(test_player, test_enemy, 0)
        actual = mock_output.getvalue()
        expected = 'Reaper unleashes all of his built-up energy!\nYou took 60 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_ult_move_that_looked_like_it_hurt(self):
        test_player = {"Current HP": 100}
        test_enemy = {"name": "Thanos", "atk": 20}
        ult_move(test_player, test_enemy, 0)
        actual = test_player["Current HP"]
        expected = -100
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ult_move_that_looked_like_it_hurt_print(self, mock_output):
        test_player = {"Current HP": 100}
        test_enemy = {"name": "Thanos", "atk": 20}
        ult_move(test_player, test_enemy, 0)
        actual = mock_output.getvalue()
        expected = 'Thanos unleashes all of his built-up energy!\nYou took 200 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_ult_move_blocking_does_not_heal(self):
        test_player = {"Current HP": 30}
        test_enemy = {"name": "Bunny", "atk": 0}
        ult_move(test_player, test_enemy, 5)
        actual = test_player["Current HP"]
        expected = 30
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ult_move_blocking_does_not_heal_print(self, mock_output):
        test_player = {"Current HP": 30}
        test_enemy = {"name": "Bunny", "atk": 0}
        ult_move(test_player, test_enemy, 5)
        actual = mock_output.getvalue()
        expected = 'Bunny unleashes all of his built-up energy!\nYou took 0 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_ult_move_enemies_cannot_heal_you(self):
        test_player = {"Current HP": 20}
        test_enemy = {"name": "Friend", "atk": -5}
        ult_move(test_player, test_enemy, 5)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ult_move_enemies_cannot_heal_you_print(self, mock_output):
        test_player = {"Current HP": 20}
        test_enemy = {"name": "Friend", "atk": -5}
        ult_move(test_player, test_enemy, 5)
        actual = mock_output.getvalue()
        expected = 'Friend unleashes all of his built-up energy!\nYou took 0 damage!\n\n'
        self.assertEqual(actual, expected)

    def test_ult_move_current_hp_not_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Got nothing": 20}
            test_enemy = {"name": "Hades", "atk": 5}
            ult_move(test_player, test_enemy, 1)

    def test_defend_atk_not_in_enemy(self):
        with self.assertRaises(KeyError):
            test_player = {"Current HP": 20}
            test_enemy = {"name": "Hades", "Whoops": 5}
            ult_move(test_player, test_enemy, 1)

    def test_defend_name_not_in_enemy(self):
        with self.assertRaises(KeyError):
            test_player = {"Current HP": 20}
            test_enemy = {"Hi Chris": "Hades", "atk": 5}
            ult_move(test_player, test_enemy, 1)

    def test_defend_no_number_in_current_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Current HP": "20"}
            test_enemy = {"name": "Hades", "atk": 5}
            ult_move(test_player, test_enemy, 1)

    def test_defend_no_number_in_atk(self):
        with self.assertRaises(TypeError):
            test_player = {"Current HP": 20}
            test_enemy = {"name": "Hades", "atk": "5"}
            ult_move(test_player, test_enemy, 1)
