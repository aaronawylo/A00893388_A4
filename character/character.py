"""
Aaron Lo
A0089388
"""


def make_character() -> dict:
    """
    Create a character that starts at (0, 0) and contains all necessary information

    :postcondition: creates a character that starts at (0, 0) and contains all necessary information
    :return: a dictionary of a character that starts at (0, 0) and contains all necessary information
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 20, 'Current HP': 20, 'atk': 2, 'def': 1, 'level': 1, 'exp': 0, \
'potions': 3, 'Battle Actions': ['Attack', 'Defend', 'Use Potion']}
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "exp":
            0, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}


def is_alive(player: dict) -> bool:
    """
    Return a Boolean of whether the character is alive (health above zero)

    :param player: a dictionary containing a key named "Current HP" with a number as the value
    :precondition: player must contain a key named "Current HP" with a number as the value
    :postcondition: returns a Boolean if the player is alive or not (health above zero)
    :return: a Boolean stating if the player is alive
    >>> example_player = {"Current HP": 5}
    >>> is_alive(example_player)
    True

    >>> example_player = {"Current HP": 0}
    >>> is_alive(example_player)
    False
    """
    return player["Current HP"] > 0


def level_up(player: dict):
    if player["exp"] >= 100:
        pass