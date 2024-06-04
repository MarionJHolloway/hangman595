import random

def validate_guess(guess) -> None:
    if len(guess) == 1 & guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That's not a valid input.")

def select_random_word() -> str:
    word_list = ["mango", "grape", "pear", "peach", "banana"]
    return random.choice(word_list)

def main():
    select_random_word()

    guess = input("Enter a single letter.")
    validate_guess(guess)


if __name__ == "__main__":
    main()