from numpy import genfromtxt
csv_data = genfromtxt('fdata.csv', dtype=['S10','float32','float32','float32','float32'], delimiter=",")
print(csv_data)
