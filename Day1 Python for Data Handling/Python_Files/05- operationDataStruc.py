# List operations
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)
cube = [x**3 for x in numbers]
print(cube)

# Dictionary operations
person = {'name': 'Ahmad', 'age': 25, 'city': 'Peshawar'}
for key, value in person.items():
    print(f'{key}: {value}')
for value in person.values():
  print(value)

# Set operations
set1 = {1, 3, 2}
set2 = {3, 4, 5}
print(set1.intersection(set2))  # Common elements
print(set2.intersection(set1))  # Common elements
print(set1.union(set2))  # All elements
