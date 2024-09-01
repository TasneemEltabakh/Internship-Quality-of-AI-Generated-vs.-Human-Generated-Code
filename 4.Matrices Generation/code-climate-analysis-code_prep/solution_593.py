import numpy as np 
student = """01	V	Debby Pramod
02	V	Artemiy Ellie
03	V	Baptist Kamal
04	V	Lavanya Davide
05	V	Fulton Antwan
06	V	Euanthe Sandeep
07	V	Endzela Sanda
08	V	Victoire Waman
09	V	Briar Nur
10	V	Rose Lykos"""

print("Original text:") 
print(student)
text_lines = student.splitlines()
text_lines = [r.split('\t') for r in text_lines]
result = np.array(text_lines, dtype=np.str)
print("\nArray from the said text:")
print(result)
