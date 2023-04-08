"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import fire_room

class TestPotionRoom(TestCase):
    def test_fire_room_normal(self):
        test_player = {"Current HP": 10}
        fire_room(test_player)
        actual = test_player["Current HP"]
        expected = 5
        self.assertEqual(actual, expected)

    def test_fire_room_die(self):
        test_player = {"Current HP": 3}
        fire_room(test_player)
        actual = test_player["Current HP"]
        expected = -2
        self.assertEqual(actual, expected)

    def test_fire_room_body_is_burning(self):
        test_player = {"Current HP": 0}
        fire_room(test_player)
        actual = test_player["Current HP"]
        expected = -5
        self.assertEqual(actual, expected)

    def test_fire_room_cant_even_feel_it(self):
        test_player = {"Current HP": 30000}
        fire_room(test_player)
        actual = test_player["Current HP"]
        expected = 29995
        self.assertEqual(actual, expected)

    def test_attack_no_current_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"forgot I can get stronger": 2, "atk": 3}
            fire_room(test_player)

    def test_attack_no_integer_in_current_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Current HP": 7.2}
            fire_room(test_player)