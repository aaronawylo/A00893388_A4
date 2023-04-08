"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import heal_room


class TestHealRoom(TestCase):
    def test_heal_room_normal(self):
        test_player = {"Max HP": 20, "Current HP": 10}
        heal_room(test_player)
        actual = test_player["Current HP"]
        expected = 15
        self.assertEqual(actual, expected)

    def test_heal_room_up_to_a_cap(self):
        test_player = {"Max HP": 20, "Current HP": 17}
        heal_room(test_player)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_heal_room_but_im_already_dead(self):
        test_player = {"Max HP": 20, "Current HP": 0}
        heal_room(test_player)
        actual = test_player["Current HP"]
        expected = 5
        self.assertEqual(actual, expected)

    def test_heal_room_cant_even_feel_it(self):
        test_player = {"Max HP": 20, "Current HP": 30000}
        heal_room(test_player)
        actual = test_player["Current HP"]
        expected = 30005
        self.assertEqual(actual, expected)

    def test_attack_no_current_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 20, "What is health?": 3}
            heal_room(test_player)

    def test_attack_no_integer_in_current_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 20, "Current HP": 7.2}
            heal_room(test_player)

    def test_attack_no_max_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"What is health?": 20, "What is health?": 3}
            heal_room(test_player)

    def test_attack_no_integer_in_max_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 20.5, "Current HP": 10}
            heal_room(test_player)
