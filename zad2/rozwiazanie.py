import numpy as np
import file_reader
import gausse_seidel

def rozwiaz_przyklad(numer,war_stop):
    sciezka = f"przyklady_do_rozw/przyklad{numer}.txt"
    print(f"\n--- Rozwiązywanie przykładu {numer} z pliku {sciezka} ---")

    try:
        tabela = file_reader.read_coefficient(sciezka)
        if not tabela:
            print("Plik jest pusty.")
            return

        A = []
        b = []
        for wiersz in tabela:
            A.append(wiersz[:-1])  # Wszystko oprócz ostatniego elementu w rzędzie
            b.append(wiersz[-1])  # Tylko ostatni element w rzędzie

        A = np.array(A)
        b = np.array(b)

        if gausse_seidel.diag_dominacja(A):

            if war_stop == 1:
                iteracje = int(input("Podaj liczbę iteracji: "))
                wynik = gausse_seidel.iter_Gauss_Seidel(A, b, max_iter=iteracje)
            elif war_stop == 2:
                epsilon = float(input("Podaj dokładność: "))
                wynik = gausse_seidel.acc_Gauss_Seidel(A, b, tol=epsilon)
            print("Znalezione rozwiązanie (x):", wynik)

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {sciezka}.")


def wybrany_plik(sciezka, war_stop):
    print(f"\n--- Rozwiązywanie układu z pliku {sciezka} ---")

    try:
        tabela = file_reader.read_coefficient(sciezka)
        if not tabela:
            print("Plik jest pusty.")
            return

        A = []
        b = []
        for wiersz in tabela:
            A.append(wiersz[:-1])  # Wszystko oprócz ostatniego elementu w rzędzie
            b.append(wiersz[-1])  # Tylko ostatni element w rzędzie

        A = np.array(A)
        b = np.array(b)

        if gausse_seidel.diag_dominacja(A):
            if war_stop == 1:
                iteracje = int(input("Podaj liczbę iteracji: "))
                wynik = gausse_seidel.iter_Gauss_Seidel(A, b, max_iter=iteracje)
            elif war_stop == 2:
                epsilon = float(input("Podaj dokładność: "))
                wynik = gausse_seidel.acc_Gauss_Seidel(A, b, tol=epsilon)
            print("Znalezione rozwiązanie (x):", wynik)

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {sciezka}.")