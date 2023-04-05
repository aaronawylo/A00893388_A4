"""
Aaron Lo
A0089388
"""
import json
import random

from battle.battle_actions import attack, defend, potion, enemy_attack
from character.character import is_alive
from utilities.miscellaneous import populate_menu, menu_print, open_json_file

character = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1,
             "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}


def enemy_randomizer(file_name) -> str:
    """
    Gives a random string of an enemy file location in the beastiary

    :param file_name: the name of a json file
    :precondition: file_name must exist
    :precondition: file_name must be the name of a json file
    :precondition: file_name must have a key named 'enemies'
    :precondition: file-name must have values attached to 'enemies' of a list of strings of enemies
    :postcondition: returns a string denoting the name of an enemy file
    :return: a string denoting the name of an enemy file
    """

    master_list = open_json_file(file_name)
    if 'enemies' not in master_list:
        raise KeyError("You don't have enemies")
    else:
        enemy_list = master_list['enemies']
        beastiary_size = len(enemy_list)
        enemy_number = random.randrange(beastiary_size)
        enemy_file = enemy_list[enemy_number] + ".json"
        return enemy_file


def valid_battle_choice(menu: dict, choice: str):
    """
    """
    try:
        choice = int(choice)
    except ValueError:
        print("That is not a valid numeric choice, please select from the following:")
        return False
    else:
        if int(choice) not in menu:
            print("That is not a valid numeric choice, please select from the following:")
            return False
        else:
            return True


def potion_check(player: dict, choice: str) -> bool:
    if "potions" not in player:
        raise KeyError("Make a better character!")
    else:
        if choice == '3' and player["potions"] < 1:
            print("You're out of potions! Do something else!")
            return False
        else:
            return True


def character_actions(player: dict) -> list:
    """
    Returns a list of the player's possible actions in battle

    :param player: a dictionary containing a key labelled "Battle Actions"
    :precondition: player must contain a key labelled "Battle Actions"
    :postcondition: returns the list value associated with "Battle Actions"
    :return: a list of the player's possible actions
    >>> test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, \
    "level": 1, "potions": 3, "Battle Actions": ['Attack', 'Defend', 'Use Potion']}
    >>> character_actions(test_player)
    ['Attack', 'Defend', 'Use Potion']

    >>> test_player = {"Battle Actions": ['Attack', 'Defend', 'Use Potion', 'Secret Move: Ultimate World Breaker']}
    >>> character_actions(test_player)
    ['Attack', 'Defend', 'Use Potion', 'Secret Move: Ultimate World Breaker']
    """

    if "Battle Actions" not in player:
        raise KeyError("Make a better character!")
    else:
        return player["Battle Actions"]


def action_select(player: dict) -> str:
    """
    Returns an string between

    :param player:
    :return:
    """
    test_actions = character_actions(player)
    menu = populate_menu(test_actions)
    action = False
    choice = None
    while not action:
        menu_print(menu)
        choice = input()
        action = valid_battle_choice(menu, choice)
        if choice == "3":
            action = potion_check(player, choice)
    return choice


def player_turn(choice: int, player: dict, enemy: dict):
    """
    Returns the function according to the choice that was made

    :param choice: an int between the numbers 1 through 3 inclusive
    :param player: a dictionary that has keys "Max HP", "Current HP", "atk", "def", "level" and  "potions"
    :param enemy: a dictionary containing keys labelled "name", "hp", "atk" and "exp"
    :precondition: choice must be an int between 1 and 3
    :precondition: player must have keys of "Max HP", "Current HP", "atk", "def", "level" and  "potions"
    :precondition: enemy must contain keys labelled "name", "hp", "atk" and "exp"
    :postcondition: returns the function chosen by the player
    :return: a function that the player has chosen to act
    >>> test_player = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3, "Battle Actions": ["Attack", "Defend", "Use Potion"]}
    >>> test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
    >>> player_turn(1, test_player, test_enemy)
    attack(test_player, test_enemy)
    """

    modes = (attack, defend, potion)
    return modes[choice-1](player, enemy)


def fight(player):

    filename = enemy_randomizer("master_list.json")
    with open(filename) as file_object:
        enemy = json.load(file_object)

    print(f'You have encountered {enemy["name"]}!')
    while enemy["hp"] > 0 and is_alive(player):
        print(f'Your HP is {player["Current HP"]}!\nThe {enemy["name"]}\'s HP is {enemy["hp"]}!')
        print("Choose an action:")
        choice = action_select(player)

        guard = player_turn(int(choice), player, enemy)
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