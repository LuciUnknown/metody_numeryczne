import horner
import trygonometria
import wykladnicza

def epsilon(a,b, tab, e):
    if tab(a) == 0.0:
        return a
    if tab(b) == 0.0:
        return b

    while abs(b - a) > e:
        f_a = tab(a)
        f_b = tab(b)

        if f_a - f_b == 0:
            return b

        x = b - f_b * (b - a) / (f_b  - f_a)

        if tab(x) == 0.0:
            return x

        a = b
        b = x

    return b


def iter(a,b, tab, stop):
    i = 0
    if tab(a) == 0.0:
        return a
    if tab(b) == 0.0:
        return b

    while i < stop:
        f_a = tab(a)
        f_b = tab(b)

        if f_a - f_b == 0:
            return b

        x = b - f_b * (b - a) / (f_b - f_a)

        if tab(x) == 0.0:
            return x

        a = b
        b = x
        i+=1

    return b



print(epsilon(-10, 10, lambda x: horner.horner(x,[1,-3,2,-6]), 0.00000001))
print(iter(-10, 10,  lambda x: horner.horner(x,[1,-3,2,-6]), 20))

print(iter(0.5, 5, lambda x: trygonometria.sin(2*x), 20))
print(epsilon(0.5, 5,  lambda x: trygonometria.sin(2*x), 0.00000001))

print(epsilon(-10, 10, lambda x: wykladnicza.wykladnicza(5,2*x, 125), 0.0001))
print(iter(-10, 10, lambda x: wykladnicza.wykladnicza(5,2*x, 125), 20))