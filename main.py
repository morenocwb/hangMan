import random
import string

from function_clear import clear
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_size = len(chosen_word)
# end_of_game = False
life = 6
display = []
dungeon = stages[6]

for i in range(0, word_size):
    display.append("_")

print(logo)
print(dungeon)
print(f'This is your Puzzle: \n {display}')
# print(f'This is the solution \"{chosen_word}\"')
# print(word_size)

#CHECKING GUESSED LETTER
while word_size > 0 and life > 0:
# while not end_of_game: SUGERIDO PELO INSTRUTOR
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guessed_letter: str = input('Guess a letter: ').lower()
    clear()
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guessed_letter in display:
        print(f'You\'ve already guessed \"{guessed_letter}\"')
    position_letters = []
    for pos, char in enumerate(chosen_word):
        if guessed_letter == char:
            position_letters.append(pos)
    if not position_letters:
        print(f'The letter \"{guessed_letter}\" is not in the word! You lost a life!')
        life -= 1
        dungeon = stages[life]
    else:
        for pos in range(0, len(position_letters)):
            display[position_letters[pos]] = guessed_letter
            word_size -= 1
    print(dungeon)
    print(display)
#     if "_" not in display
#           end_of_game = True
#           print('You Win.')   SUGERIDO PELO INSTRUTOR


#GAME IS OVER, CHECKING RESULT
if word_size == 0:
    print('Congrats You WON!')
else:
    print('You LOSE!')