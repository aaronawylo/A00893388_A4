"""
Aaron Lo
A0089388
"""
import json
import random

from battle.battle_actions import attack, defend, potion, enemy_attack
from character.character_modules import is_alive
from utilities.miscellaneous import populate_menu, menu_print, open_json_file

character = {"X-coordinate": 0, "Y-coordinate": 0, "Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1,
             "potions": 3, "exp": 0, "Battle Actions": ["Attack", "Defend", "Use Potion"]}


def enemy_randomizer(file_name) -> str:
    """
    Gives a random string of an enemy file

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


def valid_battle_choice(menu: dict, choice: str) -> bool:
    """
    Returns a Boolean if the choice typed in is a key in the menu

    :param menu: a dictionary with integers as keys
    :param choice: a string
    :precondition: menu must contain integers as keys
    :precondition: choice must be a string
    :postcondition: returns a Boolean stating if the choice entered exists in the menu
    :return: a Boolean stating if the choice entered exists in the menu
    >>> test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
    >>> valid_battle_choice(test_menu, "1")
    True

    >>> test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
    >>> valid_battle_choice(test_menu, "4")
    That is not a valid numeric choice, please select from the following:
    False

    >>> test_menu = {1: "Attack", 2: "Defend", 3: "Use Potion"}
    >>> valid_battle_choice(test_menu, "I can't read")
    That is not a valid numeric choice, please select from the following:
    False
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
    """
    Returns a Boolean if a potion exists to be used

    :param player: a dictionary containing the key "potions"
    :param choice: a string of an integer between 1 and 3
    :precondition: player must contain a key named "potions"
    :precondition: choice must be a string
    :postcondition: returns a Boolean stating if a potion is available to use
    :return: a Boolean stating if a potion is available to use
    >>> test_player = {"potions": 3}
    >>> test_choice = '3'
    >>> potion_check(test_player, test_choice)
    True

    >>> test_player = {"potions": 0}
    >>> test_choice = '3'
    >>> potion_check(test_player, test_choice)
    You're out of potions! Do something else!
    False

    >>> test_player = {"potions": 0}
    >>> test_choice = '1'
    >>> potion_check(test_player, test_choice)
    True
    """
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
    Returns a string of an integer

    :param player: a dictionary containing the keys "potions" and "Battle Actions"
    :precondition: player must contain the keys "potions" and "Battle Actions"
    :precondition: player's "Battle Actions" must have a value of a list containing actions
    :postcondition: returns a string of an integer
    :return: a string of an integer
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
    >>> test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
    >>> test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
    >>> player_turn(1, test_player, test_enemy)
    You have dealt 2 damage!
    0

    >>> test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
    >>> test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
    >>> player_turn(2, test_player, test_enemy)
    You steel yourself for the oncoming attack!
    1


    >>> test_player = {"Max HP": 20, "Current HP": 20, "atk": 2, "def": 1, "level": 1, "potions": 3}
    >>> test_enemy = {"name": "Slime", "hp": 10, "atk": 2, "exp": 20}
    >>> player_turn(3, test_player, test_enemy)
    You drank the potion and healed 0 HP!
    Your HP is now 20!
    0
    """

    modes = (attack, defend, potion)
    return modes[choice-1](player, enemy)


def fight(player):

    filename = enemy_randomizer("master_list.json")
    with open(filename) as file_object:
        enemy = json.load(file_object)

    print(f'You have encountered {enemy["name"]}!')
    while enemy["hp"] > 0 and is_alive(player):
        print(f'Your HP is {player["Current HP"]}/{player["Max HP"]}!\nThe {enemy["name"]}\'s HP is {enemy["hp"]}!\n')
        print("Choose an action:")
        choice = action_select(player)
        guard = player_turn(int(choice), player, enemy)
        if enemy["hp"] > 0:
            enemy_attack(player, enemy, guard)

    if enemy["hp"] < 1:
        print(f'You have slain {enemy["name"]}!')
        player["exp"] += enemy["exp"]
        print(f'You have gained {enemy["exp"]} EXP!\n')
    else:
        print("YOU HAVE DIED.")


def main():

    fight(character)


if __name__ == "__main__":
    main()
