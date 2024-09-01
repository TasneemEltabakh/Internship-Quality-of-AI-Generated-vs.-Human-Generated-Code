def test(dictt):
    result = list(map(list, dictt.items()))
    return result    

color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
print("\nOriginal Dictionary:")
print(color_dict)
print("Convert the said dictionary into a list of lists:")
print(test(color_dict))

color_dict = {'1' : 'Austin Little', '2' : 'Natasha Howard', '3' : 'Alfred Mullins', '4' : 'Jamie Rowe'}
print("\nOriginal Dictionary:")
print(color_dict)
print("Convert the said dictionary into a list of lists:")
print(test(color_dict))
