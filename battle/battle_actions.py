"""
Aaron Lo
A0089388
"""


def attack(player: dict, enemy: dict) -> int:
    """
    Returns a guard value of zero after dealing damage to the enemy

    :param player: a dictionary containing the keys "level" and "atk"
    :param enemy: a dictionary containing the key "hp"
    :precondition: player must contain keys named "level" and "atk"
    :precondition: enemy must contain a key named "hp"
    :precondition: all three necessary keys have integers as values
    :postcondition: deals the correct damage to the enemy's "hp"
    :postcondition: returns a guard value of zero
    :return: the integer zero
    >>> test_player = {"level": 1, "atk": 2}
    >>> test_enemy = {"hp": 3}
    >>> attack(test_player, test_enemy)
    You have dealt 2 damage!
    0
    >>> test_enemy["hp"]
    1

    >>> test_player = {"level": 3, "atk": 4}
    >>> test_enemy = {"hp": 20}
    >>> attack(test_player, test_enemy)
    You have dealt 12 damage!
    0
    >>> test_enemy["hp"]
    8
    """
    if "level" not in player or "atk" not in player or "hp" not in enemy:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["level"]) != int or type(player["atk"]) != int or type(enemy["hp"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        damage = player["level"] * player["atk"]
        enemy["hp"] -= damage
        print(f'You have dealt {damage} damage!')
        return 0


def defend(player: dict, _) -> int:
    """
    Returns the correct guard value from the player's level multiplied by defense

    :param player: a dictionary containing the keys "level" and "def"
    :param _: Unused
    :precondition: player must contain the keys "level" and "def"
    :precondition: keys "level" and "def" must have integers for values
    :postcondition: returns the correct guard value after multiplying level and def together
    :return: an integer denoting the guard value to reduce enemy attack by
    >>> test_player = {"level": 1, "def": 2}
    >>> test_enemy = {"hp": 20}
    >>> defend(test_player, test_enemy)
    You steel yourself for the oncoming attack!
    2

    >>> test_player = {"level": 3, "def": 3}
    >>> test_enemy = {"hp": 20}
    >>> defend(test_player, test_enemy)
    You steel yourself for the oncoming attack!
    9
    """
    if "level" not in player or "def" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["level"]) != int or type(player["def"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        print(f"You steel yourself for the oncoming attack!")
        return player["level"] * player["def"]


def potion(player: dict, _) -> int:
    """
    Returns a guard value of zero after healing the player

    :param player: a dictionary containing the keys "Max HP", "Current HP" and "potions"
    :param _: Unused
    :precondition: player must contain the keys "Max HP", "Current HP" and "potions"
    :precondition: keys "Max HP", "Current HP" and "potions" must have integers for values
    :postcondition: recovers player's current HP by or up to max HP
    :postcondition: returns a guard value of zero
    :return: the integer zero
    >>> test_player = {"Max HP": 20, "Current HP": 10, "potions": 3}
    >>> test_enemy = {"hp": 3}
    >>> potion(test_player, test_enemy)
    You drank the potion and healed 10 HP!
    Your HP is now 20!
    0
    >>> test_player["Current HP"]
    20

    >>> test_player = {"Max HP": 30, "Current HP": 28, "potions": 2}
    >>> test_enemy = {"hp": 3}
    >>> potion(test_player, test_enemy)
    You drank the potion and healed 2 HP!
    Your HP is now 30!
    0
    >>> test_player["Current HP"]
    30
    """
    if "potions" not in player or "Current HP" not in player or "Max HP" not in player:
        raise KeyError("Read my docstrings, dummy.")
    elif type(player["potions"]) != int or type(player["Current HP"]) != int or type(player["Max HP"]) != int:
        raise TypeError("Read my docstrings, dummy.")
    else:
        player["potions"] -= 1
        player["Current HP"] += 10
        healed = 10
        if player["Current HP"] > player["Max HP"]:
            healed = 10 - (player["Current HP"] - player["Max HP"])
            player["Current HP"] = player["Max HP"]
        print(f'You drank the potion and healed {healed} HP!\nYour HP is now {player["Current HP"]}!')
        return 0


def enemy_attack(player: dict, enemy: dict, guard: int) -> None:
    """
    Deals damage to the player's Current HP using the enemy's attack minus the guard point

    :param player: a dictionary containing the key "Current HP"
    :param enemy: a dictionary containing the key "atk"
    :param guard: an integer
    :precondition: player must contain a key called "Current HP"
    :precondition: player's "Current HP" key must have an integer value
    :precondition: enemy must contain keys called "atk" and "name"
    :precondition: enemy's "atk" key must have an integer value
    :precondition: guard must be an integer
    :postcondition: deals the correct amount of damage to the player's HP
    >>> test_player = {"Current HP": 12}
    >>> test_enemy = {"name": "Slime", "atk": 2}
    >>> enemy_attack(test_player, test_enemy, 1)
    Slime has dealt 1 damage!
    <BLANKLINE>
    >>> test_player["Current HP"]
    11

    >>> test_player = {"Current HP": 5}
    >>> test_enemy = {"name": "Wolf", "atk": 4}
    >>> enemy_attack(test_player, test_enemy, 2)
    Wolf has dealt 2 damage!
    <BLANKLINE>
    >>> test_player["Current HP"]
    3
    """
    if "Current HP" not in player or "atk" not in enemy or "name" not in enemy:
        raise KeyError("Read my docstrings, dummy.")
    elif type(enemy["atk"]) != int or type(player["Current HP"]) != int or type(guard) != int:
        raise TypeError("Read my docstrings, dummy.")
    enemy_damage = enemy["atk"] - guard
    if enemy_damage < 0:
        enemy_damage = 0
    player["Current HP"] -= enemy_damage
    print(f'{enemy["name"]} has dealt {enemy_damage} damage!\n')


def main():
    """
    Drives the program
    """

    pass


if __name__ == "__main__":
    main()
