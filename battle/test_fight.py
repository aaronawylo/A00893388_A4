"""
Aaron Lo
A0089388
"""
import json
import random
import os

from battle.battle_actions import attack, defend, potion, enemy_attack
from character.character import is_alive
from utilities.miscellaneous import populate_menu, menu_print

character = {"X-coordinate": 0, "Y-coordinate": 0, "hp": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}





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


def potion_check(player: dict, choice: str):
    if choice == '3' and player["potions"] < 1:
        print("You're out of potions! Do something else!")
        return False
    else:
        return True


def action_select(player: dict) -> str:

    test_actions = ("Attack", "Defend", "Use Potion")
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
    modes = (attack, defend, potion)
    return modes[choice-1](player, enemy)


def fight(player):

    filename = enemy_randomizer("master_list.json")
    with open(filename) as file_object:
        enemy = json.load(file_object)

    print(f'You have encountered {enemy["name"]}!')
    while enemy["hp"] > 0 and is_alive(player):
        print(f'Your HP is {player["hp"]}!\nThe {enemy["name"]}\'s HP is {enemy["hp"]}!')
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
