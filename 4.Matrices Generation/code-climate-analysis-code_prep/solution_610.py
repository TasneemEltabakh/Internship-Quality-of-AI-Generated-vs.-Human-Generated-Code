import pandas as pd
data = {\
"year": [2002, 2003, 2015, 2018],
"day_of_the_year": [250, 365, 1, 140]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df["combined"] = df["year"]*1000 + df["day_of_the_year"]
df["date"] = pd.to_datetime(df["combined"], format = "%Y%j")
print("\nNew DataFrame:")
print(df)
