import horner
import trygonometria
import wykladnicza
import wykres

def epsilon(a,b, tab, e):
    i = 0
    if tab(a) == 0.0:
        return a, i
    if tab(b) == 0.0:
        return b, i

    if tab(a) * tab(b) >= 0.0:
        print("Nie ma zera w przedziale (funkcja nie zmienia znaku w podanym przedziale)")

    while abs(b - a) > e:
        f_a = tab(a)
        f_b = tab(b)

        if f_a - f_b == 0:
            return b, i

        x = b - (f_b * (b - a)) / (f_b  - f_a)

        if tab(x) == 0.0:
            return x, i

        a = b
        b = x
        i += 1

    return b, i


def iter(a, b, tab, stop):
    i = 0
    if tab(a) == 0.0:
        return a, i
    if tab(b) == 0.0:
        return b, i

    if tab(a) * tab(b) >= 0.0:
        print("Nie ma zera w przedziale (funkcja nie zmienia znaku w podanym przedziale)")

    while i < stop:
        f_a = tab(a)
        f_b = tab(b)

        if f_a - f_b == 0:
            return b, i

        x = b - f_b * (b - a) / (f_b - f_a)

        if tab(x) == 0.0:
            return x, i

        a = b
        b = x
        i += 1

    return b, i