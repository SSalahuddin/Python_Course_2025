import csv

# Writing to a CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Ahmad', 25, 'Peshawar'])
    writer.writerow(['Behlol', 22, 'Kabul'])

# Reading from a CSV file
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
