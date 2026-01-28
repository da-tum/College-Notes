# ------------Task 1 ----------

#Name  : Harsh Dev Jha  ,
#Date  - 24/11/25 ,
#Title : gradebook-analyzer - Is a gradebook analyzer app

import csv

# ------------Task 3 ----------

def calculate_average(marks_dict):
    '''Used to Calculate Average of the Given data by the user'''
    if not marks_dict:
        return 0
    add = 0
    for i in marks_dict.values():
        add += i
    mean = add / len(list(marks_dict.values()))
    return mean

def calculate_median(marks_dict):
    '''Used to Calculate Median of the Given data by the user'''
    if not marks_dict:
        return 0
    l = list(marks_dict.values())
    #sorting the list to check median in an correct order
    #Bubble Sorting
    for i in range(len(l)):
        swap = False
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swap = True
        if not swap:
            break
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        return ((l[(len(l)//2)-1] + l[(len(l)//2)])/2)

def find_max_score(marks_dict):
    '''Used to Calculate Maximum of the Given data by the user'''
    if not marks_dict:
        return "N/A"
    l = list(marks_dict.values())
    maximum = l[0]  # Start with the first value
    for i in l:
        if i > maximum:
            maximum = i
    return maximum

def find_min_score(marks_dict):
    '''Used to Calculate Minimum of the Given data by the user'''
    if not marks_dict:
        return "N/A"
    l = list(marks_dict.values())
    minimum = l[0]  # Start with the first value
    for i in l:
        if i < minimum:
            minimum = i
    return minimum

def assign_grades(marks_dict):
    '''Assign letter grades based on marks'''
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def grade_distribution(grades_dict):
    '''Count students per grade'''
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
        distribution[grade] += 1
    return distribution

def pass_fail_filter(marks_dict):
    '''Filter passed and failed students'''
    passed_students = [name for name, mark in marks_dict.items() if mark >= 40]
    failed_students = [name for name, mark in marks_dict.items() if mark < 40]
    return passed_students, failed_students

def print_table(marks_dict, grades_dict):
    '''Print formatted table'''
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name, mark in marks_dict.items():
        grade = grades_dict[name]
        print(f"{name}\t\t{mark}\t{grade}")

def choice():
    # ------------Task 2 ----------
    choices = str(input("""
    Please choose an option:
    1 for Manual entry (multiple students)
    2 for CSV file import
    3 for Exit\n"""))

    #Error Handling
    if choices not in ['1','2','3']:
        print('Incorrect Input Choose Again')
        return choice()
    else:
        return choices

if __name__ == "__main__":
    print('''Welcome to the Gradebook Analyzer
in this mini project you will be able to
automate the entire process via a Python-based GradeBook Analyzer CLI,
of computing statistics on student marks.
The system will read marks from input or a CSV file, perform key statistical analysis,
assign grades, and generate summaries in a user friendly format.''')

    while True:
        choices = choice()
        marks_dict = {}
        if choices == '1':
            print("You have chosen the Manual entry option.")
            while True:
                try:
                    n = int(input("Enter the number of students: "))
                    if n >= 1:
                        break
                    else:
                        print("Number of students must be at least 1.")
                except ValueError:
                    print("Error: Must be an integer.")
                    continue
            for i in range(n):
                while True:
                    name = input(f"Enter name for student number {i+1}: ")
                    if name.strip() == "":
                        print("Name cannot be empty.")
                        continue
                    try:
                        marks = int(input(f"Enter marks for {name}: "))
                        if 0 <= marks <= 100:
                            marks_dict[name] = marks
                            break
                        else:
                            print("Error: Marks must be between 0 and 100.")
                    except ValueError:
                        print('Error: Marks must be an integer.')
        elif choices == '2':
            print("You have chosen the CSV import option.")
            csv_file = input("Enter the CSV file path (e.g., students.csv): ")
            try:
                with open(csv_file, mode='r') as file:
                    csv_reader = csv.reader(file)
                    next(csv_reader, None)  # Skip header if present
                    for row in csv_reader:
                        if len(row) >= 2:
                            name = row[0].strip()
                            try:
                                marks = int(row[1])
                                if 0 <= marks <= 100:
                                    marks_dict[name] = marks
                                else:
                                    print(f"Skipping {name}: Marks out of range.")
                            except ValueError:
                                print(f"Skipping {name}: Invalid marks.")
            except FileNotFoundError:
                print("File not found. Please check the path.")
                continue
            if not marks_dict:
                print("No valid data loaded from CSV.")
                continue
        else:
            print('''Thank You For Using this Service''')
            break

        if marks_dict:
            # Task 3: Statistical Analysis
            avg = calculate_average(marks_dict)
            med = calculate_median(marks_dict)
            max_score = find_max_score(marks_dict)
            min_score = find_min_score(marks_dict)
            print("\nStatistical Analysis:")
            print("Metric\t\tValue")
            print("-" * 20)
            print(f"Average\t\t{avg:.2f}")
            print(f"Median\t\t{med}")
            print(f"Max Score\t{max_score}")
            print(f"Min Score\t{min_score}")

            # Task 4: Grade Assignment and Distribution
            grades_dict = assign_grades(marks_dict)
            dist = grade_distribution(grades_dict)
            print("\nGrade Distribution:")
            print("Grade\tCount")
            print("-" * 10)
            for grade, count in dist.items():
                print(f"{grade}\t{count}")

            # Task 5: Pass/Fail Filter
            passed, failed = pass_fail_filter(marks_dict)
            print(f"\nPassed Students ({len(passed)}): {', '.join(passed)}")
            print(f"Failed Students ({len(failed)}): {', '.join(failed)}")

            # Task 6: Results Table
        # <----- TASK 6: Results Table and Loop ----->
        print("\nName\t\tMarks\t\tGrade")
        print("-" * 35)
        for name, marks in marks_dict.items():
            print(f"{name}\t\t{marks}\t\t{grades_dict[name]}")
        
        print("\n" + "="*35 + "\n") # Separator before next loop
        # After analysis, ask to repeat or exit
        repeat = input("\nDo you want to perform another analysis? (y/n): ").lower()
        if repeat != 'y':
            print('''Thank You For Using this Service''')
            break
