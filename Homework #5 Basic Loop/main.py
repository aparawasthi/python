import math

def checkForPrime(number):
    if number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        checktill = int(math.sqrt(number))
        for n in range(2,checktill+1):
            if n>2 and n%2 == 0:
                continue
            elif number%n == 0:
                return False
    return True

for n in range(1,101):
    if checkForPrime(n):
        print("Prime")
    elif n%5 == 0 and n% 3 == 0:
        print("FizzBuzz")
    elif n%5 == 0:
        print("Buzz")
    elif n%3 == 0:
        print("Fizz")
    else:
        print(n)