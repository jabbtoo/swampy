import math

def factorial(k):
    if k == 0:
        return 1

    else:
        recurse = factorial(k-1)
        result = k * recurse
        return result

factor = 2 * math.sqrt(2) / 9801    
total = 0
for n in range(2):
    quotient = factorial(4*n) * (1103 + 26390*n)
    divisor = factorial(n)**4 * 396**(4*n)
    temp = factor * quotient / divisor
    total += temp
    print ' ', ' ', 1/total
