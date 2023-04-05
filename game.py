import copy
import random
from copy import deepcopy

from test_board import populate_board, import_room_templates
from utilities.miscellaneous import open_json_file


# identifier = key
#     description
#     function call
#     number of rooms possible


# def make_board(row: int, column: int) -> dict:
#     """
#     Create a dictionary comprised of rows multiplied by columns keys with value of 'Empty room'
#
#     :param row: an integer that is equal or greater than 2
#     :param column: an integer tha is equal or greater than 2
#     :precondition: row must be an integer that is equal or greater than 2
#     :precondition: column must be an integer that is equal or greater than 2
#     :postcondition: creates a dictionary with keys of rows by columns with value of 'Empty room'
#     :return: a dictionary comprised of rows multiplied by columns keys with value of 'Empty room'
#     :raises ValueError: if number is not an integer or is less than 2
#     >>> make_board(3, 3)
#     {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (2, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room', \
# (2, 1): 'Empty Room', (0, 2): 'Empty Room', (1, 2): 'Empty Room', (2, 2): 'Empty Room'}
#
#     >>> make_board(2, 2)
#     {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
#     """
#     if row < 2 or column < 2:
#         raise ValueError("Dimension must be 2 or greater")
#     return {(lateral, longitudinal): 'Empty Room' for longitudinal in range(column) for lateral in range(row)}


