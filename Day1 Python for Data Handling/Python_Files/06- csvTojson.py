import csv
import json

# Step 1: Write CSV file
with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Ahmad', 20, 'A'])
    writer.writerow(['Faheem', 22, 'B'])
    writer.writerow(['Shahid', 21, 'A'])

# Step 2: Read from CSV
students = []
with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# Step 3: Write to JSON
with open('students.json', mode='w') as file:
    json.dump(students, file, indent=4)

print("CSV data has been successfully converted to JSON!")
