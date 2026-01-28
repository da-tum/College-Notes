import csv
from gradebook import calculate_average, calculate_median, find_max_score, find_min_score, assign_grades, grade_distribution, pass_fail_filter

def main():
    # Load data from sample_students.csv
    marks_dict = {}
    csv_file = 'sample_students.csv'
    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)  # Skip header
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
        print("File not found.")
        return

    if not marks_dict:
        print("No valid data loaded.")
        return

    # Perform analysis
    avg = calculate_average(marks_dict)
    med = calculate_median(marks_dict)
    max_score = find_max_score(marks_dict)
    min_score = find_min_score(marks_dict)
    grades_dict = assign_grades(marks_dict)
    dist = grade_distribution(grades_dict)
    passed, failed = pass_fail_filter(marks_dict)

    # Print results
    print("Statistical Analysis:")
    print("Metric\t\tValue")
    print("-" * 20)
    print(f"Average\t\t{avg:.2f}")
    print(f"Median\t\t{med}")
    print(f"Max Score\t{max_score}")
    print(f"Min Score\t{min_score}")

    print("\nGrade Distribution:")
    print("Grade\tCount")
    print("-" * 10)
    for grade, count in dist.items():
        print(f"{grade}\t{count}")

    print(f"\nPassed Students ({len(passed)}): {', '.join(passed)}")
    print(f"Failed Students ({len(failed)}): {', '.join(failed)}")

    print("\nName\t\tMarks\t\tGrade")
    print("-" * 35)
    for name, marks in marks_dict.items():
        print(f"{name}\t\t{marks}\t\t{grades_dict[name]}")

if __name__ == "__main__":
    main()
