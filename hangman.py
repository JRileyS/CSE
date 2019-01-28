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
test = ["TTTT"]

full_list = []
ascii_letter_list = string.ascii_letters
guesses = 7
guess_word = random.choice(swords)
word_person = "Sayori"
hint = [str(word_person) + " would like this word the most."]
disp_list = list("_" * len(guess_word))
letter_list = list(guess_word)
print(hint)
print(disp_list)
output = []

while guesses > 0 and "_" in disp_list:
    guess = input("Which letter will you guess?")
    for character in guess_word:
        if character == "e":
            # replace with a _
            print("Nice work!")
            currrent_index = letter_list.index(character)
            disp_list.pop(currrent_index)
            disp_list.insert(currrent_index, "e")

# Debugging code, comment out after completion
print(guess_word)
print(ascii_letter_list)
print(disp_list)
print(letter_list)
