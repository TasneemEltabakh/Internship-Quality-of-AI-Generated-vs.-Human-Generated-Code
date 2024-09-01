import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'ufo.csv')
df['duration_sec'] = (df['length_of_encounter_seconds'].astype(float))/60
s = df["duration_sec"].quantile(0.95)
temp = df['duration_sec']
temp = temp.sort_values()
temp = temp[temp < s]
plt.figure(figsize=(10, 8))
sns.distplot(temp)
plt.xlabel('Duration(min)', fontsize=20)
plt.ylabel("Frequency", fontsize=15)
plt.xticks(fontsize=12)
plt.title("-Distribution of UFO obervation time-", fontsize=20)
plt.show()
