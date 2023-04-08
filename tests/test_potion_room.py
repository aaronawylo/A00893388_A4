"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import potion_room


class TestPotionRoom(TestCase):
    def test_potion_room_normal(self):
        test_player = {"potions": 10}
        potion_room(test_player)
        actual = test_player["potions"]
        expected = 13
        self.assertEqual(actual, expected)

    def test_potion_room_was_empty(self):
        test_player = {"potions": 0}
        potion_room(test_player)
        actual = test_player["potions"]
        expected = 3
        self.assertEqual(actual, expected)

    def test_potion_room_how_do_you_have_negative_potions(self):
        test_player = {"potions": -2}
        potion_room(test_player)
        actual = test_player["potions"]
        expected = 1
        self.assertEqual(actual, expected)

    def test_potion_room_cant_even_feel_it(self):
        test_player = {"potions": 30000}
        potion_room(test_player)
        actual = test_player["potions"]
        expected = 30003
        self.assertEqual(actual, expected)

    def test_attack_no_potions_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"elixirs can't heal you here": 0}
            potion_room(test_player)

    def test_attack_no_integer_in_potions(self):
        with self.assertRaises(TypeError):
            test_player = {"potions": 7.2}
            potion_room(test_player)
