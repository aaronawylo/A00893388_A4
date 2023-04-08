"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import hp_up_room


class TestHPUpRoom(TestCase):
    def test_hp_up_room_normal(self):
        test_player = {"Max HP": 20, "Current HP": 10}
        hp_up_room(test_player)
        actual = test_player["Current HP"]
        expected = 30
        self.assertEqual(actual, expected)

    def test_hp_up_room_already_healthy(self):
        test_player = {"Max HP": 20, "Current HP": 20}
        hp_up_room(test_player)
        actual = test_player["Current HP"]
        expected = 40
        self.assertEqual(actual, expected)

    def test_hp_up_room_but_im_already_dead(self):
        test_player = {"Max HP": 0, "Current HP": 0}
        hp_up_room(test_player)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_hp_up_room_rise_from_the_dead(self):
        test_player = {"Max HP": -5, "Current HP": -10}
        hp_up_room(test_player)
        actual = test_player["Current HP"]
        expected = 10
        self.assertEqual(actual, expected)

    def test_hp_up_room_massive_number_check(self):
        test_player = {"Max HP": 20000, "Current HP": 30000}
        hp_up_room(test_player)
        actual = test_player["Current HP"]
        expected = 30020
        self.assertEqual(actual, expected)

    def test_hp_up_room_no_current_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 20, "What is health?": 3}
            hp_up_room(test_player)

    def test_hp_up_room_no_integer_in_current_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 20, "Current HP": 7.2}
            hp_up_room(test_player)

    def test_hp_up_room_normal_max_hp(self):
        test_player = {"Max HP": 20, "Current HP": 10}
        hp_up_room(test_player)
        actual = test_player["Max HP"]
        expected = 40
        self.assertEqual(actual, expected)

    def test_hp_up_room_already_healthy_max_hp(self):
        test_player = {"Max HP": 30, "Current HP": 30}
        hp_up_room(test_player)
        actual = test_player["Max HP"]
        expected = 50
        self.assertEqual(actual, expected)

    def test_hp_up_room_but_im_already_dead_max_hp(self):
        test_player = {"Max HP": 0, "Current HP": 0}
        hp_up_room(test_player)
        actual = test_player["Max HP"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_hp_up_room_rise_from_the_dead_max_hp(self):
        test_player = {"Max HP": -5, "Current HP": -10}
        hp_up_room(test_player)
        actual = test_player["Max HP"]
        expected = 15
        self.assertEqual(actual, expected)

    def test_hp_up_room_massive_number_check_max_hp(self):
        test_player = {"Max HP": 20000, "Current HP": 30000}
        hp_up_room(test_player)
        actual = test_player["Max HP"]
        expected = 20020
        self.assertEqual(actual, expected)

    def test_hp_up_room_no_max_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"What is health?": 20, "Current HP": 3}
            hp_up_room(test_player)

    def test_hp_up_room_no_integer_in_max_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 20.5, "Current HP": 10}
            hp_up_room(test_player)
