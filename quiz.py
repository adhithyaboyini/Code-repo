def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for key in questions:
        print(questions.get(key), end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print(f"Your score is: {score}%")

def play_again():
    response = input("Do you want to play again? (yes or no): ")
    return response.lower() == "yes"

questions = {
    "What is the capital of France?": "A",
    "What is 2 + 2?": "B",
    "What is the capital of Japan?": "C",
    "What is the largest planet in our solar system?": "D"
}
options = [
    ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
    ["A. 3", "B. 4", "C. 5",    "D. 6"],
    ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
    ["A. Earth", "B. Mars", "C. Saturn", "D. Jupiter"]
]

new_game()
while play_again():
    new_game()

print("Thanks for playing!")