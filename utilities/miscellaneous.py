import os
import json
import random


def menu_print(menu: dict) -> None:
    for every in menu:
        print(f"{every}: {menu[every]}")


def populate_menu(menu_list: list) -> dict:
    return dict(enumerate(menu_list, 1))


def open_json_file(file_name: str) -> dict:
    if not os.path.isfile(file_name):
        raise FileNotFoundError("Your file doesn't exist :)")
    else:
        with open(file_name) as file_object:
            loaded_json = json.load(file_object)
        return loaded_json


def check_if_goal_attained(board: dict, character: dict) -> bool:
    """
    Return a Boolean of whether the character is at the bottom right hand corner of board

    :param board: a dictionary with integer-only tuples as keys and a string as values
    :param character: a dictionary containing keys of "X-coordinate" and "Y-coordinate"
    :precondition: board must have only integers in the tuple and a string as values
    :precondition: character must contain two keys named "X-coordinate" and "Y-coordinate"
    :postcondition: returns a Boolean stating if the character is at max value for both X and Y-coordinates
    :return: a Boolean stating if the character is at max value for both X and Y-coordinates
    >>> example_board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
    >>> example_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
    >>>

    >>> example_board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
    >>> example_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
    """
    x_coordinates = []
    y_coordinates = []
    for key in board:
        x_coordinates.append(key[0])
        y_coordinates.append(key[1])
    if character["X-coordinate"] == max(x_coordinates) and character["Y-coordinate"] == max(y_coordinates):
        return True
    else:
        return False


def check_for_foes() -> bool:
    """
    Return a Boolean of whether the character has encountered an enemy at 25% chance

    :postcondition: returns a Boolean stating if the character has run into an enemy
    :return: a Boolean stating if the character has run into an enemy at 25% chance
    """
    encounter = random.randint(1, 4)
    if encounter == 1:
        return True
    else:
        return False
