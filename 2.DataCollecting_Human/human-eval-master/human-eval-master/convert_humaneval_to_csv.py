import json
import csv
import gzip

# Path to the compressed HumanEval dataset
input_file_path = 'data/HumanEval.jsonl.gz'
output_file_path = 'data/HumanEval.csv'

# Load the HumanEval dataset from the compressed file
with gzip.open(input_file_path, 'rt', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

# Prepare the CSV file
with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['task_id', 'prompt', 'canonical_solution', 'test']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for item in data:
        writer.writerow({
            'task_id': item.get('task_id', ''),
            'prompt': item.get('prompt', ''),
            'canonical_solution': item.get('canonical_solution', ''),
            'test': item.get('test', ''),
        })

print("CSV file created successfully.")
