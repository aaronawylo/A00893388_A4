"""
Aaron Lo
A0089388
"""


def boss_laugh(_, enemy: dict, ___) -> None:
    """
    Hades laughs at you and does nothing. Yup that's it.

    :param _: Unused.
    :param enemy: must be a dictionary containing the key "name"
    :param ___: Unused.
    :precondition: enemy must be a dictionary containing the key "name"
    :precondition: enemy's "name" key must have a string as the value denoting the name
    :postcondition: laughs at the player
    >>> test_player = {"Not": "Needed"}
    >>> test_guard = {"Also": "Needed"}
    >>> test_enemy = {"name": "Hades"}
    >>> boss_laugh(test_player, test_enemy, test_guard)
    Hades doubles over in laughter at your feeble attempt.
    """
    if "name" not in enemy:
        raise KeyError("Read my docstrings, dummy.")
    else:
        print(f"{enemy['name']} doubles over in laughter at your feeble attempt.")


def ult_charge(_, enemy: dict, ___) -> None:
    if "name" not in enemy:
        raise KeyError("Read my docstrings, dummy.")
    else:
        print(f"{enemy['name']} is gathering a massive amount of fire!")


def ult_move(player: dict, enemy: dict, guard: int) -> None:
    if "Current HP" not in player or "atk" not in enemy or "name" not in enemy:
        raise KeyError("Read my docstrings, dummy.")
    elif type(enemy["atk"]) != int or type(player["Current HP"]) != int or type(guard) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        enemy_damage = (enemy["atk"] * 10) - guard
        if enemy_damage < 0:
            enemy_damage = 0
        player["Current HP"] -= enemy_damage
        print(f'{enemy["name"]} unleashes all of his built up energy!\nYou took {enemy_damage} damage!')
