
def simpson(a, b, n, f):
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)

    for i in range(2, n, 2):
        suma += 2 * f(a + i * h)

    return h / 3 * suma


def newton_cotes(f, a, b, epsilon):
    iteracja = 0
    n = 2

    last = simpson(a, b, n, f)

    while True:
        n *= 2
        new = simpson(a, b, n, f)
        if abs(new - last) < epsilon:
            return new, iteracja
        last = new
        iteracja += 1