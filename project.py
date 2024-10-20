#Step 5

# Importing the modules

import random
import wordlist
import stages

# Shuffling of words

chosen_word = random.choice(wordlist.word_list)
word_length = len(chosen_word)

# Defining game logics

end_of_game = False
lives = 6

# Prints the start cool logo

print(stages.logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
used = []

# Start the game loop

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check if the word is alreaddy used
    if guess in used:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue  # Skip the rest of the loop and prompt for another guess
    else:
        used.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        elif letter in used:
            print(f"You already used {guess}")

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages.stages[lives])