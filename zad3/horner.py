

def horner(x, tab):
    result = []
    for i in range(len(tab)):
        if i == 0:
            result.append(tab[i])
        else:
            result.append(x*result[i-1]+tab[i])
    return result.pop()

def wynik(x, tab):
    res = tab[0]
    for i in range(1, len(tab)):
        res = res*x + tab[i]
    return res
