# import required modules
import pandas as pd
import numpy as np
import time

# time taken to read data
s_time = time.time()
df = pd.read_csv("gender_voice_dataset.csv")
e_time = time.time()

print("Read without chunks: ", (e_time-s_time), "seconds")

# data
df.sample(10)