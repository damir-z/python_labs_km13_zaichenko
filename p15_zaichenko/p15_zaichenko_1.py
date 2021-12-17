from math import factorial

def binomial_coeffs(n):
    for n in range(n + 1):
        coeffs = (str(int(factorial(n) / ((factorial(k) * factorial(n - k))))) for k in range(n + 1))
        yield " ".join([*coeffs])

try:
    n = int(input("Enter n: "))
    if n < 0:
        raise ValueError
    for i in ["1", binomial_coeffs(n)][n != 0]:
        print(str(i))
except ValueError:
    print("Error. Invalid input!")