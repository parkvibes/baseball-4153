from unittest import TestCase
from baseball import BaseballGame as Game

class TestGame(TestCase):
    def test_exception_when_input_is_none(self):
        game = Game()
        with self.assertRaises(TypeError):
            game.guess(None)