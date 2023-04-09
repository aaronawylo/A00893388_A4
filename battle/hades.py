"""
Aaron Lo
A0089388
"""


def boss_laugh(_, enemy: dict, ___) -> None:
    print(f"{enemy['name']} doubles over in laughter at your feeble attempt.")


def ult_charge(_, enemy: dict, ___) -> None:
    print(f"{enemy['name']} is gathering a massive amount of fire!")


def ult_move(player: dict, enemy: dict, guard: int) -> None:
    if "Current HP" not in player or "atk" not in enemy or "name" not in enemy:
        raise KeyError("Read my docstrings, dummy.")
    elif type(enemy["atk"]) != int or type(player["Current HP"]) != int or type(guard) != int:
        raise TypeError("Read my docstrings, dummy.")
    enemy_damage = (enemy["atk"] * 10) - guard
    if enemy_damage < 0:
        enemy_damage = 0
    player["Current HP"] -= enemy_damage
    print(f'{enemy["name"]} unleashes all of his built up energy!\n{enemy["name"]} has dealt {enemy_damage} damage!')
