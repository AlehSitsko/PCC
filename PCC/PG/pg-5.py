# Simple quiz program
score = 0
# Questions and answers model
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Saturn"],
        "answer": "Jupiter"
    }
]
# Loop through each question
for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    # Get user answer
    user_answer = input("Your answer (type the option number): ")
    # Validate and check answer
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(q["options"]):
        if q["options"][int(user_answer) - 1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}")
    else:
        print("Invalid input. Please enter a number corresponding to the options.")
    print()  # Print a newline for better readability
# Display final score
print(f"Your final score is: {score}/{len(questions)}")
# --- IGNORE ---
