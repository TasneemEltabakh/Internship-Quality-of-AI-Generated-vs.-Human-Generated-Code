import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df[df["MSHA ID"].isin([102976,103380])].head()
