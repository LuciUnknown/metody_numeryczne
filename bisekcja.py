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

    while i < stop:
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
        if trygonometria.sin(a) == 0.0:
            return a
        if trygonometria.sin(b) == 0.0:
            return b

        while abs(b - a) > e:
            mid = (a + b) / 2

            if trygonometria.sin(mid) == 0.0:
                return mid

            if trygonometria.sin(a)*trygonometria.sin(mid) < 0.0:
                b = mid
            else:
                a = mid
    if f == "cos":
        if trygonometria.cos(a) == 0.0:
            return a
        if trygonometria.cos(b) == 0.0:
            return b

        while abs(b - a) > e:
            mid = (a + b) / 2

            if trygonometria.cos(mid) == 0.0:
                return mid
            if trygonometria.cos(a)*trygonometria.cos(mid) < 0.0:
                b = mid
            else:
                a = mid

    if f == "tan":
        if trygonometria.tan(a) == 0.0:
            return a
        if trygonometria.tan(b) == 0.0:
            return b

        while abs(b - a) > e:
            mid = (a + b) / 2

            if trygonometria.tan(mid) == 0.0:
                return mid

            if trygonometria.tan(a)*trygonometria.tan(mid) < 0.0:
                b = mid
            else:
                a = mid
    if f == "ctan":
        if trygonometria.ctan(a) == 0.0:
            return a
        if trygonometria.ctan(b) == 0.0:
            return b

        while abs(b - a) > e:
            mid = (a + b) / 2
            if trygonometria.ctan(mid) == 0.0:
                return mid

            if trygonometria.ctan(a)*trygonometria.ctan(mid) < 0.0:
                b = mid
            else:
                a = mid
    return (a+b)/2


def trygonometria_iter(a, b, f, stop):
    i = 0
    if f == "sin":
        if trygonometria.sin(a) == 0.0:
            return a
        if trygonometria.sin(b) == 0.0:
            return b

        while i < stop:
            mid = (a + b) / 2

            if trygonometria.sin(mid) == 0.0:
                return mid

            if trygonometria.sin(a) * trygonometria.sin(mid) < 0.0:
                b = mid
            else:
                a = mid
            i+=1
    if f == "cos":
        if trygonometria.cos(a) == 0.0:
            return a
        if trygonometria.cos(b) == 0.0:
            return b

        while i < stop:
            mid = (a + b) / 2

            if trygonometria.cos(mid) == 0.0:
                return mid
            if trygonometria.cos(a) * trygonometria.cos(mid) < 0.0:
                b = mid
            else:
                a = mid
            i += 1

    if f == "tan":
        if trygonometria.tan(a) == 0.0:
            return a
        if trygonometria.tan(b) == 0.0:
            return b

        while i < stop:
            mid = (a + b) / 2

            if trygonometria.tan(mid) == 0.0:
                return mid

            if trygonometria.tan(a) * trygonometria.tan(mid) < 0.0:
                b = mid
            else:
                a = mid
            i += 1
    if f == "ctan":
        if trygonometria.ctan(a) == 0.0:
            return a
        if trygonometria.ctan(b) == 0.0:
            return b

        while i < stop:
            mid = (a + b) / 2
            if trygonometria.ctan(mid) == 0.0:
                return mid

            if trygonometria.ctan(a) * trygonometria.ctan(mid) < 0.0:
                b = mid
            else:
                a = mid
            i += 1
    return (a + b) / 2


print(wielomian_epsilon(-10, 10, [1,-3,2,-6], 0.00000001))
print(wielomian_iter(-10, 10, [1,-3,2,-6], 20))

print(trygonometria_iter(0.5, 5, 'sin', 20))