import pandas as pd
df = pd.DataFrame( {'X' : [10, 10, 10, 20, 30, 30, 10], 
                    'Y' : [10, 15, 11, 20, 21, 12, 14], 
                    'Z' : [22, 20, 18, 20, 13, 10, 0]})
print("Original DataFrame:")
print(df)
result= df.groupby('X').aggregate(lambda tdf: tdf.unique().tolist())
print(result)
