import numpy as np 

str1 = np.array([['Python','NumPy','Exercises'],
                 ['Python','Pandas','Exercises'],
                 ['Python','Machine learning','Python']])
print("Original array of string values:") 
print(str1)
print("\nCount 'Python' row wise in the above array of string values:")
print(np.char.count(str1, 'Python'))
