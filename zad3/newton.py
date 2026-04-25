
def iloraz_roznicowy(x, y):
    n = len(y)
    coef = list(y)
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            coef[j] = (coef[j] - coef[j-1]) / (x[j] - x[j-i])
    return coef


def newton(x, coef, t):
    n = len(coef)

    result = coef[0]
    nawiasy = 1.0

    for i in range(1, n):
        nawiasy *= (t - x[i-1])
        result += coef[i] * nawiasy
    return result
