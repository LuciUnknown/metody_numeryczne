import horner
import math

def liniowa(a, b, arg):
    return [a*x+b for x in arg]

def bezwzgledna(arg):
    return [abs(x) for x in arg]

def wielomian(w,arg):
    return [horner.wynik(arg, w) for x in arg]

def trygonometryczna(f, arg):
    return [getattr(math, f)(x) for x in arg]
