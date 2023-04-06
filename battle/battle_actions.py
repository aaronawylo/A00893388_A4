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
    damage = player["level"] * player["atk"]
    enemy["hp"] -= damage
    print(f'You have dealt {damage} damage!')
    return 0


def defend(player: dict, *_) -> int:
    """
    Returns the correct guard value from the player's level multiplied by defense

    :param player: a dictionary containing the keys "level" and "def"
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
    print("You steel yourself for the oncoming attack!")
    return player["level"] * player["def"]


def potion(player: dict, _) -> int:
    player["potions"] -= 1
    player["Current HP"] += 5
    healed = 5
    if player["Current HP"] > player["Max HP"]:
        healed = 5 - (player["Current HP"] - player["Max HP"])
        player["Current HP"] = player["Max HP"]
    print(f'You drank the potion and healed {healed} HP!\nYour HP is now {player["Current HP"]}')
    return 0


def enemy_attack(player: dict, enemy: dict, guard: int) -> None:
    enemy_damage = enemy["atk"] - guard
    if enemy_damage < 0:
        enemy_damage = 0
    player["Current HP"] -= enemy_damage
    print(f'{enemy["name"]} has dealt {enemy_damage} damage!')
