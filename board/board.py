"""
Aaron Lo
A0089388
"""

import random

from board.rooms import fireroom, poisonroom, healroom, potionroom, atkuproom, defuproom, hpuproom
from utilities.miscellaneous import open_json_file


def room_action(room_name: str, player: dict):
    room_actions = {"fireroom": fireroom, "poisonroom": poisonroom, "healroom": healroom, "potionroom": potionroom,
                    "atkuproom": atkuproom, "defuproom": defuproom, "hpuproom": hpuproom}
    if room_name in room_actions:
        return room_actions[room_name](player)
    else:
        return


def import_room_templates() -> dict:
    dynamics_to_add = open_json_file('rooms.json')
    statics_to_add = open_json_file('static_rooms.json')
    for every, item in statics_to_add.items():
        dynamics_to_add[every] = item
    return dynamics_to_add


def create_list_of_room_ids(templates, length):

    template_list = [key for key in templates for _ in range(templates[key][2])]
    empty_number = length - len(template_list) - 2
    while empty_number > 0:
        template_list.append("emptyroom")
        empty_number -= 1
    return template_list


def populate_board(row, column):

    example_dictionary = open_json_file('rooms.json')
    board_numbers = [(lateral, longitudinal) for longitudinal in range(column) for lateral in range(row)]
    board_length = len(board_numbers)
    room_ids = create_list_of_room_ids(example_dictionary, board_length)
    random.shuffle(room_ids)
    room_ids.insert(0, "startroom")
    room_ids.append('bossroom')
    final_board = dict(zip(board_numbers, room_ids))
    return final_board


def main():

    print(populate_board(5, 5))


if __name__ == "__main__":
    main()