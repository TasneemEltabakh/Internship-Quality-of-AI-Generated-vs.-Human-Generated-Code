import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df[df["Labor_Hours"] > 20000].head()
