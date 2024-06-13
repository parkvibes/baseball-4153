from unittest import TestCase
from baseball import BaseballGame as Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)

    def test_exception_when_input_length_is_unmatched(self):
        with self.assertRaises(TypeError):
            self.game.guess("12")