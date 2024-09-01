import pandas as pd
import numpy as np
df = pd.read_excel('E:\coalpublic2013.xlsx')    
df.query('Mine_Name == ["Shoal Creek Mine", "Piney Woods Preparation Plant"]').head()
