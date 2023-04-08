"""
Aaron Lo
A0089388
"""


from Movement.movement import get_user_choice, validate_move, move_character
from battle.normal_fight import fight
from character.character_modules import make_character, level_up, is_alive
from board.game_board import populate_board, import_room_templates, room_action, get_board_id, describe_current_location
from utilities.miscellaneous import check_for_foes, check_if_goal_attained


def game():
    rows = 5
    columns = 5
    board = populate_board(rows, columns)
    character = make_character()
    room_list = import_room_templates()
    achieved_goal = False
    while not achieved_goal and is_alive(character):
        room_action(get_board_id(board, character), character)
        describe_current_location(board, character, room_list)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
        else:
            print("You can't move that way!\n")
        if get_board_id(board, character) == "bossroom":
            # boss_fight(character)
            pass
        else:
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                fight(character)
        level_up(character)
        achieved_goal = check_if_goal_attained(board, character)
    else:
        if not is_alive(character):
            print("Sorry you died, GITGUD. Run the program to try again!")
        else:
            print("Congratulations, you beat the game!")


def main():

    game()


if __name__ == "__main__":
    main()
