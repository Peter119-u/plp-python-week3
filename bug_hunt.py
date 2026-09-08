# BUG: Added the missing closing quote after "Bug Hunt!".
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: Changed "nmae" to "name" so the user's name is displayed correctly.
print("Nice to meet you, " + name)

age = input("How old are you? ")

# BUG: Converted age from a string to an integer before adding 1.
print("Next year you will be " + str(int(age) + 1))
