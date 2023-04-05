import itertools


def main():
    test_actions = ("Attack", "Defend", "Use Potion")
    enumeration = dict(enumerate(test_actions, 1))
    count = dict(zip(test_actions, itertools.repeat(10, 3)))
    print(count)
    print(enumeration)


if __name__ == '__main__':
    main()


