

def fireroom(player: dict) -> None:
    player["Current HP"] -= 5


def poisonroom(player: dict) -> None:
    player["Current HP"] -= 2


def healroom(player: dict) -> None:
    player["Current HP"] += 5
    if player["Current HP"] > player["Max HP"]:
        player["Current HP"] = player["Max HP"]


def potionroom(player: dict) -> None:
    player["potions"] += 3
    print(f"You now have {player['potions']} potions!\n")


def atkuproom(player: dict) -> None:
    player['atk'] += 1
    print(f"Your Attack is now {player['atk']}!\n")


def defuproom(player: dict) -> None:
    player['atk'] += 1
    print(f"Your Defense is now {player['def']}!\n")


def hpuproom(player: dict) -> None:
    player['Max HP'] += 20
    player['Current HP'] += 20
    print(f"Your Max HP is now {player['Max HP']}!\n")
