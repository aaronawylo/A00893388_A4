

def fireroom(player: dict) -> None:
    player["Current HP"] -= 5


def poisonroom(player: dict) -> None:
    player["Current HP"] -= 2


def healroom(player: dict) -> None:
    player["Current HP"] += 5


def potionroom(player: dict) -> None:
    player["potions"] += 3
    print(f"You now have {player['potions']} potions!")

