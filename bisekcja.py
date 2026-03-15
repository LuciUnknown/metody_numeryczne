import horner
import trygonometria
import wykladnicza
import wykres
import math

def epsilon(a, b, f, e):
    i = 0
    if f(a) == 0.0:
        return a, i
    if f(b) == 0.0:
        return b, i

    while abs(b - a) >= e:
        mid = (a + b) / 2

        if f(mid) == 0.0:
            return mid, i

        if f(a) * f(mid) < 0.0:
            b = mid
        else:
            a = mid
        i+=1
    return (a + b) / 2, i


def iter(a, b, f, stop):
    i = 0

    if f(a) == 0.0:
        return a, i
    if f(b) == 0.0:
        return b, i

    while abs(i < stop):
        mid = (a + b) / 2
        if f(mid) == 0.0:
            return mid, i

        if f(a) * f(mid) < 0.0:
            b = mid
        else:
            a = mid
        i += 1
    return (a + b) / 2, i