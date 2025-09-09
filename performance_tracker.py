# Function to calculate average marks of each student
def calculate_avg(students):
    avgs = {}  
    for name, marks in students.items():
        avgs[name] = round(sum(marks) / len(marks), 2)
    return avgs
# Function to find the student with the highest average
def find_top_performer(avgs):
    return max(avgs, key=avgs.get)  
# Dictionary to store student names and their marks
students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("\nEnter student name: ")
    marks = list(map(int, input(f"Enter marks for {name} (space-separated): ").split()))
    students[name] = marks  
# Calculate average marks of all students
avgs = calculate_avg(students)
# Find top-performing student
top_student = find_top_performer(avgs)
# Display results
print("\nAverage Marks:", avgs)
print("Top Performer:", top_student)
