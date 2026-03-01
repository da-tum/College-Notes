# 📊Gradebook Analyzer

## Description
Gradebook Analyzer is a Python-based command-line interface (CLI) tool designed to automate the process of analyzing student marks. It reads student data either through manual input or from a CSV file, performs statistical analysis (average, median, maximum, and minimum scores), assigns letter grades based on marks, provides grade distribution, filters passed and failed students, and displays a formatted results table.

---

## 🧠 Methodology: The CRISP-DM Approach

This project follows the **Cross-Industry Standard Process for Data Mining (CRISP-DM)** framework to ensure accurate and meaningful data processing:

1.  **Business Understanding 🎯**
    * **Goal:** Automate the tedious process of calculating student statistics and assigning grades to save time and reduce human error.
2.  **Data Understanding 📂**
    * **Input:** The system handles raw data in two forms: direct user input (Manual) or structured text files (CSV format: Name, Marks).
3.  **Data Preparation 🧹**
    * **Cleaning:** The script validates inputs, stripping whitespace and ensuring numerical values are valid integers before processing.
4.  **Modeling (Logic Application) ⚙️**
    * **Transformation:** Applies logic gates to map numerical scores to categorical data (Letter Grades A-F) and computes central tendency metrics (Average, Median).
5.  **Evaluation 📉**
    * **Analysis:** Generates frequency distributions for grades and separates students into "Passed" and "Failed" cohorts for quick assessment.
6.  **Deployment 🚀**
    * **Interface:** A user-friendly CLI loop that presents the analyzed data in a tabulated format and allows for continuous usage.

---

## Features
- **⌨️Manual Entry**: Input student names and marks directly via the CLI for multiple students.
- **📂CSV Import**: Load student data from a CSV file (columns: Name, Marks).
- **🧮Statistical Analysis**: Calculate average, median, maximum, and minimum scores.
- **🏷️Smart Grade Assignment**: Assign letter grades (A, B, C, D, F) based on marks:
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - F: Below 60
- **📊Distribution Insights:** Visualizes the count of students per grade tier.
- **🚦Pass/Fail Filter**: List students who passed (marks >= 40) and failed (marks < 40).
- **📑Formatted Results Table**: Display a formatted table of names, marks, and grades.
- **🛡️Robust Error Handling**: Validates inputs and handles file not found or invalid data gracefully.

## Requirements
- Python 3.x
- Built-in `csv` module (no external `pip install` dependencies required)

## 🚀 Usage
1. Run the script: `python gradebook.py`
2. Choose an option:
   - 1: Manual entry (enter number of students, then names and marks).
   - 2: CSV import (provide the path to a CSV file with columns: Name, Marks).
   - 3: Exit.
3. The script will perform analysis and display results.
4. After analysis, choose to perform another analysis or exit.

### CSV File Format
The CSV file should have at least two columns: `Name` and `Marks`. The first row is treated as the header and skipped. Example:

```
Name,Marks
Alice,85
Bob,92
Charlie,78
```

## 💻 Example Output
```
Welcome to the Gradebook Analyzer
in this mini project you will be able to
automate the entire process via a Python-based GradeBook Analyzer CLI,
of computing statistics on student marks.
The system will read marks from input or a CSV file, perform key statistical analysis,
assign grades, and generate summaries in a user friendly format.

    Please choose an option:
    1 for Manual entry (multiple students)
    2 for CSV file import
    3 for Exit
2
You have chosen the CSV import option.
Enter the CSV file path (e.g., students.csv): sample_students.csv

Statistical Analysis:
Metric          Value
--------------------
Average         82.50
Median          85.0
Max Score       95
Min Score       65

Grade Distribution:
Grade   Count
----------
A       2
B       1
C       1
D       1
F       0

Passed Students (4): Alice, Bob, Charlie, David
Failed Students (0): 

Name            Marks           Grade
-----------------------------------
Alice           85              B
Bob             95              A
Charlie         78              C
David           92              A
Eve             65              D

===================================

Do you want to perform another analysis? (y/n): n
Thank You For Using this Service
```

## 📸 Attachments for Sample
![Sample1](Assets/m-1.png)
![Sample2](Assets/m-2.png)
![Sample3](Assets/sample-run.png)
![Sample4](Assets/Exit.png)
![Sample5](Assets/1.png)
![Sample6](Assets/2..png)

## 📥Accessing the Sample Files
[Access Sample CSV](Assets/Sample/sample_students.csv)

<br>

[Access Sample run py file](Assets/Sample/sample_run.py)

