# GCD
def gcd(x, y):
    # logic here
    if x > y:
        return gcd(x - y, y)
    elif x < y:
        return gcd(x, y - x)
    else:
        return x


print(gcd(10, 12))


