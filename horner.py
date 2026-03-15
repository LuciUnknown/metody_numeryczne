

def horner(x, tab):
    result = []
    for i in range(len(tab)):
        if i == 0:
            result.append(tab[i])
        else:
            result.append(x*result[i-1]+tab[i])
    return result.pop()

def y(x, tab):
    wynik = 0
    for i in range(len(tab)):
        wynik += tab[i]*pow(x, len(tab)-i-1)
    return wynik
