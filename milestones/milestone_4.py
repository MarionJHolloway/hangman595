import random

class Hangman:
    """
    This class is used to represent a game of hangman.

    Attributes:
        word (str): the word to be guessed
        word_guessed( list): a list of blanks and letters guessed so far
        num_letters (int): the number of unique letters left to guess
        num_lives (int): the number of guesses remaining
        word_list (list): the words given by the user which the computer can select from
        list_of_guesses (list): the letters already guessed by the user
    """
    def __init__(self, word_list, num_lives=5) -> None:
        """
        See help(Hangman) for accurate signature
        """
        self.word = random.choice(word_list)
        self.word_guessed:list = ['_' for letter in list(self.word)]
        self.num_letters: int = len(set(self.word) - set(self.word_guessed))
        self.num_lives: int = num_lives
        self.word_list: list = word_list
        self.list_of_guesses: list = []
    

    def ask_for_input(self):
        """
        This function prompts the user to input a single letter and responds to that input.
        """
        while True:
            guess = input("Enter a single letter.")
            self.__respond_to_input(guess)


    def __respond_to_input(self, guess):
        """
        This function decides how to respond to the user's input.

        If the guess is not a single alphabetical character, the user 
        is informed and prompted to try again. If the input has been 
        guessed previously, the user is informaed and prompted to guess 
        again. Otherwise, the guess is checked and added to the list 
        of guesses.

        Args:
            guess (str): The user's input when instructed to enter a single letter.
        """
        if not(len(guess) == 1 & guess.isalpha()):
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that")
        else:
            self.__check_guess(guess)
            self.list_of_guesses.append(guess)

    
    def __check_guess(self, guess: str) -> None:
        """
        This function decides whether the guess is in the word or not.

        The guess is converted to lowercase, then, if the guess is in the word, the user is informed and the game 
        status is updated. If the guess is not in the word, the number 
        of lives are reduced and the user is informed.

        Args:
            guess (str): a single alphabetical character
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.__update_game_status(guess)
        else:
            self.__reduce_number_of_lives()
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def __update_game_status(self, guess):
        """
        This function updates the attributes that contain the game's current status.

        The letter guessed is revealed and the number of letter left to guess is 
        updated.

        Args:
            guess (str): a single alphabetical character
        """
        self.__reveal_letter_guessed(guess)
        self.__update_number_of_letters_left_to_guess()


    def __reveal_letter_guessed(self, guess):
        """
        This function reveals where the guess is present in the word.

        The guessed letter is placed into the blank space in word_guessed.

        Args:
            guess (str): a single alphabetical character
        """
        for letter, i in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess


    def __update_number_of_letters_left_to_guess(self):
        """
        This function reduces the number of letters left to guess by one.
        """
        self.num_letters = self.num_letters - 1

    
    
    def __reduce_number_of_lives(self):
        """
        This function reduces the number of lives left by one.
        """
        self.num_lives = self.num_lives -1

game = Hangman(["mango", "grape", "pear", "peach", "banana"])
game.ask_for_input()
            
