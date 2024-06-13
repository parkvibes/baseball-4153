class BaseballGame:
    def guess(self, guess_number):
        if guess_number is None:
            raise TypeError

        if len(guess_number) != 3:
            raise TypeError

        for c in guess_number:
            if c < '0' and c > '9':
                raise TypeError