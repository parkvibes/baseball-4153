class BaseballGame:
    def guess(self, guess_number):
        if guess_number is None:
            raise TypeError

        if len(guess_number) != 3:
            raise TypeError

        for c in guess_number:
            if not c.isdigit():
                raise TypeError
