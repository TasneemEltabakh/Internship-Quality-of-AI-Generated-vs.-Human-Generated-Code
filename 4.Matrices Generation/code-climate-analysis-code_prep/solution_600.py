from re import sub
def snake_case(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
 
print(snake_case('JavaScript'))
print(snake_case('GDScript'))
print(snake_case('BTW...what *do* you call that naming style? snake_case? '))
