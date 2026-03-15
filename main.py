import bisekcja
import horner
import trygonometria
import sieczna
import wykladnicza

wybor_funkcji = int(input("Wybierz funkcje nieliniową: \n1. Trygonometryczna \n2. Wielomian \n3. Wykładnicza \n4. Ich złożenia\nWybieram:"))
print("-----------------------------------------------------------")
wybor2 = int(input("Wybierz kryterium zatrzymania algorytmu: \n1.spełnienie warunku nałożonego na dokładność \n2.liczba iteracji \nWybieram: "))
print("-----------------------------------------------------------")

if wybor_funkcji == 1:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        print("Miejsce zerowe metodą bisekcji: ", bisekcja.epsilon(a,b,lambda x: trygonometria.sin(x) * trygonometria.cos(x), e))
        print("Miejsce zerowe metodą siecznych: ", sieczna.epsilon(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x), e))

    elif wybor2 == 2:
        top = int(input("Podaj liczbę iteracji: "))
        print("Miejsce zerowe metodą bisekcji: ", bisekcja.iter(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x), top))
        print("Miejsce zerowe metodą siecznych: ", sieczna.iter(a, b, lambda x: trygonometria.sin(x) * trygonometria.cos(x), top))

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

    elif wybor2 == 2:
        stop = int(input("Podaj liczbę iteracji: "))
        print("Miejsce zerowe metodą bisekcji: ",bisekcja.iter(a,b, lambda x: horner.horner(x, tab), stop))
        print("Miejsce zerowe metodą siecznych: ",sieczna.iter(a,b, lambda x: horner.horner(x, tab), stop))

    else:
        print("Wybrano zły numer kryterium zatrzymania")

elif wybor_funkcji == 3:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))
    tab = [input("Podaj współczynniki x od największego")]

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        wynik = bisekcja.epsilon(a, b, lambda x: wykladnicza.wykladnicza(x, tab), e)
        print("Miejsce zerowe metodą bisekcji: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
        wynik = sieczna.epsilon(a, b, lambda x: wykladnicza.wykladnicza(x, tab), e)
        print("Miejsce zerowe metodą siecznych: ", wynik[0])

    elif wybor2 == 2:
        stop = int(input("Podaj liczbę iteracji: "))
        print("Miejsce zerowe metodą bisekcji: ", bisekcja.iter(a, b, lambda x: wykladnicza.wykladnicza(x, tab), stop))
        print("Miejsce zerowe metodą siecznych: ", sieczna.iter(a, b, lambda x: wykladnicza.wykladnicza(x, tab), stop))

    else:
        print("Wybrano zły numer kryterium zatrzymania")

elif wybor_funkcji == 4:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))

    zlozenie1 = int(input("Wybierz pierwszą funkcje nieliniową do złożenia: \n1. Trygonometryczna \n2. Wielomian \n3. Wykładnicza"))
    zlozenie2 = int(input("Wybierz drugą funkcje nieliniową do złożenia: \n1. Trygonometryczna \n2. Wielomian \n3. Wykładnicza"))

    if zlozenie1 == 2 or zlozenie1 == 3:
        tab = [input("Podaj współczynniki x od największego")]

    elif zlozenie1 < 1 or zlozenie1 > 3:
        zlozenie2 = 0
        wybor2 = 0
        print("Wybrano zły numer funkcji nieliniowej do złożenia")

    if zlozenie2 == 1:
        funkcja = lambda x: trygonometria.sin(x) * trygonometria.cos(x)
    elif zlozenie2 == 2 or zlozenie2 == 3:
        tab = [input("Podaj współczynniki x od największego")]
        if zlozenie2 == 2:
            funkcja = lambda x: horner.horner(x, tab)
        if zlozenie2 == 3:
            funkcja = lambda x: wykladnicza.wykladnicza(x, tab)
    else:
        if zlozenie2 == 0:
            print("")
        else:
            wybor2 = 0
            print("Wybrano zły numer do złożenia 2. funkcji nieliniowej")

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        if zlozenie1 == 1:
            print("Miejsce zerowe metodą bisekcji: ",
                  bisekcja.epsilon(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), e))
            print("Miejsce zerowe metodą siecznych: ",
                  sieczna.epsilon(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), e))

        elif zlozenie1 == 2:
            wynik = bisekcja.epsilon(a, b, lambda x: horner.horner(funkcja(x), tab), e)
            print("Miejsce zerowe metodą bisekcji: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wynik = sieczna.epsilon(a, b, lambda x: horner.horner(funkcja(x), tab), e)
            print("Miejsce zerowe metodą siecznych: ", wynik[0])

        elif zlozenie1 == 3:
            wynik = bisekcja.epsilon(a, b, lambda x: wykladnicza.wykladnicza(funkcja(x), tab), e)
            print("Miejsce zerowe metodą bisekcji: ", wynik[0])
            print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")
            wynik = sieczna.epsilon(a, b, lambda x: wykladnicza.wykladnicza(funkcja(x), tab), e)
            print("Miejsce zerowe metodą siecznych: ", wynik[0])


    if wybor2 == 2:
        stop = int(input("Podaj liczbę iteracji: "))

        if zlozenie1 == 1:
            print("Miejsce zerowe metodą bisekcji: ",
                  bisekcja.iter(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), stop))
            print("Miejsce zerowe metodą siecznych: ",
                  sieczna.iter(a, b, lambda x: trygonometria.sin(funkcja(x)) * trygonometria.cos(funkcja(x)), stop))

        elif zlozenie1 == 2:
            print("Miejsce zerowe metodą bisekcji: ", bisekcja.iter(a, b, lambda x: horner.horner(funkcja(x), tab), stop))
            print("Miejsce zerowe metodą siecznych: ", sieczna.iter(a, b, lambda x: horner.horner(funkcja(x), tab), stop))


        elif zlozenie1 == 3:
            print("Miejsce zerowe metodą bisekcji: ",
                  bisekcja.iter(a, b, lambda x: wykladnicza.wykladnicza(funkcja(x), tab), stop))
            print("Miejsce zerowe metodą siecznych: ",
                  sieczna.iter(a, b, lambda x: wykladnicza.wykladnicza(funkcja(x), tab), stop))
    else:
        if wybor2 == 0:
            print("")
        print("Wybrano zły numer kryterium zatrzymania")


