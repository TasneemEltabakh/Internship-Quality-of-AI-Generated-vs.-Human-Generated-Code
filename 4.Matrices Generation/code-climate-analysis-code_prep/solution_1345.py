import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df[df["MSHA ID"]==102901].head()
