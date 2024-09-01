def test(lst,str1):
    result = [el for el in lst if(el in str1)] 
    return bool(result)


str1 = "https://www.w3resource.com/python-exercises/list/"
lst = ['.com', '.edu', '.tv']   
print("The original string and list: ") 
print(str1)
print(lst)
print("\nCheck if",str1,"contains an element, which is present in the list",lst)
print(test(lst,str1))
str1 = "https://www.w3resource.net"
lst = ['.com', '.edu', '.tv']   
print("\nThe original string and list: " + str1) 
print(str1)
print(lst)
print("\nCheck if",str1,"contains an element, which is present in the list",lst)
print(test(lst,str1))
