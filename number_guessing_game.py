import random

score = 0   

while True:
    print("\nNUMBER GUESSING GAME")
    print("1. EASY (1-50)")
    print("2. HARD (1-100)")

    choice = input("Choose level: ")

    if choice == '1':
        number = random.randint(1, 50)
        max_attempt = 7
    elif choice == '2':
        number = random.randint(1, 100)
        max_attempt = 5
    else:
        print("Invalid choice, defaulting to EASY mode")
        number = random.randint(1, 50)
        max_attempt = 7

    attempts = 0
    guess = None

    while attempts < max_attempt:
        try:
            guess = int(input("Enter your guess: "))
        except:
            print("Please enter a valid number!")
            continue

        attempts += 1
        print(f"Attempts left: {max_attempt - attempts}")

        if guess == number:
            print(f"Correct! You guessed it in {attempts} attempts")
            score += 1  
            break
        elif abs(guess - number) <= 5:
            print("Very Close!")
        elif guess > number:
            print("Too HIGH!")
        else:
            print("Too LOW!")

    if guess != number:
        print(f"GAME OVER! The number was {number}")

    print(f"Your Score: {score}")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() not in ['y', 'yes']:
        print(f"Final Score: {score}")
        print("Thanks for playing!")
        break