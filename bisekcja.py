import horner

def wielomian_epsilon(a,b, tab, e):
    if horner.horner(a, tab) == 0.0:
        return a
    if horner.horner(b, tab) == 0.0:
        return b

    while b - a > e:
        mid = (a + b) / 2

        if horner.horner(mid, tab) == 0.0:
            return mid

        if horner.horner(a,tab)*horner.horner(mid,tab) < 0.0:
            b = mid
        else:
            a = mid

    return (a+b)/2

print(wielomian_epsilon(-10, 10, [1,-3,2,-6], 0.0001))