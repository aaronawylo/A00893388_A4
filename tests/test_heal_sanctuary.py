"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from board.rooms import heal_sanctuary


class TestHealSanctuary(TestCase):
    def test_heal_sanctuary_normal(self):
        test_player = {"Max HP": 20, "Current HP": 10}
        heal_sanctuary(test_player)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_heal_sanctuary_already_healthy(self):
        test_player = {"Max HP": 20, "Current HP": 20}
        heal_sanctuary(test_player)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_heal_sanctuary_but_im_already_dead(self):
        test_player = {"Max HP": 20, "Current HP": 0}
        heal_sanctuary(test_player)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_heal_sanctuary_is_this_technically_damage(self):
        test_player = {"Max HP": 20, "Current HP": 30000}
        heal_sanctuary(test_player)
        actual = test_player["Current HP"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_heal_sanctuary_no_current_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"Max HP": 20, "What is health?": 3}
            heal_sanctuary(test_player)

    def test_heal_sanctuary_no_integer_in_current_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 20, "Current HP": 7.2}
            heal_sanctuary(test_player)

    def test_heal_sanctuary_no_max_hp_in_player(self):
        with self.assertRaises(KeyError):
            test_player = {"What is health?": 20, "Current HP": 3}
            heal_sanctuary(test_player)

    def test_heal_sanctuary_no_integer_in_max_hp(self):
        with self.assertRaises(TypeError):
            test_player = {"Max HP": 20.5, "Current HP": 10}
            heal_sanctuary(test_player)
