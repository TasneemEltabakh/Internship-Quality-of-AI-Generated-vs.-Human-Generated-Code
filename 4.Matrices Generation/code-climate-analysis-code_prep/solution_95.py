import pandas as pd
nums = {'amount': ['10', '250', '3000', '40000', '500000']}
print("Original dataframe:")
df = pd.DataFrame(nums)
print(df)
print("\nAdd leading zeros:")
df['amount'] = list(map(lambda x: x.zfill(10), df['amount']))
print(df)
