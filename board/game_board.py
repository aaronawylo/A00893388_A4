"""
Aaron Lo
A0089388
"""

import random

from board.rooms import fire_room, poison_room, heal_room, potion_room, atk_up_room, def_up_room, hp_up_room, \
    heal_sanctuary
from utilities.miscellaneous import open_json_file


def room_action(room_name: str, player: dict):
    """
    Returns the function of the room the player is in if there is one

    :param room_name: a string denoting the room name
    :param player: a dictionary containing the keys "Current HP", "Max HP", "potions", "atk", and "def"
    :precondition: room_name must be a string
    :precondition: player must be a dictionary containing the keys "Current HP", "Max HP", "potions", "atk", and "def"
    :postcondition: activates the room's special effect if it is a special room
    :return: the function of the special room the player is in if there is one
    >>> test_player = {"Max HP": 20, "Current HP": 10, "atk": 2, "def": 2, "potions": 3}
    >>> room_action("fire_room", test_player)
    >>> test_player["Current HP"]
    5

    >>> test_player = {"Max HP": 20, "Current HP": 20, "atk": 7, "def": 2, "potions": 3}
    >>> room_action("atk_up_room", test_player)
    >>> test_player["atk"]
    8
    """
    room_actions = {"fire_room": fire_room, "poison_room": poison_room, "heal_room": heal_room, "potion_room":
                    potion_room, "atk_up_room": atk_up_room, "def_up_room": def_up_room, "hp_up_room": hp_up_room,
                    "heal_sanctuary": heal_sanctuary}
    if room_name in room_actions:
        return room_actions[room_name](player)
    else:
        return


def import_room_templates() -> dict:
    dynamics_to_add = open_json_file('data/rooms.json')
    statics_to_add = open_json_file('data/static_rooms.json')
    for every, item in statics_to_add.items():
        dynamics_to_add[every] = item
    return dynamics_to_add


def create_list_of_room_ids(templates, length):

    template_list = [key for key in templates for _ in range(templates[key][2])]
    empty_number = length - len(template_list) - 2
    while empty_number > 0:
        template_list.append("empty_room")
        empty_number -= 1
    return template_list


def populate_board(row, column):

    example_dictionary = open_json_file('data/rooms.json')
    board_numbers = [(lateral, longitudinal) for longitudinal in range(column) for lateral in range(row)]
    board_length = len(board_numbers)
    room_ids = create_list_of_room_ids(example_dictionary, board_length)
    random.shuffle(room_ids)
    room_ids.insert(0, "start_room")
    room_ids.append('boss_room')
    final_board = dict(zip(board_numbers, room_ids))
    return final_board


def describe_current_location(board: dict, player: dict, room_list: dict) -> None:
    """
    Return the room description located in the value that matches the character's location

    :param board: a dictionary with integer-only tuples as keys and a string as values
    :param player: a dictionary containing keys of "X-coordinate" and "Y-coordinate" that are in param board
    :param room_list: a dictionary containing keys matching the values in board
    :precondition: board must have only integers in the tuple and a string as values
    :precondition: player must contain two keys named "X-coordinate" and "Y-coordinate" with values in param board
    :precondition: player must contain a key named "Current HP" with an integer for a value
    :precondition: room_list must have keys matching the values in board
    :precondition: room_list must have a string denoting the description of the room at index 0 of the value list
    :postcondition: returns the string description of the room the character is in
    :return: a string describing the room the character is in
    :raises ValueError: if character coordinate values are not in the parameter of board
    >>> example_board = {(0, 0): 'empty_room', (1, 0): 'empty_room', (0, 1): 'empty_room', (1, 1): 'empty_room'}
    >>> example_player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> example_room_list = {"empty_room": ["This is an empty room.", "empty_room", 3]}
    >>> describe_current_location(example_board, example_player, example_room_list)
    This is an empty room.
    You are currently at (0, 0)
    Your HP is: 5
    <BLANKLINE>

    >>> example_board = {(0, 0): 'empty_room', (1, 0): 'empty_room', (0, 1): 'empty_room', (1, 1): 'puppy_room'}
    >>> example_player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
    >>> example_room_list = {"empty_room": ["This is an empty room.", "empty_room", 2], "puppy_room": ["PUPPIES."]}
    >>> describe_current_location(example_board, example_player, example_room_list)
    PUPPIES.
    You are currently at (1, 1)
    Your HP is: 5
    <BLANKLINE>
    """
    if (player["X-coordinate"], player["Y-coordinate"]) not in board:
        raise KeyError("Player is out of bounds")
    else:
        print(room_list[get_board_id(board, player)][0])
        print(f"You are currently at ({player['X-coordinate']}, {player['Y-coordinate']})")
        print(f"Your HP is: {player['Current HP']}\n")


def get_board_id(board, player):
    """
    Returns the value of attached to the key where the player is currently

    :param board: a dictionary with integer-only tuples as keys and a string as values
    :param player: a dictionary containing keys of "X-coordinate" and "Y-coordinate" that are in param board
    :precondition: board must have only integers in the tuple and a string as values
    :precondition: player must contain two keys named "X-coordinate" and "Y-coordinate" with values in param board
    :postcondition: returns the value attached to the tuple coordinate key in board
    :return: the value attached to the tuple coordinate key in board
    >>> example_board = {(0, 0): 'empty_room', (1, 0): 'empty_room', (0, 1): 'empty_room', (1, 1): 'empty_room'}
    >>> example_player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> get_board_id(example_board, example_player)
    'empty_room'

    >>> example_board = {(0, 0): 'puppy_room', (1, 0): 'kitty_room', (0, 1): 'bird_room', (1, 1): 'fox_room'}
    >>> example_player = {"X-coordinate": 1, "Y-coordinate": 0}
    >>> get_board_id(example_board, example_player)
    'kitty_room'
    """
    return board[(player["X-coordinate"], player["Y-coordinate"])]


def main():

    print(populate_board(5, 5))


if __name__ == "__main__":
    main()
