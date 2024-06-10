# Hangman

1. [Introduction](#introduction)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [File Structure](#file-structure)
5. [License Information](#license-information)

## Introduction
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
### What does Hangman do?
Hangman selects a random word form a list.
It asks the user to guess a letter.
If the input is not one letter of the alphabet, the user is prompted to enter a single alphabetical character.
If the input has already been guessed, the user is prompted to try a different letter.
It checks if the letter is in the word. If the guess is correct, the user is informed, and the blank word and number of characters to guess are updated. If the guess is incorrect, the number of lives is reduced and the user is informed. Regardless of whether the guess is correct or not, it is logged so that repeat guesses can be checked.
If the user guesses all the letters correctly before they run out of lives, they win. If the run out of lives before they can guess all the letters correctly, they lose.


### What was the aim?
The aim of the porject was to demonstrate the skills learned to date on the AICore course.

### What did I learn?
I learned how to write and debug classes to create an interactive command line game. I documented my code and created this README file.

## Installation Instructions
### Necessary software
- git
- VSCode (or other IDE)


### Environment setup
1. Clone the repository
```
git clone https://github.com/MarionJHolloway/hangman595.git
```
2. Open repository in VSCode

### Installing dependancies
This project does not require any dependancies. 


## Usage Instructions
In the command line type:
```
python3 milestone_5.py
```
When prompted, type a single letter you think is in the word. 


## File Structure
* [hangman](./hangman/)
    * [milestone_2.py](./hangman/milestone_2.py)
    * [milestone_3.py](./hangman/milestone_3.py)
    * [milestone_4.py](./hangman/milestone_4.py)
    * [milestone_5.py](./hangman/milestone_5.py)
* [README.md](README.md)


## License Information
GNU General Public License (GPL) v3.0