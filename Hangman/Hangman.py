import random
word_list = ["Apple", "Banana", "Orange", "Mango"]

# Step1- Randomly choose a word from the word_list
chosen_word = random.choice(word_list).lower()
print(chosen_word)
word_length = len(chosen_word)

# Setting the number of lives
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']  # stages are in descending order

# Creating a list with as many letters as the chosen_word but with underscore
display =[]
for letter in chosen_word:
  display.append("_")
print(display)

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower() # Ask the user to guess a letter

  # Checking the guessed letter
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter # adding the correct letter to its position
  print(display)

  if guess not in chosen_word:
      lives -= 1  # taking out lives for every wrong letter guessed
      if lives == 0:
          end_of_game = True  # end while loop if all lives are lost
          print("You loose")

  print(f"{ ' '.join(display)}")

  # adding the logic how to come out of while loop
  if "_" not in display:
    end_of_game = True
    print("You win")

  print(stages[lives])