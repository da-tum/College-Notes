import csv


#writing to csv file

with open("data.csv", "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])


#reading from csv file
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        


