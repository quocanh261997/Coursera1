import math

def multiply(x, y):
    if x<10 or y<10:
        return x*y
    m = len(str(x))
    m2 = m//2
    high1, low1 = x // (10**m2), x % (10**m2)
    high2, low2 = y // (10**m2), y % (10**m2)
    z0 = multiply(low1,low2)
    z1 = multiply((low1+high1),(low2+high2))
    z2 = multiply(high1,high2)
    return z2*(10**(2*m2))+(z1-z2-z0)*(10**(m2))+z0

a = multiply(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
print(1234*5678)
print(a)

