

def fire_room(player: dict) -> None:
    player["Current HP"] -= 5


def poison_room(player: dict) -> None:
    player["Current HP"] -= 2


def heal_room(player: dict) -> None:
    player["Current HP"] += 5
    if player["Current HP"] > player["Max HP"]:
        player["Current HP"] = player["Max HP"]


def potion_room(player: dict) -> None:
    player["potions"] += 3
    print(f"You now have {player['potions']} potions!\n")


def atk_up_room(player: dict) -> None:
    player['atk'] += 1
    print(f"Your Attack is now {player['atk']}!\n")


def def_up_room(player: dict) -> None:
    player['atk'] += 1
    print(f"Your Defense is now {player['def']}!\n")


def hp_up_room(player: dict) -> None:
    player['Max HP'] += 20
    player['Current HP'] += 20
    print(f"Your Max HP is now {player['Max HP']}!\n")
