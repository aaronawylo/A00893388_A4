import os
import json


def menu_print(menu: dict) -> None:
    for every in menu:
        print(str(every) + ":", menu[every])


def populate_menu(menu_list: list) -> dict:
    return dict(enumerate(menu_list, 1))


def open_json_file(file_name: str) -> dict:
    if not os.path.isfile(file_name):
        raise FileNotFoundError("Your file doesn't exist :)")
    else:
        with open(file_name) as file_object:
            loaded_json = json.load(file_object)
        return loaded_json
