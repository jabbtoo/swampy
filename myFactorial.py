

def factorial(n):
    space = ' ' * (4 * n)
    name = 'factorial'
    print(space + name, n)

    if n == 0:
        print(space, 'returning 1')
        return 1

    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, "returning", result)
        return result

factorial(5)
