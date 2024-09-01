import pandas as pd


file_path = 'ProblemSolutionPythonV3.csv' 
df = pd.read_csv(file_path)


def clean_non_ascii(text):
    if isinstance(text, str):  
        return ''.join(char for char in text if ord(char) < 128)  
    return text


df['Python Code'] = df['Python Code'].apply(clean_non_ascii)
df['Problem'] = df['Problem'].apply(clean_non_ascii)


cleaned_file_path = 'Cleaned_ProblemSolutionPythonV3.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data has been saved to {cleaned_file_path}")
