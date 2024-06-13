class BaseballGame:
    def guess(self, guess_number):
        if guess_number is None:
            raise TypeError

        if len(guess_number) != 3:
            raise TypeError

        for c in guess_number:
            if not c.isdigit():
                raise TypeError

        if guess_number[0] == guess_number[1] or guess_number[1] == guess_number[2] or guess_number[0] == guess_number[2]:
            raise TypeError
