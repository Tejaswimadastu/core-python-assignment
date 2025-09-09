# Function to calculate percentage of positive feedback
def positive_feedback_percentage(ratings):
    # If no ratings are given
    if not ratings:
        return "No ratings available"
    # Count ratings that are 4 or 5 (considered positive)
    positive = sum(1 for r in ratings if r >= 4)
    # Calculate percentage of positive ratings
    percentage = (positive / len(ratings)) * 100
    return f"Positive Feedback: {round(percentage, 2)}%"
ratings = list(map(int, input("Enter ratings (1-5) separated by space: ").split()))
print(positive_feedback_percentage(ratings))
