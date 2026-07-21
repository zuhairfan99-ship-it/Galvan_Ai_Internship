# Automated Quiz Generator
import random
import time
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Platinum"],
        "answer": "Diamond"
    }
]
def main():
    print("--- Automated Quiz Generator ---")
    while True:
        try:
            num_questions = int(
                input(f"Enter number of questions (1-{len(QUESTIONS)}): ")
            )
            if 1 <= num_questions <= len(QUESTIONS):
                break
            print(f"Please enter a number between 1 and {len(QUESTIONS)}.")
        except ValueError:
            print("Please enter a valid number.")
    selected_questions = random.sample(QUESTIONS, num_questions)
    score = 0
    start_time = time.time()
    for idx, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        options = q["options"].copy()
        random.shuffle(options)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                user_choice = int(input("Your answer (number): "))
                if 1 <= user_choice <= len(options):
                    selected_answer = options[user_choice - 1]
                    break
                print("Invalid choice number.")
            except ValueError:
                print("Please enter a valid number.")
        if selected_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
    completed_time = time.time() - start_time
    percentage = round((score / len(selected_questions)) * 100, 2)
    print("\n--- Quiz Summary ---")
    print(f"Total Questions: {len(selected_questions)}")
    print(f"Correct Answers: {score}")
    print(f"Score: {percentage}%")
    print(f"Time Taken: {round(completed_time, 2)} seconds")
if __name__ == "__main__":
    main()