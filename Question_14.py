# Question 14:
# Write a program to calculate the percentage of correct answers.

# Taking inputs from user
total_questions = int(input("Enter total number of questions: "))
correct_answers = int(input("Enter number of correct answers: "))

# Validating inputs
if total_questions <= 0:
    print("Total questions must be greater than 0 ❌")
elif correct_answers > total_questions:
    print("Correct answers cannot be greater than total questions ❌")
else:
    # Calculating percentage
    percentage = (correct_answers / total_questions) * 100

    # Printing results
    print(f"\nYou got {correct_answers} out of {total_questions} correct.")
    print(f"Your percentage score is: {percentage:.2f}%")

    # Extra grading logic
    if percentage >= 90:
        print("Excellent performance 🏆")
    elif percentage >= 75:
        print("Good job 👍")
    elif percentage >= 50:
        print("Needs improvement ⚠️")
    else:
        print("Poor performance ❌")
