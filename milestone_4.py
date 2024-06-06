import random

class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
        self.word = random.choice(word_list)
        self.word_guessed:list = ['_' for letter in list(self.word)]
        self.num_letters: int = len(set(self.word) - set(self.word_guessed))
        self.num_lives: int = num_lives
        self.word_list: list = word_list
        self.list_of_guesses: list = []
    
    def check_guess(self, guess: str) -> None:
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter, i in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives -1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter.")
            if not(len(guess) == 1 & guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

game = Hangman(["mango", "grape", "pear", "peach", "banana"])
game.ask_for_input()
            