
def legrande(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x

    p2 = 1.0
    p1 = x
    p = 0.0

    for i in range(1, n):
        p = ((2*i + 1) * x * p1 - i * p2) / (i + 1)
        p2 = p1
        p1 = p

    return p

def transform(a, b, x):
    return (2*x-a-b)/(b-a)