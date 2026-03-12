import bisekcja
import sieczna

wybor_funkcji = int(input("Wybierz funkcje nieliniową: \n1. Trygonometryczna \n2. Wielomian \n3. Wykładnicza \n4. Ich złożenia\nWybieram:"))
print("-----------------------------------------------------------")
wybor2 = input("Wybierz kryterium zatrzymania algorytmu: \n1.spełnienie warunku nałożonego na dokładność \n2.liczba iteracji \nWybieram: ")
print("-----------------------------------------------------------")

if wybor_funkcji == 1:
    a = int(input("Podaj początek przedziału (a)"))
    b = int(input("Podaj koniec przedziału (b)"))
    tryg = input("Podaj rodzaj funkcji trygonometrycznej (sin/cos/tan/ctan): ")
    if tryg not in ["sin", "cos", "tan", "ctan"]:
        print("Co ty odpier...")
    # if wybor2 == 1:
    #
    # elif wybor2 == 2:
    #
    # else:
    #     print("Wybrano zły numer kryterium zatrzymania")

# elif wybor_funkcji == 3:
# elif wybor_funkcji == 2 | wybor_funkcji == 4:
