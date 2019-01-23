import random
import string
import os
import wave
swords = ["Adventure", "Alone", "Amazing", "Awesome", "Bed", "Beauty", "Bliss", "Broken", "Calm", "Charm", "Cheer",
          "Childhood", "Clumsy", "Color", "Comfort", "Cry", "Dance", "Dark", "Daydream", "Dazzle", "Death", "Defeat",
          "Depression", "Embrace", "Empty", "Excitement", "Extraordinary", "Family", "Fear", "Feather", "Fireflies",
          "Fireworks", "Flower", "Flying", "Forgive", "Friends", "Fun", "Grief", "Happiness", "Heart", "Holiday",
          "Hope", "Hopeless", "Hurt", "Joy", "Laugh", "Lazy", "Loud", "Love", "Lucky", "Marriage", "Memories", "Misery",
          "Misfortune", "Music", "Nature", "Ocean", "Passion", "Peaceful", "Pain", "Party", "Play", "Prayer",
          "Precious", "Promise", "Rainbow", "Raincloud", "Romance", "Rose", "Sadness", "Scars", "Shame", "Silly",
          "Sing", "Smile", "Sparkle", "Special", "Sunny", "Sunset", "Sweet", "Tears", "Together", "Tragedy", "Treasure",
          "Unrequited", "Vacation", "Warm", "Wonderful"]

full_list = []
ascii_letter_list = string.ascii_letters
guesses = 7
guess_word = random.choice(swords)
word_person = "Sayori"
hint = [str(word_person) + " would like this word the most."]
disp_list = list("_" * len(guess_word))
letter_list = list(guess_word)
print(disp_list)
output = []

while guesses > 0 and "_" in disp_list:
    guess = input("Which letter will you guess?")
    for i in range(len(guess_word)):
        if guess_word[i] in guess:
            print("Nice work!")
            # output.append(letter_list[i])
            output = guess
            print(output)
            guess = "_"
        else:
            print("Whoops. Ahaha!")
            # output.append(disp_list[i])
            guesses -= 1

# Debugging code, comment out after completion
print(guess_word)
print(ascii_letter_list)
print(disp_list)
print(letter_list)
