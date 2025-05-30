# create_exercise.py

import os

def create_exercise_folder(ex_name):
    # Define the base directory (Pandas DataFrame folder)
    base_dir = "Pandas DataFrame"

    # Create full path for the new exercise
    folder_path = os.path.join(base_dir, ex_name)

    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"✅ Created base directory: {base_dir}")

    # Create the exercise folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"✅ Created folder: {folder_path}")
    else:
        print(f"⚠️ Folder '{folder_path}' already exists!")

    # File path for the Python file
    file_path = os.path.join(folder_path, f"{ex_name}.py")

    # Template code
    template = '''import numpy as np
import pandas as pd

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame

'''

    # Write template to file
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(template)
        print(f"✅ Created file with template: {file_path}")
    else:
        print(f"⚠️ File '{file_path}' already exists!")

if __name__ == "__main__":
    ex_name = input("Enter exercise name (e.g., Ex12): ").strip()
    create_exercise_folder(ex_name)