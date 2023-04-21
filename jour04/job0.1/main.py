def puissance(n):
    if n == 0:
        return 1
    else:
        return 2 * puissance(2, n-1)

n = input("mettez une puissance: ")
print(puissance(int(n)))