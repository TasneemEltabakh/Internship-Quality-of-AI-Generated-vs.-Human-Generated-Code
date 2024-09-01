def decapitalize_first_letter(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])]) 
print(decapitalize_first_letter('Java Script'))
print(decapitalize_first_letter('Python'))
