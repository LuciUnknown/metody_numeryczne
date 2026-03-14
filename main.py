import bisekcja
import horner
import trygonometria
import sieczna

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
    tab = [input("Podaj współczynniki x od największego")]

    if wybor2 == 1:
        e = float(input("Podaj oczekiwaną dokładność: "))
        wynik = bisekcja.epsilon(a, b, lambda x: horner.horner(x, tab), e)
        print("Miejsce zerowe metodą bisekcji: ", wynik[0])
        print("Wynik otrzymano po liczbie ", wynik[1], " iteracji")

    elif wybor2 == 2:
        stop = int(input("Podaj liczbę iteracji: "))
        print("Miejsce zerowe metodą bisekcji: ",bisekcja.iter(a,b, lambda x: horner.horner(x, tab), stop))

    else:
        print("Wybrano zły numer kryterium zatrzymania")
# | wybor_funkcji == 3 | wybor_funkcji == 4: