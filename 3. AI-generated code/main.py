import pandas as pd
import time
from openai import OpenAI
import os
import re

# Initialize the OpenAI client
# $env:OPENAI_API_KEY="your-actual-api-key-here"
# python main.py
client = OpenAI()

def extract_code_block(text):
    # Use regex to find content between triple backticks
    code_block_match = re.search(r'```python\n(.*?)```', text, re.DOTALL)
    if code_block_match:
        return code_block_match.group(1).strip()
    return text  # Return original text if no code block found

def get_chatgpt_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates Python code solutions."},
                {"role": "user", "content": prompt}
            ]
        )
        return extract_code_block(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def process_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Add a new column for the ChatGPT solutions
    df['ChatGPT_Solution'] = ''
    
    # Process each row
    for index, row in df.iterrows():
        problem = row['Problem']
        prompt = f"Generate a Python code solution for the following problem:\n{problem}"
        
        # Get response from ChatGPT
        solution = get_chatgpt_response(prompt)
        
        if solution:
            df.at[index, 'ChatGPT_Solution'] = solution
        
        # Add a delay to avoid hitting rate limits[adjust as you want ]
        time.sleep(1)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    input_file = 'Cleaned_ProblemSolutionPythonV3.csv.csv'  # Your input CSV file
    output_file = 'output_with_solutions_GPT4.csv'  # The output file name
    
    process_csv(input_file, output_file)