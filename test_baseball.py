from unittest import TestCase
from baseball import BaseballGame as Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def assert_illegal_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
        except TypeError:
            pass

    def test_exception_when_input_is_invalid(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")