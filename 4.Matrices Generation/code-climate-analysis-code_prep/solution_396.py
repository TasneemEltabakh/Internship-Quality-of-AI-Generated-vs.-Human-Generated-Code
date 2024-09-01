import pandas as pd
mtp = pd.Period('2021-11','M')
print("Monthly time perid: ",mtp)
print("\nList of names in the current local scope:")
print(dir(mtp)) 
