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

ascii_letter_list = string.ascii_letters
guesses = 7
guess_word = random.choice(swords)
disp_list = list("_" * len(guess_word))
letter_list = list(guess_word)
print(disp_list)
output = []
guess = input("Which letter will you guess?")
while guesses > 0 and "_" in disp_list:
    if guess in guess_word:
        print("Nice work!")
        for i in range(len(guess_word)):
            if letter_list[i] in guess_word:
                output = guess
                print(output)
                guess = "_"
    else:
        print("Whoops. Ahaha!")
        guesses -= 1
        guess = "_"

# Debugging code, comment out after completion
# print (guess_word)
# print (ascii_letter_list)
# print (disp_list)
# print (letter_list)
