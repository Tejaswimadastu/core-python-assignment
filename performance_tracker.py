def calculate_avg(students):
    avgs= {}
    for name, marks in students.items():
        avgs[name] = round(sum(marks) / len(marks), 2)
    return avgs
def find_top_performer(avgs):
    return max(avgs, key=avgs.get)
students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("\nEnter student name: ")
    marks = list(map(int, input(f"Enter marks for {name} (space-separated): ").split()))
    students[name] = marks
avgs = calculate_avg(students)
top_student = find_top_performer(avgs)
print("\nAverage Marks:", avgs)
print("Top Performer:", top_student)
