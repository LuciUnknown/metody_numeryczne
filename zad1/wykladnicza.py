import math

def wykladnicza(a,x, b):
    l = 1
    p = 1
    while a != b:
        if a < b:
            b/=a
            p+=1
        else:
            a/=b
            l+=1
    return l*x-p