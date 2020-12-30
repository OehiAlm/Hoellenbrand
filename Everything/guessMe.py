
secret_number = 13
guess = int
guess_count = 0
print("You have 3 guesses")

while guess != secret_number and guess_count <= 2:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess < secret_number:
        print("Guess is too small")
    elif guess == secret_number:
        print("YAY")
    else:
        print("Guess is too high")

print("You lose")
