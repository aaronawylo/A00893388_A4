"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.game_board import room_action


class TestRoomAction(TestCase):
    def test_room_action_fire_room(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("fire_room", test_player)
        actual = test_player["Current HP"]
        expected = 5
        self.assertEqual(actual, expected)

    def test_room_action_poison_room(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("poison_room", test_player)
        actual = test_player["Current HP"]
        expected = 8
        self.assertEqual(actual, expected)

    def test_room_action_heal_room(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("heal_room", test_player)
        actual = test_player["Current HP"]
        expected = 15
        self.assertEqual(actual, expected)

    def test_room_action_potion_room(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("potion_room", test_player)
        actual = test_player["potions"]
        expected = 6
        self.assertEqual(actual, expected)

    def test_room_action_atk_up_room(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("atk_up_room", test_player)
        actual = test_player["atk"]
        expected = 6
        self.assertEqual(actual, expected)

    def test_room_action_def_up_room(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("def_up_room", test_player)
        actual = test_player["def"]
        expected = 3
        self.assertEqual(actual, expected)

    def test_room_action_hp_up_room_current(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("hp_up_room", test_player)
        actual = test_player["Current HP"]
        expected = 30
        self.assertEqual(actual, expected)

    def test_room_action_hp_up_room_max(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("hp_up_room", test_player)
        actual = test_player["Max HP"]
        expected = 40
        self.assertEqual(actual, expected)

    def test_room_action_heal_sanctuary(self):
        test_player = {"Max HP": 20, "Current HP": 10, "atk": 5, "def": 2, "potions": 3}
        room_action("heal_sanctuary", test_player)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)
