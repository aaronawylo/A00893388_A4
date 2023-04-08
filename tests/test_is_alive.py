"""
Aaron Lo
A0089388
"""
from unittest import TestCase

from character.character_modules import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_just_died(self):
        character = {"Current HP": 0}
        actual = is_alive(character)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_definitely_not(self):
        character = {"Current HP": -10}
        actual = is_alive(character)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_barely_hanging_on(self):
        character = {"Current HP": 1}
        actual = is_alive(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_healthy(self):
        character = {"Current HP": 5}
        actual = is_alive(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_immortal(self):
        character = {"Current HP": 99999999999}
        actual = is_alive(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_who_has_a_fraction_of_health(self):
        character = {"Current HP": 3.1415}
        actual = is_alive(character)
        expected = True
        self.assertEqual(actual, expected)
