import horner

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


print(sieczna_epsilon(-10, 10, [1,-3,2,-6], 0.00000001))
print(sieczna_iter(-10, 10, [1,-3,2,-6], 20))