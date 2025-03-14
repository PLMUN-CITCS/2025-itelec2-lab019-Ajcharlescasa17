def get_student_score() -> float:
    """
    Prompts the user to enter a valid numerical score.
    Returns:
        float: The student's score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))  # Get user input
            if 0 <= score <= 100:  # Validate input range
                return score
            else:
                print("Error: Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.
    Args:
        score (float): The student's numerical score.
    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Main Program Flow
student_score = get_student_score()  # Get user input
student_grade = calculate_grade(student_score)  # Calculate grade

# Display the result
print(f"Your Grade is: {student_grade}")