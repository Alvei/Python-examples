""" General class to guess an integer. """


class GuessNumber:
    def __init__(self, number: int, minimum: int = 0, maximum: int = 100):
        """ Initialize. """
        self.number = number
        self.guesses: int = 0  # Counts the number of guesses taken
        self.min = minimum
        self.max = maximum

    def get_guess(self) -> int:
        """ Ask user to guess a number. """
        guess = input(f"Please guess a number ({self.min} - {self.max}) ")
        if self.valid_int(guess):
            return int(guess)
        else:
            print(f"Please enter a valid number!")
            return get_guess()  # Recursive

    def valid_int(self, str_number: str) -> bool:
        " Conduct two checks on the number received from input() function. "
        try:
            number = int(str_number)
        except:
            return False

        # Second check for validity of range
        return self.min <= number <= self.max

    def play(self):
        """ Main method. """
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print(f"Your guess was under.")
            elif guess > self.number:
                print(f"Your guess was above.")
            else:
                break  # They guessed it

        print(f"You guessed it in {self.guesses} guesses")


game = GuessNumber(56)
game.play()
