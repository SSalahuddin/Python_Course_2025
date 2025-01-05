import json

# Writing to a JSON file
records = [{
           'Name': 'Ahmad',
           'Age': 25,
           'City': 'Peshawar'
           },
           {
           'Name': 'Ali',
           'Age': 22,
           'City': 'Kabul'
           }
           ]

with open('data.json', 'w') as file:
    json.dump(records, file)

# Reading from a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
