
character = {"X-coordinate": 0, "Y-coordinate": 0, "hp": 20, "atk": 2, "def": 1, "level": 2, "potions": 3}
slime = {"name": "Slime", "hp": 10, "atk": 2}


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


def player_action(player):

    actions = ["1", "2", "3"]
    choice = input("1: Attack\n2: Defend\n3: Use Potion\n")
    action = False
    while not action:
        if choice not in actions:
            print("That is not a valid numeric choice, please select from the following:")
            choice = input("1: Attack\n2: Defend\n3: Use Potion")
        elif choice == "3":
            if player["potions"] < 1:
                choice = input("You're out of potions! Do something else!\n1: Attack\n2: Defend\n3: Use Potion")
            else:
                action = True
        else:
            action = True
    return choice


def fight(player, enemy):

    print(f'You have encountered {enemy["name"]}!')
    while enemy["hp"] > 0 and is_alive(player):
        guard = 0
        print(f'Your HP is {player["hp"]}!\nThe {enemy["name"]}\'s HP is {enemy["hp"]}!')
        print("Choose an action:")
        choice = player_action(player)
        if choice == "1":
            attack = player["level"] * player["atk"]
            enemy["hp"] -= attack
            print(f'You have dealt {attack} damage!')
        elif choice == "2":
            guard = player["def"]
            print("You steel yourself for the oncoming attack!")
        else:
            player["potions"] -= 1
            player["hp"] += 5
            print(f'You drank the potion and healed 5 HP!\nYour HP is now {player["hp"]}')
        if enemy["hp"] > 0:
            enemy_damage = enemy["atk"] - guard
            player["hp"] -= enemy_damage
            print(f'{enemy["name"]} has dealt {enemy_damage} damage!')
    if enemy["hp"] < 1:
        print(f'You have slain {enemy["name"]}!')
    if not is_alive(player):
        print("YOU HAVE DIED.")


def main():

    fight(character, slime)


if __name__ == "__main__":
    main()
