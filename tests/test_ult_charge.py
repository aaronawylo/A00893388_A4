"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.hades import ult_charge
from unittest.mock import patch
import io


class TestUltCharge(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ult_charge_print(self, mock_output):
        test_player = {"Not": "Needed"}
        test_guard = {"Also": "Unneeded"}
        test_enemy = {"name": "Hades"}
        ult_charge(test_player, test_enemy, test_guard)
        actual = mock_output.getvalue()
        expected = "Hades is gathering a massive amount of fire!\n"
        self.assertEqual(actual, expected)

    def test_ult_charge_need_a_name(self):
        with self.assertRaises(KeyError):
            test_player = {"Not": "Needed"}
            test_guard = {"Also": "Needed"}
            test_enemy = {"Oopsies": "Poopsies"}
            ult_charge(test_player, test_enemy, test_guard)
