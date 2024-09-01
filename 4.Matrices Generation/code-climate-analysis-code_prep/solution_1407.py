import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'ufo.csv')
df['Date_time'] = df['Date_time'].astype('datetime64[ns]')
df["ufo_yr"] = df.Date_time.dt.year
years_data = df.ufo_yr.value_counts()
years_index = years_data.index  # x ticks
years_values = years_data.get_values()
plt.figure(figsize=(15,8))
plt.xticks(rotation = 60)
plt.title('UFO Sightings by Year')
plt.xlabel("Year")
plt.ylabel("Number of reports")
years_plot = sns.barplot(x=years_index[:60],y=years_values[:60], palette = "Reds")
