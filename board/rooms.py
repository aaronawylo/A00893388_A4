"""
Aaron Lo
A0089388
"""


def fire_room(player: dict) -> None:
    """
    Deals 5 damage to the player's HP

    :param player: a dictionary containing the key "Current HP"
    :precondition: player must be a dictionary containing the key "Current HP"
    :precondition: "Current HP" must have an integer value pair
    :postcondition: subtracts 5 damage from the player's current HP
    >>> test_player = {"Current HP": 10}
    >>> fire_room(test_player)
    >>> test_player["Current HP"]
    5

    >>> test_player = {"Current HP": 18}
    >>> fire_room(test_player)
    >>> test_player["Current HP"]
    13
    """
    if "Current HP" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["Current HP"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player["Current HP"] -= 5


def poison_room(player: dict) -> None:
    """
    Deals 2 damage to the player's HP

    :param player: a dictionary containing the key "Current HP"
    :precondition: player must be a dictionary containing the key "Current HP"
    :precondition: "Current HP" must have an integer value pair
    :postcondition: subtracts 2 damage from the player's current HP
    >>> test_player = {"Current HP": 10}
    >>> poison_room(test_player)
    >>> test_player["Current HP"]
    8

    >>> test_player = {"Current HP": 18}
    >>> poison_room(test_player)
    >>> test_player["Current HP"]
    16
    """
    if "Current HP" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["Current HP"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player["Current HP"] -= 2


def heal_room(player: dict) -> None:
    """
    Heals up to 5 points of the player's HP

    :param player: a dictionary containing the keys "Current HP" and "Max HP"
    :precondition: player must be a dictionary containing the keys "Current HP" and "Max HP"
    :precondition: "Current HP" must have an integer value pair
    :precondition: "Max HP" must have an integer value pair and be greater or equal than "Current HP"
    :postcondition: adds 5 points to the player's current HP
    >>> test_player = {"Max HP": 20, "Current HP": 10}
    >>> heal_room(test_player)
    >>> test_player["Current HP"]
    15

    >>> test_player = {"Max HP": 30, "Current HP": 28}
    >>> heal_room(test_player)
    >>> test_player["Current HP"]
    30
    """
    if "Current HP" not in player or "Max HP" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["Current HP"]) != int or type(player["Max HP"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player["Current HP"] += 5
        if player["Current HP"] > player["Max HP"]:
            player["Current HP"] = player["Max HP"]


def potion_room(player: dict) -> None:
    """
    Gives the player 3 potions

    :param player: a dictionary containing the key "potions"
    :precondition: player must be a dictionary containing the key "potions"
    :precondition: "potions" must have an integer value pair
    :postcondition: adds 3 potions to the "potions" key
    >>> test_player = {"potions": 3}
    >>> potion_room(test_player)
    >>> test_player["potions"]
    6

    >>> test_player = {"potions": 5}
    >>> potion_room(test_player)
    >>> test_player["potions"]
    8
    """
    if "potions" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["potions"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player["potions"] += 3


def atk_up_room(player: dict) -> None:
    """
    Adds 1 to the player's attack stat

    :param player: a dictionary containing the key "atk"
    :precondition: player must be a dictionary containing the key "atk"
    :precondition: "atk" must have an integer value pair
    :postcondition: adds 1 to the player's atk stat
    >>> test_player = {"atk": 3}
    >>> atk_up_room(test_player)
    >>> test_player["atk"]
    4

    >>> test_player = {"atk": 5}
    >>> atk_up_room(test_player)
    >>> test_player["atk"]
    6
    """
    if "atk" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["atk"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player['atk'] += 1


def def_up_room(player: dict) -> None:
    """
    Adds 1 to the player's defense stat

    :param player: a dictionary containing the key "def"
    :precondition: player must be a dictionary containing the key "def"
    :precondition: "def" must have an integer value pair
    :postcondition: adds 1 to the player's def stat
    >>> test_player = {"def": 2}
    >>> def_up_room(test_player)
    >>> test_player["def"]
    3

    >>> test_player = {"def": 7}
    >>> def_up_room(test_player)
    >>> test_player["def"]
    8
    """
    if "def" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["def"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player['def'] += 1


def hp_up_room(player: dict) -> None:
    """
    Adds 20 to the player's Max HP and Current HP stats

    :param player: a dictionary containing the keys "Current HP" and "Max HP"
    :precondition: player must be a dictionary containing the keys "Current HP" and "Max HP"
    :precondition: "Current HP" must have an integer value pair
    :precondition: "Max HP" must have an integer value pair and be greater or equal than "Current HP"
    :postcondition: adds 20 points to the player's current HP and max HP
    >>> test_player = {"Max HP": 20, "Current HP": 10}
    >>> hp_up_room(test_player)
    >>> test_player["Current HP"]
    30
    >>> test_player["Max HP"]
    40

    >>> test_player = {"Max HP": 60, "Current HP": 55}
    >>> hp_up_room(test_player)
    >>> test_player["Current HP"]
    75
    >>> test_player["Max HP"]
    80
    """
    if "Current HP" not in player or "Max HP" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["Current HP"]) != int or type(player["Max HP"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player['Max HP'] += 20
        player['Current HP'] += 20


def heal_sanctuary(player: dict) -> None:
    """
    Heals the player's HP to full

    :param player: a dictionary containing the keys "Current HP" and "Max HP"
    :precondition: player must be a dictionary containing the keys "Current HP" and "Max HP"
    :precondition: "Current HP" must have an integer value pair
    :precondition: "Max HP" must have an integer value pair and be greater or equal than "Current HP"
    :postcondition: sets the player's "Current HP" to "Max HP"
    >>> test_player = {"Max HP": 20, "Current HP": 10}
    >>> heal_sanctuary(test_player)
    >>> test_player["Current HP"]
    20

    >>> test_player = {"Max HP": 30, "Current HP": 28}
    >>> heal_sanctuary(test_player)
    >>> test_player["Current HP"]
    30
    """
    if "Current HP" not in player or "Max HP" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["Current HP"]) != int or type(player["Max HP"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player["Current HP"] = player["Max HP"]


def main():
    """
    Drives the program
    """

    pass


if __name__ == "__main__":
    main()
