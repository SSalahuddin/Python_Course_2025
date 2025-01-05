import os
import shutil

# Creating a new directory
os.makedirs('Python_course', exist_ok=True)

# Moving a file
shutil.move('data.csv', 'Python_course/data.csv')

# Deleting a directory
# shutil.rmtree('Python_course')
