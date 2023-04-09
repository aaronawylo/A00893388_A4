"""
Aaron Lo
A0089388
"""


def get_user_choice() -> int:
    """
    Return a number between 1 and 4 for the player to move in

    :postcondition: returns an integer between 1 and 4
    :return: an integer between 1 and 4
    """

    directions = {"1": "North", "2": "East", "3": "South", "4": "West"}
    print(f"Enter a number for the direction you want:")
    for key in directions:
        print(key + " : " + directions[key])
    movement = input()
    while movement not in directions:
        print(f"That is not a valid numeric choice, please select from the following:")
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
