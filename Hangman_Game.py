
import random
from Hangman_Words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Create a list that displays the number of letters for the chosen word.
display = []
for _ in range(word_length):
    display += "_"
end_of_game = False

# Create a user input that guesses if the randomly generated word contains a certain letter.
while not end_of_game:
    guess = input('Please guess a letter ').lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f'Current position: {position}\n'
        #       f'Current letter: {letter}\n Guessed'
        #       f'letter: {guess}')
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word."
              f"You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')
    print(display)

    if '_' not in display:
        end_of_game = True
        print('You win')
