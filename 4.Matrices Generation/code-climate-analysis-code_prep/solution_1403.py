import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')
print("Sum: ",df["Production"].sum()) 
print("Mean: ",df["Production"].mean())
print("Maximum: ",df["Production"].max())
print("Minimum: ",df["Production"].min()) 
