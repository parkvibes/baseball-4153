from baseball_result import *


class BaseballGame:

    def __init__(self):
        self.question = ""

    def guess(self, guess_number):
        self.check_input_validity(guess_number)
        if self.is_solved(guess_number):
            return self.get_success_baseballgame_result()
        else:
            return self.get_unsolved_baseballgame_result(guess_number)

    def get_unsolved_baseballgame_result(self, guess_number):
        strikes = 0
        balls = 0
        for idx in range(len(guess_number)):
            if guess_number[idx] == self.question[idx]:
                strikes += 1
            elif self.question.find(guess_number[idx]) > -1:
                balls += 1
        return BaseballGameResult(False, strikes, balls)

    def get_success_baseballgame_result(self):
        return BaseballGameResult(True, 3, 0)

    def is_solved(self, guess_number):
        return self.question == guess_number

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
