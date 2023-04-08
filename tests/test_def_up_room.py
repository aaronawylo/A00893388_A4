"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import def_up_room


class TestDefUpRoom(TestCase):
    def test_def_up_room_normal(self):
        test_player = {"def": 10}
        def_up_room(test_player)
        actual = test_player["def"]
        expected = 11
        self.assertEqual(actual, expected)

    def test_def_up_room_no_muscles(self):
        test_player = {"def": 0}
        def_up_room(test_player)
        actual = test_player["def"]
        expected = 1
        self.assertEqual(actual, expected)

    def test_def_up_room_muscles_are_concave(self):
        test_player = {"def": -5}
        def_up_room(test_player)
        actual = test_player["def"]
        expected = -4
        self.assertEqual(actual, expected)

    def test_def_up_room_cant_even_feel_it(self):
        test_player = {"def": 30000}
        def_up_room(test_player)
        actual = test_player["def"]
        expected = 30001
        self.assertEqual(actual, expected)

    def test_attack_no_def_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"forgot I can get stronger": 2}
            def_up_room(test_player)

    def test_attack_no_integer_in_def(self):
        with self.assertRaises(TypeError):
            test_player = {"def": 7.2}
            def_up_room(test_player)
