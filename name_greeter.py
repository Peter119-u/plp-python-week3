name = input("What is your full name? ")

parts = name.split()

if len(parts) >= 2:
    print("Hello, " + parts[0] + "!")
else:
    print("Please enter your full name.")
