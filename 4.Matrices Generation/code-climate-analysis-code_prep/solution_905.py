import numpy as np
arra1 = np.array([("Yasemin Rayner", 88.5, 90),
                 ("Ayaana Mcnamara", 87, 99),
             ("Jody Preece", 85.5, 91)])
print("Original arrays:")
print(arra1)
print("\nRecord array;")
result = np.core.records.fromarrays(arra1.T,
                              names='col1, col2, col3',
                              formats = 'S80, f8, i8')
print(result)
