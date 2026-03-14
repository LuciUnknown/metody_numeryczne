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


print(epsilon(-10, 10, lambda x: horner.horner(x, [1,-3,2,-6]), 0.00000001))
print(iter(-10, 10, lambda x: horner.horner(x,[1,-3,2,-6]), 100))

print(epsilon(0.5, 5,lambda x: trygonometria.sin(2*x)*trygonometria.cos(2*x), 0.00000001))
print(iter(0.5, 10, lambda x: trygonometria.sin(x+0.3), 20))

print(epsilon(-10, 10, lambda x: wykladnicza.wykladnicza(5,2*x, 125), 0.0001))
print(iter(-10, 10, lambda x: wykladnicza.wykladnicza(5,2*x, 125), 20))

print(epsilon(-5, 50, lambda x: math.exp(x)-5, 0.000001))

wykres.wykres(-10, 10, lambda x: trygonometria.sin(x))