#Source:https://bit.ly/30PS62m
import itertools as it
 
def fizz_buzz(n):
    fizzes = it.cycle([""] * 2 + ["Fizz"])
    buzzes = it.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, it.count(1)))
    for i in it.islice(result, 100):
        print(i)

n = 50
fizz_buzz(n)
