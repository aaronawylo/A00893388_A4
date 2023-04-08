"""
Aaron Lo
A0089388
"""

import random

from board.rooms import fireroom, poisonroom, healroom, potionroom, atkuproom, defuproom, hpuproom
from utilities.miscellaneous import open_json_file


def room_action(room_name: str, player: dict):
    room_actions = {"fireroom": fireroom, "poisonroom": poisonroom, "healroom": healroom, "potionroom": potionroom,
                    "atkuproom": atkuproom, "defuproom": defuproom, "hpuproom": hpuproom}
    if room_name in room_actions:
        return room_actions[room_name](player)
    else:
        return


def import_room_templates() -> dict:
    dynamics_to_add = open_json_file('rooms.json')
    statics_to_add = open_json_file('static_rooms.json')
    for every, item in statics_to_add.items():
        dynamics_to_add[every] = item
    return dynamics_to_add


def create_list_of_room_ids(templates, length):

    template_list = [key for key in templates for _ in range(templates[key][2])]
    empty_number = length - len(template_list) - 2
    while empty_number > 0:
        template_list.append("emptyroom")
        empty_number -= 1
    return template_list


def populate_board(row, column):

    example_dictionary = open_json_file('rooms.json')
    board_numbers = [(lateral, longitudinal) for longitudinal in range(column) for lateral in range(row)]
    board_length = len(board_numbers)
    room_ids = create_list_of_room_ids(example_dictionary, board_length)
    random.shuffle(room_ids)
    room_ids.insert(0, "startroom")
    room_ids.append('bossroom')
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
    >>> example_board = {(0, 0): 'emptyroom', (1, 0): 'emptyroom', (0, 1): 'emptyroom', (1, 1): 'emptyroom'}
    >>> example_player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> example_room_list = {"emptyroom": ["This is an empty room.", "emptyroomfunction"]}
    >>> describe_current_location(example_board, example_player, example_room_list)
    This is an empty room.
    You are currently at (0, 0)
    Your HP is: 5

    >>> example_board = {(0, 0): 'emptyroom', (1, 0): 'emptyroom', (0, 1): 'emptyroom', (1, 1): 'puppyroom'}
    >>> example_player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
    >>> example_room_list = {"emptyroom": ["This is an empty room.", "emptyroomfunction"], "puppyroom": ["PUPPIES."]}
    >>> describe_current_location(example_board, example_player, example_room_list)
    PUPPIES.
    You are currently at (1, 1)
    Your HP is: 5
    """
    if (player["X-coordinate"], player["Y-coordinate"]) not in board:
        raise KeyError("Player is out of bounds")
    else:
        print(room_list[get_board_id(board, player)][0])
        print("You are currently at (" + str(player["X-coordinate"]) + ", " + str(player["Y-coordinate"]) + ")")
        print("Your HP is: " + str(player["Current HP"]) + "\n")


def get_board_id(board, player):
    """
    Returns the value of attached to the key where the player is currently

    :param board: a dictionary with integer-only tuples as keys and a string as values
    :param player: a dictionary containing keys of "X-coordinate" and "Y-coordinate" that are in param board
    :precondition: board must have only integers in the tuple and a string as values
    :precondition: player must contain two keys named "X-coordinate" and "Y-coordinate" with values in param board
    :postcondition: returns the value attached to the tuple coordinate key in board
    :return: the value attached to the tuple coordinate key in board
    >>> example_board = {(0, 0): 'emptyroom', (1, 0): 'emptyroom', (0, 1): 'emptyroom', (1, 1): 'emptyroom'}
    >>> example_player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> get_board_id(example_board, example_player)
    'emptyroom'

    >>> example_board = {(0, 0): 'puppyroom', (1, 0): 'kittyroom', (0, 1): 'birdyroom', (1, 1): 'foxroom'}
    >>> example_player = {"X-coordinate": 1, "Y-coordinate": 0}
    >>> get_board_id(example_board, example_player)
    'kittyroom'
    """
    return board[(player["X-coordinate"], player["Y-coordinate"])]


def main():

    print(populate_board(5, 5))


if __name__ == "__main__":
    main()
