import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

number = int(input("How many letters do you want?"))

for i in range(0, number):

                print(random.choice(letters))

input()
