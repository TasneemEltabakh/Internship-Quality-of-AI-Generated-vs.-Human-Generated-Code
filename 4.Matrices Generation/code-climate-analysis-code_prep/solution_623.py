def test(n1, n2):
    n1, n2 = '0' + n1, '0' + n2
    if (n1.isnumeric() and n2.isnumeric()):
        return str(int(n1) + int(n2))
    else:
        return 'Error in input!'
print(test("10", "32"))
print(test("10", "22.6"))
print(test("100", "-200")) 
