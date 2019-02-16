import random
words = ["Apple", "Banana", "Crayon", "Depth", "Earthbound", "Fire", "Gasp", "Horse", "Impossible", "Joke", "Keep",
         "Lemon", "Mother", "Nobody", "Ocean", "Pleasing", "Quick", "Repeat", "Stay", "Test", "Under", "Violet",
         "Weather", "Xylophone", "You", "Zebra"]
full_list = []
guesses_left = 7
guess_word = random.choice(words).lower()
player_input = None
guessed_letters = []
word_guessed = []
for char in guess_word:
    word_guessed.append("_")

while guesses_left > 1 and "_" in word_guessed:
    print("You have " + str(guesses_left) + " guesses left.")
    join_guess = "".join(word_guessed)
    print(join_guess)

    try:
        player_input = str(input("Please input a letter from A to Z.")).lower()
    except:
        print("That isn't a valid input. Try again?")
        continue
    else:
        if not player_input.isalpha():  # Check if the guess is not a letter
            print("That isn't a letter. Try again?")
            continue
        elif len(player_input) > 1:  # Check if the guess is more than one letter
            print("That's more than one letter. Try again?")
            continue
        elif player_input in guessed_letters:  # Check if the letter's already guessed
            print("You've already guessed that letter. I won't take any points off, but don't do that.")
            continue
        else:
            pass
    guessed_letters.append(player_input)

    for char in range(len(guess_word)):
        if player_input == guess_word[char]:  # If your guessed letter matches a letter in the word
            word_guessed[char] = player_input  # Replace all the letters that match with your guessed letter
    if player_input not in guess_word:
        guesses_left -= 1
        print("Whoops! That wasn't in the word.")

    if "_" not in word_guessed:
        print("Congrats! " + str(guess_word) + " was the word.")
    elif guesses_left == 0:
        print("Looks like you're out of guesses. " + str(guess_word) + " was the word.")
    else:
        pass

while guesses_left == 1 and "_" in word_guessed:
    print("Only 1 guess left! Choose carefully!")
    join_guess = "".join(word_guessed)
    print(join_guess)

    try:
        player_input = str(input("Please input a letter from A to Z.")).lower()
    except:
        print("That isn't a valid input. Try again?")
        continue
    else:
        if not player_input.isalpha():  # Check if the guess is not a letter
            print("That isn't a letter. Try again?")
            continue
        elif len(player_input) > 1:  # Check if the guess is more than one letter
            print("That's more than one letter. Try again?")
            continue
        elif player_input in guessed_letters:  # Check if the letter's already guessed
            print("You've already guessed that letter. I won't take any points off, but don't do that.")
            continue
        else:
            pass
    guessed_letters.append(player_input)

    for char in range(len(guess_word)):
        if player_input == guess_word[char]:  # If your guessed letter matches a letter in the word
            word_guessed[char] = player_input  # Replace all the letters that match with your guessed letter
    if player_input not in guess_word:
        guesses_left -= 1
        print("Whoops! That wasn't in the word.")

    if "_" not in word_guessed:
        print("Congrats! " + str(guess_word) + " was the word.")
    elif guesses_left == 0:
        print("Looks like you're out of guesses. " + str(guess_word) + " was the word.")
    else:
        pass