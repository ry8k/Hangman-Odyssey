

# 🎮 Hangman Game 🚀

## 📦 **Importing Modules**
- `random`: To select a random word.
- `wordlist`: Contains the list of possible words.
- `stages`: Holds the visual representations of the hangman.

## 🔀 **Shuffling Words**
- **Select Word**: Randomly choose a word from `wordlist.word_list`.
- **Word Length**: Determine the length of the chosen word.

## 🕹️ **Defining Game Logic**
- **Game State**: Initialize `end_of_game` as `False`.
- **Lives**: Set the number of lives to `6`.

## 🎨 **Display Logo**
- **Start Screen**: Print the game logo from `stages.logo` to welcome players.

## ✍️ **Initialize Display**
- **Blanks Creation**: Create a list of underscores `_` representing each letter in the chosen word.
- **Used Letters**: Initialize an empty list `used` to track guessed letters.

## 🔄 **Game Loop**
1. **Input Guess**: Prompt the user to guess a letter.
2. **Check Usage**:
   - If the letter has already been guessed, notify the user and prompt again.
   - Otherwise, add the letter to the `used` list.
3. **Update Display**:
   - Iterate through each letter in the chosen word.
   - If the guessed letter matches, reveal it in the `display`.
4. **Incorrect Guess Handling**:
   - If the guessed letter isn't in the word, decrement `lives` by 1.
   - If `lives` reach `0`, end the game with a loss message.
5. **Show Progress**:
   - Display the current state of the word with guessed letters revealed.
6. **Win Condition**:
   - If all letters are guessed (`_` not in `display`), end the game with a win message.
7. **Visual Update**:
   - Print the current hangman stage from `stages.stages[lives]`.

## 🏁 **Game End**
- **Win**: Congratulate the player for guessing the word correctly.
- **Lose**: Inform the player they've run out of lives.

---

## 🛠️ **Example Code Snippet**
```py
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

# Create blanks
display = ["_" for _ in range(word_length)]
used = []

# Start the game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in used:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue
    else:
        used.append(guess)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    # Show current progress
    print(' '.join(display))
    
    # Check win condition
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    # Show hangman stage
    print(stages.stages[lives])
```

## 🎯 **Features**
- **Random Word Selection**: Ensures a unique game experience each time.
- **User Input Validation**: Prevents repeated guesses and provides feedback.
- **Visual Feedback**: Displays the hangman stages and word progress.
- **Win/Lose Conditions**: Clearly informs the player of the game's outcome.

---

Feel free to customize and enhance this to fit your project's needs! Happy coding! 🚀✨
