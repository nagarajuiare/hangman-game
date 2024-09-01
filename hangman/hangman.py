import random
import string
from words import words  # Ensure 'words.py' exists in the same directory

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # Fixed the condition
        word = random.choice(words)
    return word.upper()  # Convert the word to uppercase to match user input

def hangman():
    word  = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)  # Contains all the uppercase letters
    used_letters = set()  # Keep track of guessed letters
    max_guess = len(word) + 5
    print(f"Maximum {max_guess} guesses you can make!")
    while len(word_letters) > 0 and max_guess > 0:

        print('You have used these letters:', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()  # User guesses a letter

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Add the valid guess to used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove the letter from the remaining letters
                print(f'Good guess! {user_letter} is in the word.')
            else:
                max_guess -= 1 # deduced one chance.

        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')

        else:
            print("Invalid character. Please try again.")

        # print(f"You have {max_guess} chance{"s" if max_guess > 1 else ''} left!")
        print(f"You have {max_guess} chance{'s' if max_guess != 1 else ''} left!")

    if len(word_letters) == 0:
        print(f"Congratulations! You guessed the word {word} correctly!")
    else:
        print(f"Sorry! you ran out the guess. The word was {word}")
hangman()

