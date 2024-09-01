import pandas as pd
import numpy as np
df = pd.DataFrame({'Geek_ID':['Geek1_id', 'Geek2_id', 'Geek3_id',
'Geek4_id', 'Geek5_id'],
'Geek_A': [1, 1, 3, 2, 4],
'Geek_B': [1, 2, 3, 4, 6],
'Geek_R': np.random.randn(5)})

# Geek_A Geek_B Geek_ID Geek_R
# 0 1 1 Geek1_id random number
# 1 1 2 Geek2_id random number
# 2 3 3 Geek3_id random number
# 3 2 4 Geek4_id random number
# 4 4 6 Geek5_id random number

print(df.Geek_ID.str.split('_').str[0])