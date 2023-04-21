def factorielle(n):
    if int(n) == 0:
        return 1
    else:
        return n * factorielle(int(n)-1)

n = input('Mettez un nombre pour obtenir sa factorielle: ')

print(factorielle(int(n)))