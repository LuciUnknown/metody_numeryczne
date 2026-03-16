import math
from ctypes import wstring_at

import bisekcja
import horner
import trygonometria
import sieczna
import wykladnicza
import wykres

wybor_funkcji = int(input("Wybierz funkcje nieliniową: \n1. Trygonometryczna \n2. Wielomian \n3. Wykładnicza \n4. Ich złożenia\nWybieram:"))
print("-----------------------------------------------------------")
wybor2 = int(input("Wybierz kryterium zatrzymania algorytmu: \n1.spełnienie warunku nałożonego na dokładność \n2.liczba iteracji \nWybieram: "))
print("-----------------------------------------------------------")

if wybor_funkcji == 1:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        wynik = bisekcja.epsilon(a,b,lambda x: trygonometria.sin(x) * trygonometria.cos(x), e)
        print("Miejsce zerowe metodą bisekcji: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wynik = sieczna.epsilon(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x), e)
        print("Miejsce zerowe metodą siecznych: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wykres.wykres(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x))

    elif wybor2 == 2:
        top = int(input("Podaj liczbę iteracji: "))
        print("Miejsce zerowe metodą bisekcji: ", bisekcja.iter(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x), top))
        print("Miejsce zerowe metodą siecznych: ", sieczna.iter(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x), top))
        wykres.wykres(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x))

    else:
        print("Wybrano zły numer kryterium zatrzymania")



elif wybor_funkcji == 2:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))
    tab = list(map(int, input("Podaj współczynniki x od największego").split(",")))

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        wynik = bisekcja.epsilon(a, b, lambda x: horner.horner(x, tab), e)
        print("Miejsce zerowe metodą bisekcji: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wynik = sieczna.epsilon(a, b, lambda x:  horner.horner(x, tab), e)
        print("Miejsce zerowe metodą siecznych: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wykres.wykres(a, b, lambda x:  horner.y(x, tab))

    elif wybor2 == 2:
        stop = int(input("Podaj liczbę iteracji: "))
        wynik = bisekcja.iter(a,b, lambda x: horner.horner(x, tab), stop)
        print("Miejsce zerowe metodą bisekcji: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wynik = sieczna.iter(a,b, lambda x: horner.horner(x, tab), stop)
        print("Miejsce zerowe metodą siecznych: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wykres.wykres(a,b, lambda x: horner.y(x, tab))

    else:
        print("Wybrano zły numer kryterium zatrzymania")

elif wybor_funkcji == 3:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        wynik = bisekcja.epsilon(a, b, lambda x: math.exp(x+3)-7, e)
        print("Miejsce zerowe metodą bisekcji: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wynik = sieczna.epsilon(a, b, lambda x: math.exp(x-3)-7, e)
        print("Miejsce zerowe metodą siecznych: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wykres.wykres(a, b, lambda x: math.exp(x+3)-7)

    elif wybor2 == 2:
        stop = int(input("Podaj liczbę iteracji: "))
        wynik = bisekcja.iter(a, b, lambda x: math.exp(x+3)-7, stop)
        print("Miejsce zerowe metodą bisekcji: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wynik = sieczna.iter(a, b, lambda x: math.exp(x+3)-7, stop)
        print("Miejsce zerowe metodą siecznych: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wykres.wykres(a, b, lambda x: math.exp(x+3)-7)

    else:
        print("Wybrano zły numer kryterium zatrzymania")

elif wybor_funkcji == 4:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))

    zlozenie1 = int(input("Wybierz pierwszą funkcje nieliniową do złożenia: \n1. Trygonometryczna \n2. Wielomian \n3. Wykładnicza"))
    zlozenie2 = int(input("Wybierz drugą funkcje nieliniową do złożenia: \n1. Trygonometryczna \n2. Wielomian \n3. Wykładnicza"))

    if zlozenie1 == 2:
        tab = list(map(int, input("Podaj współczynniki x od największego").split(",")))

    elif zlozenie1 < 1 or zlozenie1 > 3:
        zlozenie2 = 0
        wybor2 = 0
        print("Wybrano zły numer funkcji nieliniowej do złożenia")

    if zlozenie2 == 1:
        funkcja = lambda x: trygonometria.sin(x) * trygonometria.cos(x)
    elif zlozenie2 == 2:
        tab = list(map(int,input("Podaj współczynniki x od największego").split(",")))
        funkcja = lambda x: horner.horner(x, tab)
    elif zlozenie2 == 3:
        funkcja = lambda x: math.exp(x+3)-7
    else:
        if zlozenie2 == 0:
            print("")
        else:
            wybor2 = 0
            print("Wybrano zły numer do złożenia 2. funkcji nieliniowej")

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        if zlozenie1 == 1:
            wynik = bisekcja.epsilon(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), e)
            print("Miejsce zerowe metodą bisekcji: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wynik = sieczna.epsilon(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), e)
            print("Miejsce zerowe metodą siecznych: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wykres.wykres(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)))

        elif zlozenie1 == 2:
            wynik = bisekcja.epsilon(a, b, lambda x: horner.horner(funkcja(x), tab), e)
            print("Miejsce zerowe metodą bisekcji: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wynik = sieczna.epsilon(a, b, lambda x: horner.horner(funkcja(x), tab), e)
            print("Miejsce zerowe metodą siecznych: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wykres.wykres(a, b, lambda x: horner.y(funkcja(x), tab))

        elif zlozenie1 == 3:
            wynik = bisekcja.epsilon(a, b, lambda x: math.exp(funkcja(x)+3)-7, e)
            print("Miejsce zerowe metodą bisekcji: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wynik = sieczna.epsilon(a, b, lambda x: math.exp(funkcja(x)+3)-7, e)
            print("Miejsce zerowe metodą siecznych: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wykres.wykres(a, b, lambda x: math.exp(funkcja(x)+3)-7)


    if wybor2 == 2:
        stop = int(input("Podaj liczbę iteracji: "))

        if zlozenie1 == 1:
            print("Miejsce zerowe metodą bisekcji: ",
                  bisekcja.iter(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), stop))
            print("Miejsce zerowe metodą siecznych: ",
                  sieczna.iter(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), stop))

        elif zlozenie1 == 2:
            wynik = bisekcja.iter(a, b, lambda x: horner.horner(funkcja(x), tab), stop)
            print("Miejsce zerowe metodą bisekcji: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wynik = sieczna.iter(a, b, lambda x: horner.horner(funkcja(x), tab), stop)
            print("Miejsce zerowe metodą siecznych: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wykres.wykres(a, b, lambda x: horner.horner(funkcja(x), tab))


        elif zlozenie1 == 3:
            print("Miejsce zerowe metodą bisekcji: ",
                  bisekcja.iter(a, b, lambda x: math.exp(x+3)-7, stop))
            print("Miejsce zerowe metodą siecznych: ",
                  sieczna.iter(a, b, lambda x: math.exp(x+3)-7, stop))
    else:
        if wybor2 == 0:
            print("")
        print("Wybrano zły numer kryterium zatrzymania")


