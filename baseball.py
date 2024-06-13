from baseball_result import *
class BaseballGame:

    def __init__(self):
        self.question = ""
    def guess(self, guess_number):
        self.check_input_validity(guess_number)
        return BaseballGameResult(True, 3, 0)

    def check_input_validity(self, guess_number):
        if guess_number is None:
            raise TypeError
        if len(guess_number) != 3:
            raise TypeError
        for c in guess_number:
            if not c.isdigit():
                raise TypeError
        if self.check_duplication(guess_number):
            raise TypeError

    def check_duplication(self, guess_number):
        return guess_number[0] == guess_number[1] or \
            guess_number[1] == guess_number[2] or \
            guess_number[0] == guess_number[2]

