from unittest import TestCase
from battle.test_fight import enemy_randomizer
from unittest.mock import patch
import io


class TestEnemyRandomizer(TestCase):

    @patch('os.path.isfile')
    @patch('builtins.open', return_value=io.StringIO('{ "enemies": ["slime", "wolf", "knight"]}'))
    @patch('random.randrange', return_value=0)
    def test_enemy_randomizer(self, _, __, os_mock):
        os_mock.path.isfile.return_value = True
        actual = enemy_randomizer('master_list.json')
        expected = 'slime.json'
        self.assertEqual(actual, expected)

    @patch('os.path.isfile')
    def test_enemy_randomizer(self, os_mock):
        os_mock.path.isfile.return_value = False
        with self.assertRaises(FileNotFoundError):
            enemy_randomizer("oopsies")

    @patch('os.path.isfile')
    @patch('builtins.open', return_value=io.StringIO('{ "creampuffs": ["slime", "wolf", "knight"]}'))
    def test_enemy_randomizer(self, _, os_mock):
        os_mock.path.isfile.return_value = True
        with self.assertRaises(KeyError):
            enemy_randomizer("oopsies")
