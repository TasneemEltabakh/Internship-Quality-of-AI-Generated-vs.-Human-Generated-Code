# import required module
import pandas as pd;
import re;

# Read excel file and store in to DataFrame
data = pd.read_excel("date_sample_data.xlsx");

print("Original DataFrame")
data