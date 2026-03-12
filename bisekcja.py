import horner
import trygonometria

def wielomian_epsilon(a,b, tab, e):
    if horner.horner(a, tab) == 0.0:
        return a
    if horner.horner(b, tab) == 0.0:
        return b

    while abs(b - a) >= e:
        mid = (a + b) / 2

        if horner.horner(mid, tab) == 0.0:
            return mid

        if horner.horner(a,tab)*horner.horner(mid,tab) < 0.0:
            b = mid
        else:
            a = mid

    return (a+b)/2

def wielomian_iter(a,b, tab, stop):
    i = 0
    if horner.horner(a, tab) == 0.0:
        return a
    if horner.horner(b, tab) == 0.0:
        return b

    while abs(i < stop):
        mid = (a + b) / 2

        if horner.horner(mid, tab) == 0.0:
            return mid

        if horner.horner(a,tab)*horner.horner(mid,tab) < 0.0:
            b = mid
        else:
            a = mid
        i+=1

    return (a+b)/2

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

    while abs(b - a) >= e:
        mid = (a + b) / 2

        if func(mid) == 0.0:
            return mid

        if func(a) * func(mid) < 0.0:
            b = mid
        else:
            a = mid
    return (a + b) / 2


def trygonometria_iter(a, b, f, stop):
    i = 0
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

    while abs(i < stop):
        mid = (a + b) / 2
        if func == 0.0:
            return mid

        if func(a) * func(mid) < 0.0:
            b = mid
        else:
            a = mid
        i += 1
    return (a + b) / 2


print(wielomian_epsilon(-10, 10, [1,-3,2,-6], 0.00000001))
print(wielomian_iter(-10, 10, [1,-3,2,-6], 20))

print(trygonometria_epsilon(0.5, 5, 'sin', 0.00000001))
print(trygonometria_iter(0.5, 5, 'sin', 20))