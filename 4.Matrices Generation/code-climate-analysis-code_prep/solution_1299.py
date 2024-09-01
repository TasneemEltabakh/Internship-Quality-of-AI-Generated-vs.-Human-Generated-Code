import numpy as np 
print("Generate a uniform random sample with replacement:") 
print(np.random.choice(7, 5))
print("\nGenerate a uniform random sample without replacement:") 
print(np.random.choice(7, 5, replace=False))
print("\nGenerate a non-uniform random sample with replacement:") 
print(np.random.choice(7, 5, p=[0.1, 0.2, 0, 0.2, 0.4, 0, 0.1]))
print("\nGenerate a uniform random sample without replacement:") 
print(np.random.choice(7, 5, replace=False, p=[0.1, 0.2, 0, 0.2, 0.4, 0, 0.1]))  
