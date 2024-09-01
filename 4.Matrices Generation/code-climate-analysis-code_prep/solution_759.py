from collections import Counter
def test(dictt):    
    result = Counter(dictt.values())
    return result    

dictt = {
 'V': 10,
 'VI': 10,
 'VII': 40,
 'VIII': 20,
 'IX': 70,
 'X': 80,
 'XI': 40,
 'XII': 20, 
 }

print("\nOriginal Dictionary:")
print(dictt)
print("\nCount the frequency of the said dictionary:")
print(test(dictt))
