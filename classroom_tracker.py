def average_marks(marks):
    return sum(marks) / len(marks)
def find_top_performer(average):
    top_student = max(average, key=average.get)
    return top_student
def performance(students):
    average = {}
    for student, marks in students.items():
        average[student] = average_marks(marks)
    top_performer = find_top_performer(average)
    return average, top_performer
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average, top_performer =performance(students)
print("Average Marks:", average)
print("Top Performer:", top_performer)