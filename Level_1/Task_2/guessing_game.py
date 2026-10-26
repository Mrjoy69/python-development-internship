import random

secret_number=random.randint(1, 100)
guess = None
attempts = 0
max_attempts = 5

print("\n===============================")
print("Number Guessing Game")
print("===============================")

while guess != secret_number and attempts < max_attempts:
    try:
        guess = int(input("\nGuess a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    attempts += 1
    print(f"You have {max_attempts - attempts} attempts left.")

    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        
    elif guess > secret_number:
        print("Too High! Try again")

    elif guess < secret_number:
        print("Too Low! Try again")

    elif guess == secret_number and attempts == 5:
        print("Congratulations! You got it on the fifth attempt.")

    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

    if attempts == max_attempts:
        print(f"You have used all your attempts. The correct number was: {secret_number}\n")
