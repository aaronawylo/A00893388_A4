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
    return {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 2, "level": 1, "exp":
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
    """
    Increases the player's level by one, the attack and defense stats by 3, and the two HP values by 20

    :param player: a dictionary containing the key values of "exp", "Max HP", "Current HP", "atk", "def" and "level"
    :precondition: player must be a dictionary containing "exp", "Max HP", "Current HP", "atk", "def" and "level"
    :precondition: the keys must have integer values
    :postcondition: levels up the player and increases the stats accordingly and reduces "exp" by 100
    >>> test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, \
                       "level": 1, "exp": 0, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
    >>> level_up(test_player)
    >>> test_player
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 20, 'Current HP': 20, 'atk': 2, 'def': 1, 'level': 1, 'exp': 0, \
'potions': 3, 'Battle Actions': ['Attack', 'Defend', 'Use Potion']}

    >>> test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, \
                       "level": 1, "exp": 110, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
    >>> level_up(test_player)
    You have gained a level, and you are now level 2!
    Your Max HP is 40!
    Your Attack is now 5!
    Your Defense is now 4!
    <BLANKLINE>
    >>> test_player
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 40, 'Current HP': 40, 'atk': 5, 'def': 4, 'level': 2, 'exp': 10, \
'potions': 3, 'Battle Actions': ['Attack', 'Defend', 'Use Potion']}
    """
    error_check = ("exp", "Max HP", "Current HP", "atk", "def", "level")
    for each in error_check:
        if each not in player:
            raise KeyError("Read my docstrings, dummy.")
        if type(player[each]) != int:
            raise TypeError("Read my docstrings, dummy.")
    if player["exp"] >= 100 and player["level"] < 3:
        player["exp"] -= 100
        player["Max HP"] += 20
        player["Current HP"] += 20
        player["atk"] += 3
        player["def"] += 3
        player["level"] += 1
        print(f"You have gained a level, and you are now level {player['level']}!\nYour Max HP is {player['Max HP']}!\n"
              f"Your Attack is now {player['atk']}!\nYour Defense is now {player['def']}!\n")
