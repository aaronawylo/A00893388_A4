

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

