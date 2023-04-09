"""
Aaron Lo
A0089388
"""
from battle.battle_actions import enemy_attack
from battle.hades import boss_laugh, ult_charge, ult_move
from battle.normal_fight import action_select, player_turn
from character.character_modules import is_alive
from utilities.miscellaneous import open_json_file
from itertools import cycle


def boss_fight(player):

    boss = open_json_file("data/hades.json")
    attack_pattern = cycle([enemy_attack, boss_laugh, enemy_attack, ult_charge, ult_move])
    print(f'{boss["name"]} stands before you.')
    while boss["hp"] > 0 and is_alive(player):
        print(f'Your HP is {player["Current HP"]}/{player["Max HP"]}!\n{boss["name"]}\'s HP is {boss["hp"]}!\n'
              f'You have {player["potions"]} potions in your bag!\n\nChoose an action:')
        choice = action_select(player)
        guard = player_turn(int(choice), player, boss)
        if boss["hp"] > 0:
            next(attack_pattern)(player, boss, guard)
    if boss["hp"] < 1:
        print(f'{boss["name"]} screams out in agony and fades into nothingness...')
    else:
        print(f"YOU HAVE DIED.")
