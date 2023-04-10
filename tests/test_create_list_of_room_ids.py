"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.game_board import create_list_of_room_ids


class TestCreateListOfRoomIDs(TestCase):
    def test_create_list_of_room_ids_base(self):
        example_templates = {"fire_room": ["This is a fire_room", "fire_room", 2], "pup_room": ["This is a smoke_room",
                             "smoke_room", 1]}
        actual = create_list_of_room_ids(example_templates, 7)
        expected = ['fire_room', 'fire_room', 'pup_room', 'empty_room', 'empty_room']
        self.assertEqual(actual, expected)

    def test_create_list_of_room_ids_no_empty(self):
        example_templates = {"cat_room": ["This is a cat_room", "cat_room", 1], "bird_room": ["This is a bird_room",
                             "bird_room", 1]}
        actual = create_list_of_room_ids(example_templates, 4)
        expected = ['cat_room', 'bird_room']
        self.assertEqual(actual, expected)

    def test_create_list_of_room_ids_dict_len_error(self):
        with self.assertRaises(KeyError):
            example_templates = {}
            create_list_of_room_ids(example_templates, 7)

    def test_create_list_of_room_ids_length_too_small_error(self):
        with self.assertRaises(ValueError):
            example_templates = {"fire_room": ["This is a fire_room", "fire_room", 2], "pup_room":
                                 ["This is a smoke_room", "smoke_room", 1]}
            create_list_of_room_ids(example_templates, 4)

    def test_create_list_of_room_ids_iterable_too_short(self):
        with self.assertRaises(IndexError):
            example_templates = {"fire_room": ["This is a fire_room", "fire_room"], "pup_room":
                                 ["This is a smoke_room", "smoke_room", 1]}
            create_list_of_room_ids(example_templates, 4)

    def test_create_list_of_room_ids_iterable_too_short_second_list(self):
        with self.assertRaises(IndexError):
            example_templates = {"fire_room": ["This is a fire_room", "fire_room", 2], "pup_room":
                                 ["This is a smoke_room", "smoke_room"]}
            create_list_of_room_ids(example_templates, 4)
