def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available"
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return f"Positive Feedback: {round(percentage, 2)}%"
ratings = list(map(int, input("Enter ratings (1-5) separated by space: ").split()))
print(positive_feedback_percentage(ratings))
