def positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    positive_ratings = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_ratings / len(ratings)) * 100
    return round(percentage, 2)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
feedback_percentage = positive_feedback_percentage(ratings)
print(f"Positive Feedback: {feedback_percentage}%")
