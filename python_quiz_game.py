import random
import os

# Function to load questions
def load_questions():
    questions = []

    with open("questions.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")

            question_text = parts[0]
            options = parts[1].split(",")
            answer = parts[2]

            question_dict = {
                "question": question_text,
                "options": options,
                "answer": answer
            }

            questions.append(question_dict)

    return questions


# Function to save score
def save_score(name, score, total, percentage):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name} - {score}/{total} - {percentage}%\n")


# Function to show leaderboard
def show_leaderboard():
    print("\n🏆 Leaderboard")

    try:
        with open("leaderboard.txt", "r") as file:
            data = file.read()

            if data.strip() == "":
                print("No scores yet.")
            else:
                print(data)

    except FileNotFoundError:
        print("No leaderboard yet.")


# Function to clear leaderboard
def clear_leaderboard():
    confirm = input("Are you sure you want to clear leaderboard? (y/n): ")

    if confirm.lower() == "y":
        open("leaderboard.txt", "w").close()
        print("🧹 Leaderboard cleared!")
    else:
        print("Cancelled.")


# Load questions once
all_questions = load_questions()

# Main Menu Loop
while True:

    print("\n🎯 Python Quiz Game")
    print("-------------------")
    print("1. Play Quiz")
    print("2. View Leaderboard")
    print("3. Clear Leaderboard")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # PLAY QUIZ
    if choice == "1":

        score = 0

        # Pick 5 random questions
        questions = random.sample(all_questions, 5)

        for i, q in enumerate(questions, start=1):

            print(f"\nQuestion {i}:")
            print(q["question"])

            for option in q["options"]:
                print(option)

            user_answer = input("Enter answer (a/b/c/d): ").lower()

            if user_answer == q["answer"]:
                print("✅ Correct!")
                score += 1

            else:
                print("❌ Wrong!")

                for option in q["options"]:
                    if option.startswith(q["answer"]):
                        print("Correct answer was:", option)

        # Score display
        print("\nFinal Score:", score, "/", len(questions))

        percentage = (score / len(questions)) * 100
        percentage = round(percentage, 2)

        print("Percentage:", percentage, "%")

        # Save score
        name = input("\nEnter your name: ")
        save_score(name, score, len(questions), percentage)

        print("✅ Score saved!")

    # VIEW LEADERBOARD
    elif choice == "2":
        show_leaderboard()

    # CLEAR LEADERBOARD
    elif choice == "3":
        clear_leaderboard()

    # EXIT
    elif choice == "4":
        print("👋 Exiting game. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")