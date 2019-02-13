import string
import random
print (list(string.ascii_letters))
print (string.digits)
print (string.punctuation)
print("Hello World!")
# What do I put here? Blah blah blah lorem ipsum dolor
cars = 5
driving = True
print("I have %d cars." %cars)
print("I have " + str(cars) + " cars.")
print("* Concatenation.")

age = input("How old are you?")
print(age + "? That's young.")

colors = ["cyan", "orange", "blue", "purple", "green", "yellow", "red"]
colors.append("pink")
# okay how do i remove something from a list without using list.remove
colors.pop(0)

print(colors)
print(colors[2])
print(len(colors))

