import horner
import trygonometria
import wykladnicza

def epsilon(a, b, f, e):
    if f(a) == 0.0:
        return a
    if f(b) == 0.0:
        return b

    while abs(b - a) >= e:
        mid = (a + b) / 2

        if f(mid) == 0.0:
            return mid

        if f(a) * f(mid) < 0.0:
            b = mid
        else:
            a = mid
    return (a + b) / 2


def iter(a, b, f, stop):
    i = 0

    if f(a) == 0.0:
        return a
    if f(b) == 0.0:
        return b

    while abs(i < stop):
        mid = (a + b) / 2
        if f(mid) == 0.0:
            return mid

        if f(a) * f(mid) < 0.0:
            b = mid
        else:
            a = mid
        i += 1
    return (a + b) / 2


print(epsilon(-10, 10, lambda x: horner.horner(x, [1,-3,2,-6]), 0.00000001))
print(iter(-10, 10, lambda x: horner.horner(x,[1,-3,2,-6]), 100))

print(epsilon(0.5, 5,lambda x: trygonometria.sin(2*x), 0.00000001))
print(iter(0.5, 5, lambda x: trygonometria.sin(2*x), 20))

print(epsilon(-10, 10, lambda x: wykladnicza.wykladnicza(5,2*x, 125), 0.0001))
print(iter(-10, 10, lambda x: wykladnicza.wykladnicza(5,2*x, 125), 20))