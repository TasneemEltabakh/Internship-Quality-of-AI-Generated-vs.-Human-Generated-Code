import numpy as np
np.random.seed(42) 
student = np.array([['stident_id', 'Class', 'Name'],
              ['01', 'V', 'Debby Pramod'],
              ['02', 'V', 'Artemiy Ellie'],
              ['03', 'V', 'Baptist Kamal'],
              ['04', 'V', 'Lavanya Davide'],
              ['05', 'V', 'Fulton Antwan'],
              ['06', 'V', 'Euanthe Sandeep'],
              ['07', 'V', 'Endzela Sanda'],
              ['08', 'V', 'Victoire Waman'],
              ['09', 'V', 'Briar Nur'],
              ['10', 'V', 'Rose Lykos']]) 
print("Original array:")
print(student)
np.random.shuffle(student[2:8])
print("Shuffle the said array rows starting from 3rd to 9th")
print(student)
