import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df[df["Mine_Name"].map(lambda x: x.startswith('P'))].head()
