"""
Aaron Lo
A0089388
"""


def attack(player: dict, enemy: dict) -> int:
    damage = player["level"] * player["atk"]
    enemy["hp"] -= damage
    print(f'You have dealt {damage} damage!')
    return 0


def defend(player: dict, _) -> int:
    print("You steel yourself for the oncoming attack!")
    return player["def"]


def potion(player: dict, _) -> int:
    player["potions"] -= 1
    player["hp"] += 5
    print(f'You drank the potion and healed 5 HP!\nYour HP is now {player["hp"]}')
    return 0


def enemy_attack(player: dict, enemy: dict, guard: int) -> None:
    enemy_damage = enemy["atk"] - guard
    player["hp"] -= enemy_damage
    print(f'{enemy["name"]} has dealt {enemy_damage} damage!')
