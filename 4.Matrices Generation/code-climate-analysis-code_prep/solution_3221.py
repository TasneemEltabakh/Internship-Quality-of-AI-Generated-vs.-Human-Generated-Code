
basic=float(input("Enter the basic salary of an employee:"))
da = (float)(15 * basic) / 100.0
hr = (float)(10 * basic) / 100.0
da_on_ta = (float)(3 * basic) / 100.0
gross = basic + da + hr + da_on_ta
print("Gross salary of an Employee= ",gross)