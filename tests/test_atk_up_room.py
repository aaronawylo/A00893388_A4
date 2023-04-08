"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import atk_up_room


class TestAtkUpRoom(TestCase):
    def test_atk_up_room_normal(self):
        test_player = {"atk": 10}
        atk_up_room(test_player)
        actual = test_player["atk"]
        expected = 11
        self.assertEqual(actual, expected)

    def test_atk_up_room_no_muscles(self):
        test_player = {"atk": 0}
        atk_up_room(test_player)
        actual = test_player["atk"]
        expected = 1
        self.assertEqual(actual, expected)

    def test_atk_up_room_muscles_are_concave(self):
        test_player = {"atk": -5}
        atk_up_room(test_player)
        actual = test_player["atk"]
        expected = -4
        self.assertEqual(actual, expected)

    def test_atk_up_room_cant_even_feel_it(self):
        test_player = {"atk": 30000}
        atk_up_room(test_player)
        actual = test_player["atk"]
        expected = 30001
        self.assertEqual(actual, expected)

    def test_attack_no_atk_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"forgot I can get stronger": 2}
            atk_up_room(test_player)

    def test_attack_no_integer_in_atk(self):
        with self.assertRaises(TypeError):
            test_player = {"atk": 7.2}
            atk_up_room(test_player)
