import csv
import os

# Path to your CSV file
csv_file_path = 'Cleaned_ProblemSolutionPythonV3.csv'

# Output directory in the same directory as the script
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, 'code_solutions')
os.makedirs(output_dir, exist_ok=True)

# Read CSV and write code to files
with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        code = row['Python Code']  # Assuming the code is in a column named 'ChatGPT_Solution'  
        file_name = f"solution_{i + 1}.py"
        with open(os.path.join(output_dir, file_name), 'w') as code_file:
            code_file.write(code)

print("Code files created successfully!")