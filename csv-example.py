import csv

with open("students.csv", "w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Score"])

    writer.writerow(["Ali", 20, 18])

    writer.writerow(["Sara", 21, 19])



with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)