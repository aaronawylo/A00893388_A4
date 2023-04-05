

def is_alive(player: dict) -> bool:
    """
    Return a Boolean of whether the character is alive (health above zero)

    :param player: a dictionary containing a key named "Current HP" with a number as the value
    :precondition: character must contain a key named "Current HP" with a number as the value
    :postcondition: returns a Boolean if the character is alive or not (health above zero)
    :return: a Boolean stating if the character is alive
    >>> example_player = {"Current HP": 5}
    >>> is_alive(example_player)
    True

    >>> example_player = {"Current HP": 0}
    >>> is_alive(example_player)
    False
    """
    return player["Current HP"] > 0
