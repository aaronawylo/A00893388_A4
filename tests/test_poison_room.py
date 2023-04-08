"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import poison_room


class TestPoisonRoom(TestCase):
    def test_poison_room(self):
        test_player = {"Current HP": 10}
        poison_room(test_player)
        actual = test_player["Current HP"]
        expected = 8
        self.assertEqual(actual, expected)

    def test_poison_room_die(self):
        test_player = {"Current HP": 1}
        poison_room(test_player)
        actual = test_player["Current HP"]
        expected = -1
        self.assertEqual(actual, expected)

    def test_poison_room_im_already_dead_though(self):
        test_player = {"Current HP": 0}
        poison_room(test_player)
        actual = test_player["Current HP"]
        expected = -2
        self.assertEqual(actual, expected)

    def test_poison_room_cant_even_feel_it(self):
        test_player = {"Current HP": 30000}
        poison_room(test_player)
        actual = test_player["Current HP"]
        expected = 29998
        self.assertEqual(actual, expected)

    def test_attack_no_current_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"forgot I can get stronger": 2, "atk": 3}
            poison_room(test_player)

    def test_attack_no_integer_in_current_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Current HP": 7.2}
            poison_room(test_player)

