import copy
import random


def get_template_size(templates):

    size = 0
    for every in templates:
        size += templates[every][2]
    return size


def check_template_room_count(templates, room):

    return templates[room][2] > 0


# def individual_room_population(dictionary, room):
#
#
#     dictionary[room][2] -= 1
#     if dictionary[key][2] == 0:
#         dictionary[0].delete()
#     return dictionary[key]


def create_list_of_room_ids(templates, length):

    template_list = [key for key in templates for _ in range(templates[key][2])]
    empty_number = length - len(template_list) - 2
    while empty_number > 0:
        template_list.append("emptyroom")
        empty_number -= 1
    return template_list


def populate_board(row, column):

    example_dictionary = {"poisontrap": ("The room fills with gas, you take 1 damage!", "poisontrap()", 2),
                          "healroom": ("You are bathed in a warm light, you heal 2 HP", "healroom()", 3),
                          "fireroom": ("The room is on fire, you take 2 damage!", "fireroom()", 1)}
    # example_board = {(0, 0): 'Empty Room', (1, 0): 'Empty Room', (2, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 1):
    #                  'Empty Room', (2, 1): 'Empty Room', (0, 2): 'Empty Room', (1, 2): 'Empty Room', (2, 2):
    #                  'Empty Room'}

    board_numbers = [(lateral, longitudinal) for longitudinal in range(column) for lateral in range(row)]
    print(board_numbers)
    board_length = len(board_numbers)
    room_ids = create_list_of_room_ids(example_dictionary, board_length)
    random.shuffle(room_ids)
    room_ids.insert(0, "startroom")
    room_ids.append('bossroom')
    final_board = dict(zip(board_numbers, room_ids))
    return final_board


    # rooms_to_populate = copy.deepcopy(example_dictionary)
    # total_rooms = len(example_board)
    # randomized_order = list(range(0, total_rooms))
    # random.shuffle(randomized_order)
    # room_list = []
    # for every in rooms_to_populate:
    #     room_list = room_list.append(every)
    # while rooms_to_populate:
    #     for every in randomized_order:
    #         example_board[every] = rooms_to_populate


    # rooms_to_add = len(rooms_to_populate)
    # while rooms_to_populate:
    #     random_target_room = random.randint(0, total_rooms)
        # if (example_board[random_target_room] == 'Empty Room':
        #     random_new_room = random.randint(0, rooms_to_add)
        #     pass


"""stupid stuff"""

        # for every in rooms_to_populate.values():
        #     print(every[3])


def main():

    # templates = {"poisontrap": ("The room fills with gas, you take 1 damage!", "poisontrap()", 2),
    #                       "healroom": ("You are bathed in a warm light, you heal 2 HP", "healroom()", 3),
    #                       "fireroom": ("The room is on fire, you take 2 damage!", "fireroom()", 1)}
    # room = "poisontrap"
    # print(get_template_size(templates))

    print(populate_board(5, 5))


if __name__ == "__main__":
    main()
