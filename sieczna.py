import horner
import trygonometria

def sieczna_epsilon(a,b, tab, e):
    if horner.horner(a, tab) == 0.0:
        return a
    if horner.horner(b, tab) == 0.0:
        return b

    while abs(b - a > e):
        f_a = horner.horner(a, tab)
        f_b = horner.horner(b, tab)

        if f_a - f_b == 0:
            return b

        x = b - f_b * (b - a) / (f_b  - f_a)

        if horner.horner(x, tab) == 0.0:
            return x

        a = b
        b = x

    return b


    # return (a+b)/2

def sieczna_iter(a,b, tab, stop):
    i = 0
    if horner.horner(a, tab) == 0.0:
        return a
    if horner.horner(b, tab) == 0.0:
        return b

    while abs(i < stop):
        f_a = horner.horner(a, tab)
        f_b = horner.horner(b, tab)

        if f_a - f_b == 0:
            return b

        x = b - f_b * (b - a) / (f_b - f_a)

        if horner.horner(x, tab) == 0.0:
            return x

        a = b
        b = x
        i+=1

    return b


def trygonometria_epsilon(a, b, f, e):
    if f == "sin":
        func = trygonometria.sin
    elif f == "cos":
        func = trygonometria.cos
    elif f == "tan":
        func = trygonometria.tan
    elif f == "ctan":
        func = trygonometria.ctan
    else:
        return

    if func(a) == 0.0:
        return a
    if func(b) == 0.0:
        return b

    while abs(b - a) > e:
        f_a = func(a)
        f_b = func(b)

        if f_a-f_b == 0:
            return b

        x = b - f_b * (b - a) / (f_b - f_a)

        if func(x) == 0.0:
            return x

        a = b
        b = x

    return b

def trygonometria_iter(a, b, f, stop):
    if f == "sin":
        func = trygonometria.sin
    elif f == "cos":
        func = trygonometria.cos
    elif f == "tan":
        func = trygonometria.tan
    elif f == "ctan":
        func = trygonometria.ctan

    if func(a) == 0.0:
        return a
    if func(b) == 0.0:
        return b

    i=0
    while abs(i < stop):
        f_a = func(a)
        f_b = func(b)

        if f_a-f_b == 0:
            return b

        x = b - f_b * (b - a) / (f_b - f_a)

        if func(x) == 0.0:
            return x

        a = b
        b = x
        i+=1

    return b


print(sieczna_epsilon(-10, 10, [1,-3,2,-6], 0.00000001))
print(sieczna_iter(-10, 10, [1,-3,2,-6], 20))

print(trygonometria_iter(0.5, 5, 'sin', 20))
print(trygonometria_epsilon(0.5, 5, 'sin', 0.00000001))