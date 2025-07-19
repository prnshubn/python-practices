questions=("1) What is the largest planet in our solar system?",
           "2) What is the hottest planet in our solar system?",
           "3) Who is the current Prime Minister of India?",
           "4) What is the only even prime number?",
           "5) What is the capital of Germany?")

answers=("A) Earth  B) Jupiter  C) Mars  D) Saturn",
         "A) Venus  B) Jupiter  C) Mars  D) Mercury",
         "A) Narendra Modi  B) Rahul Gandhi  C) Amit Shah  D) Mamata Banerjee",
         "A) 8  B) 3  C) 2  D) 5",
         "A) Munich  B) Hamburg  C) Frankfurt  D) Berlin")

your_guesses=[]
correct_answers=("B","A","A","C","D")
index=0
score=0

print("Let's play a game of quiz. Each correct answer will give you 10 points and no points for incorrect answer.")

while index < len(questions):
    print("--------------------------------------------------------")
    print(questions[index])
    print(answers[index])
    guess=input("Enter your answer: ")
    while guess.upper() not in ["A", "B", "C", "D"]:
        print("Wrong input. You can only enter A, B, C, or D.")
        guess = input("Enter your answer: ")
    if guess.upper()==correct_answers[index]:
        print("CORRECT!")
        your_guesses.append(guess.upper())
        score+=10
    else:
        print("INCORRECT!")
        your_guesses.append(guess.upper())
    index+=1

print("---------------------")
print("-----Your result-----")
print(f"Correct options are: {correct_answers}")
print(f"Your guesses are: {your_guesses}")
print(f"Your score is: {score}")
