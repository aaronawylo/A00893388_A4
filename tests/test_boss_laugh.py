"""
Aaron Lo
A0089388
"""
from unittest import TestCase
from battle.hades import boss_laugh
from unittest.mock import patch
import io


class TestBossLaugh(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_laugh_print(self, mock_output):
        test_player = {"Not": "Needed"}
        test_guard = {"Also": "Unneeded"}
        test_enemy = {"name": "Hades"}
        boss_laugh(test_player, test_enemy, test_guard)
        actual = mock_output.getvalue()
        expected = "Hades doubles over in laughter at your feeble attempt.\n"
        self.assertEqual(actual, expected)

    def test_boss_laugh_need_a_name(self):
        with self.assertRaises(KeyError):
            test_player = {"Not": "Needed"}
            test_guard = {"Also": "Needed"}
            test_enemy = {"Oopsies": "Poopsies"}
            boss_laugh(test_player, test_enemy, test_guard)
