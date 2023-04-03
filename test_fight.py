import json
import random

character = {"X-coordinate": 0, "Y-coordinate": 0, "hp": 20, "atk": 2, "def": 1, "level": 2, "potions": 3}
enemy_list = ('slime', 'wolf', 'knight')


def enemy_randomizer() -> str:
    beastiary_size = len(enemy_list)
    enemy_number = random.randrange(beastiary_size)
    enemy_file = enemy_list[enemy_number] + ".json"
    return enemy_file


def is_alive(player: dict) -> bool:
    """
    Return a Boolean of whether the character is alive (health above zero)

    :param player: a dictionary containing a key named "Current HP" with a number as the value
    :precondition: character must contain a key named "Current HP" with a number as the value
    :postcondition: returns a Boolean if the character is alive or not (health above zero)
    :return: a Boolean stating if the character is alive
    >>> example_player = {"hp": 5}
    >>> is_alive(example_player)
    True

    >>> example_player = {"hp": 0}
    >>> is_alive(example_player)
    False
    """
    return player["hp"] > 0


def attack(player: dict, enemy: dict) -> int:
    damage = player["level"] * player["atk"]
    enemy["hp"] -= damage
    print(f'You have dealt {damage} damage!')
    return 0


def defend(player: dict) -> int:
    print("You steel yourself for the oncoming attack!")
    return player["def"]


def potion(player: dict) -> int:
    player["potions"] -= 1
    player["hp"] += 5
    print(f'You drank the potion and healed 5 HP!\nYour HP is now {player["hp"]}')
    return 0


def enemy_attack(player: dict, enemy: dict, guard: int) -> None:
    enemy_damage = enemy["atk"] - guard
    player["hp"] -= enemy_damage
    print(f'{enemy["name"]} has dealt {enemy_damage} damage!')


def menu_print(menu: dict) -> None:
    for every in menu:
        print(str(every) + ":", menu[every])


def populate_menu(move_list: list) -> dict:
    return dict(enumerate(move_list, 1))


def valid_battle_choice(menu: dict, choice: str):
    if int(choice) not in menu:
        print("That is not a valid numeric choice, please select from the following:\n")
        return False
    else:
        return True


def potion_check(player: dict, menu: dict, choice: str):
    if choice == '3' and player["potions"] < 1:
        print("You're out of potions! Do something else!")
        return False
    else:
        return True


def action_select(player):

    test_actions = ["Attack", "Defend", "Use Potion"]
    menu = populate_menu(test_actions)
    action = False
    while not action:
        menu_print(menu)
        choice = input()
        action = valid_battle_choice(menu, choice)
        if choice == "3":
            action = potion_check(player, menu, choice)
    return choice


def player_turn(choice, player, enemy):
    if choice == "1":
        return attack(player, enemy)
    if choice == "2":
        return defend(player)
    if choice == "3":
        return potion(player)


def fight(player):

    filename = enemy_randomizer()
    with open(filename) as file_object:
        enemy = json.load(file_object)

    print(f'You have encountered {enemy["name"]}!')
    while enemy["hp"] > 0 and is_alive(player):
        print(f'Your HP is {player["hp"]}!\nThe {enemy["name"]}\'s HP is {enemy["hp"]}!')
        print("Choose an action:")
        choice = action_select(player)
        guard = player_turn(choice, player, enemy)
        if enemy["hp"] > 0:
            enemy_attack(player, enemy, guard)
    if enemy["hp"] < 1:
        print(f'You have slain {enemy["name"]}!')
    if not is_alive(player):
        print("YOU HAVE DIED.")


def main():

    fight(character)


if __name__ == "__main__":
    main()
