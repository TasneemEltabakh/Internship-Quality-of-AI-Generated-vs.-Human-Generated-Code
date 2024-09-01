import pandas as pd
print("Create an Interval Index using IntervalIndex.from_breaks:")
df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},
                            index = pd.IntervalIndex.from_breaks(
                            [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5]))    
print(df_interval)
print(df_interval.index)

print("\nCreate an Interval Index using IntervalIndex.from_tuples:")
df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},             
                            index = pd.IntervalIndex.from_tuples(
                            [(0, .5), (.5, 1), (1, 1.5), (1.5, 2), (2, 2.5), (2.5, 3), (3, 3.5)]))
print(df_interval)
print(df_interval.index)

print("\nCreate an Interval Index using IntervalIndex.from_arrays:")
df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},             
                            index = pd.IntervalIndex.from_arrays(
                            [0, .5, 1, 1.5, 2, 2.5, 3], [.5, 1, 1.5, 2, 2.5, 3, 3.5]))
print(df_interval)
print(df_interval.index) 