def make_character() -> dict:
    """
    Create a character that starts at (0, 0) and has HP of 5

    :postcondition: creates a character that starts at (0, 0) and has HP of 5
    :return: a dictionary of a character that starts at (0, 0) and has HP of 5
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}


def describe_current_location(board: dict, character: dict, room_list: dict) -> None:
    """
    Return the room description located in the value that matches the character's location

    :param board: a dictionary with integer-only tuples as keys and a string as values
    :param character: a dictionary containing keys of "X-coordinate" and "Y-coordinate" that are in param board
    :precondition: board must have only integers in the tuple and a string as values
    :precondition: character must contain two keys named "X-coordinate" and "Y-coordinate" with values in param board
    :postcondition: returns the string description of the room the character is in
    :return: a string describing the room the character is in
    :raises ValueError: if character coordinate values are not in the parameter of board
    >>> example_board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
    >>> example_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> describe_current_location(example_board, example_character)
    Empty Room
    You are currently at (0, 0)
    Your HP is: 5

    >>> example_board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'PUPPY ROOM!'}
    >>> example_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 2}
    >>> describe_current_location(example_board, example_character)
    PUPPY ROOM!
    You are currently at (1, 1)
    Your HP is: 2
    """
    if (character["X-coordinate"], character["Y-coordinate"]) not in board:
        raise KeyError("Character is out of bounds")
    else:
        if get_board_id(board, character) == 'startroom' or 'bossroom':
            pass
        else:
            print(room_list[get_board_id(board, character)][0])
            print("You are currently at (" + str(character["X-coordinate"]) + ", " + str(character["Y-coordinate"]) + ")")
            print("Your HP is: " + str(character["Current HP"]))


def get_board_id(board, character):
    return board[(character["X-coordinate"], character["Y-coordinate"])]


def get_user_choice() -> int:
    """
    Return a number between 1 and 4 for the character to move in

    :postcondition: returns an integer between 1 and 4
    :return: an integer between 1 and 4
    """

    directions = {"1": "North", "2": "East", "3": "South", "4": "West"}
    print("Enter a number for the direction you want:")
    for key in directions:
        print(key + " : " + directions[key])
    movement = input()
    while movement not in directions:
        print("That is not a valid numeric choice, please select from the following:")
        for key in directions:
            print(key + " : " + directions[key])
        movement = input()
    return int(movement)


def validate_move(board: dict, character: dict, direction: int) -> bool:
    """
    Return a Boolean if the character can move in chosen direction

    :param board: a dictionary with integer-only tuples as keys and a string as values
    :param character: a dictionary containing keys of "X-coordinate" and "Y-coordinate"
    :param direction: an integer between 1 and 4
    :precondition: board must have only integers in the tuple and a string as values
    :precondition: character must contain two keys named "X-coordinate" and "Y-coordinate"
    :precondition: direction is an integer between 1 and 4
    :postcondition: returns Boolean if the character can move in chosen direction
    :return: a Boolean if the character can move in chosen direction
    >>> example_board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
    >>> example_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> example_direction = 2
    >>> validate_move(example_board, example_character, example_direction)
    True

    >>> example_board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1): 'Empty Room'}
    >>> example_character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 3}
    >>> example_direction = 4
    >>> validate_move(example_board, example_character, example_direction)
    False
    """
    movement_value = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
    projected_x_axis = character["X-coordinate"] + movement_value[direction][0]
    projected_y_axis = character["Y-coordinate"] + movement_value[direction][1]
    if (projected_x_axis, projected_y_axis) not in board:
        return False
    else:
        return True


def move_character(character: dict, direction: int) -> None:
    """
    Updates the character dictionary keys of coordinate with the new coordinate values

    :param character: a dictionary containing keys of "X-coordinate" and "Y-coordinate"
    :param direction: a string of one of "North", "East", "South", or "West"
    :precondition: character must contain two keys named "X-coordinate" and "Y-coordinate"
    :precondition: direction is an integer between 1 and 4 inclusive
    :postcondition: updates the associated coordinate with the new position
    >>> example_character = {"X-coordinate": 0, "Y-coordinate": 3, "Current HP": 5}
    >>> example_direction = 2
    >>> move_character(example_character, example_direction)
    >>> example_character
    {'X-coordinate': 1, 'Y-coordinate': 3, 'Current HP': 5}

    >>> example_character = {"X-coordinate": 3, "Y-coordinate": 1, "Current HP": 3}
    >>> example_direction = 3
    >>> move_character(example_character, example_direction)
    >>> example_character
    {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 3}
    """

    movement_value = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
    character["X-coordinate"] += movement_value[direction][0]
    character["Y-coordinate"] += movement_value[direction][1]


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


def guessing_game(character: dict) -> None:
    """
    Return a Boolean of whether the character is at the bottom right hand corner

    :param character: a dictionary containing a key named "Current HP"
    :precondition: character must contain a key named "Current HP"
    :postcondition: affects the character's HP according to a right or wrong guess
    """
    secret_number = random.randint(1, 5)
    try:
        guess = int(input('"MUAHAHA, enter a number between 1 and 5 inclusive!":'))
    except ValueError:
        print('"That isn\'t a number dummy, NOW DIE!"')
        print("You have taken 1 damage!")
        character["Current HP"] -= 1
    else:
        if guess == secret_number:
            print('"DARN IT, YOU GOT IT I\'LL BE BACKKKKKK"')
        else:
            print(f'"Sorry, the number was {secret_number}, NOW DIE!"')
            print("You have taken 1 damage!")
            character["Current HP"] -= 1


def is_alive(character: dict) -> bool:
    """
    Return a Boolean of whether the character is alive (health above zero)

    :param character: a dictionary containing a key named "Current HP" with a number as the value
    :precondition: character must contain a key named "Current HP" with a number as the value
    :postcondition: returns a Boolean if the character is alive or not (health above zero)
    :return: a Boolean stating if the character is alive
    >>> example_character = {"Current HP": 5}
    >>> is_alive(example_character)
    True

    >>> example_character = {"Current HP": 0}
    >>> is_alive(example_character)
    False
    """
    return character["Current HP"] > 0


def game():
    rows = 5
    columns = 5
    board = populate_board(rows, columns)
    character = make_character()
    room_list = import_room_templates()
    achieved_goal = False
    while not achieved_goal and is_alive(character):
        describe_current_location(board, character, room_list)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
        else:
            print("You can't move that way!")

        there_is_a_challenger = check_for_foes()
        if there_is_a_challenger:
            guessing_game(character)
        achieved_goal = check_if_goal_attained(board, character)
    else:
        if not is_alive(character):
            print("Sorry you died, GITGUD. Run the program to try again!")
        else:
            print("Congratulations, you beat the game!")


def main():

    game()


if __name__ == "__main__":
    main()
