import numpy as np
from legendre import gauss_legendre_quadrature
from newton_cotes import newton_cotes


def funkcja_podcalkowa(val):
    if val == '1':
        return lambda x: np.sin(x) + x ** 2
    elif val == '2':
        return lambda x: pow(x, 5) + pow(x, 2)
    elif val == '3':
        return lambda x: np.sqrt(x)

    return None


def main():
    while True:
        print("\n=== Menu Całkowania Numerycznego ===")
        print("Wybierz funkcje")
        print("1. f(x) = sin(x) + x^2")
        print("2. f(x) = (x^5 + x^2)")
        print("3. f(x) = sqrt(x)")

        fun = input("Wybierz numer funkcji (1-2): ")

        print("1. Kwadratura Gaussa-Legendre'a (2-5 węzłów)")
        print("2. Metoda Newtona-Cotesa (złożona Simpsona)")
        print("3. Zakończ program")

        wybor = input("Wybierz opcję (1-3): ")

        if wybor == '3':
            break

        if wybor in ('1', '2'):
            try:
                a = float(input("Podaj dolną granicę całkowania (a): "))
                b = float(input("Podaj górną granicę całkowania (b): "))
                
                if wybor == '1':
                    print(f"\nWyniki dla kwadratury Gaussa-Legendre'a w przedziale [{a}, {b}):")
                    for n in range(2, 6):
                        wynik = gauss_legendre_quadrature(funkcja_podcalkowa(fun), a, b, n)
                        print(f"Dla n={n} węzłów: {wynik:.8f}")
                
                elif wybor == '2':
                    epsilon = float(input("Podaj dokładność (epsilon, np. 0.0001): "))
                    wynik, iteracje = newton_cotes(funkcja_podcalkowa(fun), a, b, epsilon)
                    print(f"\nWynik całkowania: {wynik:.8f}")
                    print(f"Liczba iteracji: {iteracje}")
            
            except ValueError:
                print("Błąd: Wprowadzono niepoprawną wartość. Wymagana liczba.")
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == '__main__':
    main()