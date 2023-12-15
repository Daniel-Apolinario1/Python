# ---------------------------------------------------------------
#            %%%%%      DAY SEVEN PROJECT      %%%%%
# ---------------------------------------------------------------

import random
import hangman_images
import hangman_words

#  Defining variables
chosen_word = random.choice(hangman_words.word_list)  # Select a word from the word_list
display = []  # List with all the underscores to match the size of the word
word_length = int(len(chosen_word))
end_game = False
lives = 6
guesses = []


# The Game
print(hangman_images.logo)
for characters in range(word_length):  # Defines the number of underscores to print
    display.append("_")
print(display)

while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess not in guesses:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed the letter {guess}, that's not in the word. You lose a life :(")
            print(hangman_images.stages[lives])
            guesses.append(guess)
        else:
            print(f"You guessed the letter {guess}, that was a good guess!")
            print(hangman_images.stages[lives])
            guesses.append(guess)
        string = " ".join(display)
        print(string)

        if "_" in display:
            end_game = False
        else:
            print(f'You Win, the word was : "{chosen_word}".')
            end_game = True

        if lives == 0:
            print(f'You Lose, the word was : "{chosen_word}".')
            end_game = True
    else:
        print(f"You've already guessed {guess}.")
