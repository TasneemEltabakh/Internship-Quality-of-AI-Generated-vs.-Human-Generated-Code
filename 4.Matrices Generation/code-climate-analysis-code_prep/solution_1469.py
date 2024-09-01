import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
result = df.pivot_table( 'survived' , [ 'sex' , 'alone' ] , 'class' )
print(result)
